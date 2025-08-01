import os
from datetime import datetime

import time_machine

from integrify.postaguvercini.client import PostaGuverciniClientClass
from integrify.postaguvercini.types import timestamp_to_str
from integrify.test import live
from tests.conftest import requires_env


def test_timestamp_to_str_correct_str():
    assert timestamp_to_str('20250403 02:01') == '20250403 02:01'


def test_timestamp_to_str_wrong_str():
    assert timestamp_to_str('20250403-02:01') is None


@time_machine.travel('2025-04-03 02:01')
def test_timestamp_to_str_datetime():
    assert timestamp_to_str(datetime.now()) == '20250403 02:01'


@requires_env('PHONE_NUMBER_1')
@live
def test_single_sms_request(postaguvercini_client: PostaGuverciniClientClass):
    old_balance = postaguvercini_client.credit_balance().body.result.balance

    postaguvercini_client.send_single_sms(message='test', receivers=[os.getenv('PHONE_NUMBER_1')])

    new_balance = postaguvercini_client.credit_balance().body.result.balance

    assert new_balance + 1 == old_balance


@requires_env('PHONE_NUMBER_1', 'PHONE_NUMBER_2')
@live
def test_multiple_sms_request(postaguvercini_client: PostaGuverciniClientClass):
    old_balance = postaguvercini_client.credit_balance().body.result.balance

    postaguvercini_client.send_multiple_sms(
        messages=[
            {'receiver': os.getenv('PHONE_NUMBER_1'), 'message': 'Test SMS 1'},
            {'receiver': os.getenv('PHONE_NUMBER_2'), 'message': 'Test SMS 2'},
        ]
    )

    new_balance = postaguvercini_client.credit_balance().body.result.balance

    assert new_balance + 2 == old_balance


@requires_env('POSTAGUVERCINI_MESSAGE_ID')
def test_status_request(postaguvercini_client: PostaGuverciniClientClass):
    message_id = os.getenv('POSTAGUVERCINI_MESSAGE_ID')
    resp = postaguvercini_client.get_status(message_ids=[message_id])

    assert resp.status_code == 200
    assert resp.body.status_code == 200
    assert resp.body.result[0].message_id == message_id
    assert resp.body.result[0].sms_status_description == 'Çatdı'


@requires_env()
def test_credit_balance_request(postaguvercini_client: PostaGuverciniClientClass):
    resp = postaguvercini_client.credit_balance()

    assert resp.body.status_code == 200
    assert resp.body.status_description == 'Transaction done successfully'
    assert resp.body.result.balance == 22
