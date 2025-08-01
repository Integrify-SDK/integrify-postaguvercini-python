from functools import partial

import pytest

from integrify.postaguvercini.client import PostaGuverciniClientClass
from integrify.test import pytest_addoption  # noqa: F401
from integrify.test import requires_env as _requires_env
from tests.mocks import *  # noqa: F403

requires_env = partial(_requires_env, 'POSTA_GUVERCINI_USERNAME', 'POSTA_GUVERCINI_PASSWORD')


@pytest.fixture(scope='package')
def postaguvercini_client():
    yield PostaGuverciniClientClass()
