from django.conf import settings
from celery import shared_task
import requests


@shared_task
def send_on_start(chat_id) -> None:
    """Запрос к ТG в ответ на /start"""
    response = requests.post(
        url=f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage',
        json={
            'chat_id': chat_id,
            'text': 'Привет, а дай номер',
            'reply_markup': {
                'keyboard': [[
                    {'text': 'Отправить', 'request_contact': True},
                ], ],
                'one_time_keyboard': True,
            }
        }
    )
    print(response.status_code)


@shared_task
def send_to_nova(phone, login) -> None:
    """Запрос к Nova в ответ на 'contact'"""
    response = requests.post(
        url=f'https://s1-nova.ru/app/private_test_python/',
        headers={'Content-type': 'application/json'},
        json={
            'phone': phone,
            'login': login,
        }
    )
    print(response.status_code)


def set_webhook():
    """Подключить webhook (если отвалился)"""
    response = requests.post(
        url=f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/setWebhook'
            f'?url=https://158.160.55.223/api/message/',
        headers={
            'Content-Type': 'multipart/form-data; boundary=WebAppBoundary'
        },
        files={'filename': ('YOURPUBLIC.pem', open('../cert/YOURPUBLIC.pem', 'rb'), 'InputFile')}
    )
    return response.json()


def get_webhook_info():
    """Получить информацию от TG API /getWebhookInfo"""
    response = requests.post(
        url=f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/getWebhookInfo',
    )
    return response.json()
