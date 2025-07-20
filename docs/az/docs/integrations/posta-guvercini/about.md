# Posta Guvercini

## Rəsmi Dokumentasiya (v1) { #official-documentation }

[İngliscə](https://www.poctgoyercini.com/api_json/swagger/ui/index#/)

## İstifadəsi { #usage }

Bu sorğulardan istifadə etmək üçün, bu dəyərləri "environment variable"-larına əlavə etməlisiniz: `POSTA_GUVERCINI_USERNAME`, `POSTA_GUVERCINI_PASSWORD`, `POSTAGUVERCINI_MESSAGE_ID`

## Sorğular listi { #list-of-requests }

| Sorğu metodu                                                                                       | Məqsəd                            |        PostaGuvercini API        |
| :------------------------------------------------------------------------------------------------- | :-------------------------------- | :------------------------------: |
| [`send_single_sms`][integrify.postaguvercini.client.PostaGuverciniClientClass.send_single_sms]     | Tək nömrəyə sms göndərilməsi      |   `/api_json/v1/Sms/Send_1_N`    |
| [`send_multiple_sms`][integrify.postaguvercini.client.PostaGuverciniClientClass.send_multiple_sms] | Bir neçə nömrəyə sms göndərilməsi |   `/api_json/v1/Sms/Send_N_N`    |
| [`get_status`][integrify.postaguvercini.client.PostaGuverciniClientClass.get_status]               | SMS-in statusunu yoxlamaq         |    `/api_json/v1/Sms/Status`     |
| [`credit_balance`][integrify.postaguvercini.client.PostaGuverciniClientClass.credit_balance]       | Balansın yoxlanılması             | `/api_json/v1/Sms/CreditBalance` |
