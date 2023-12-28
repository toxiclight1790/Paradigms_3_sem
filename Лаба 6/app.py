"""
from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = '5996777299:AAFOESn7zVViUhF8sG8rWGgMHWwhRkNmpH8'
WEBHOOK_URL = 'https://48f8-176-120-65-16.ngrok-free.app/5996777299:AAFOESn7zVViUhF8sG8rWGgMHWwhRkNmpH8'

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

@app.route(f'/{TOKEN}', methods=['POST'])
def main():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        message_text = data['message']['text']

        if message_text.lower() == 'привет':
            send_message(chat_id, 'Привет! Я ваш чат-бот.')

    return '', 200

if __name__ == '__main__':
    set_webhook_url = f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}'
    response = requests.get(set_webhook_url)

    if response.json().get('ok'):
        print('Webhook установлен успешно!')
        app.run(port=5000)
    else:
        print('Ошибка установки вебхука. Проверьте URL и токен.')

------------------------------------------------------------------------------------------------------------"""

from flask import Flask, request
import requests

app = Flask(__name__)

# Замените 'ваш-токен-от-BotFather' на реальный токен, полученный от @BotFather
TOKEN = '5996777299:AAFOESn7zVViUhF8sG8rWGgMHWwhRkNmpH8'

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

@app.route(f'/{TOKEN}', methods=['POST'])
def main():
    # Получаем данные из входящего JSON-запроса
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        message_text = data['message']['text']

        # Обрабатываем приветствие
        if message_text.lower() == 'привет':
            send_message(chat_id, 'Привет! Я ваш чат-бот.')

    return '', 200

if __name__ == '__main__':
    # Устанавливаем вебхук для бота
    set_webhook_url = f'https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://59cb-176-120-65-16.ngrok-free.app/5996777299:AAFOESn7zVViUhF8sG8rWGgMHWwhRkNmpH8'
    response = requests.get(set_webhook_url)

    if response.json().get('ok'):
        print('Webhook установлен успешно!')
        app.run(port=5000)
    else:
        print('Ошибка установки вебхука. Проверьте URL и токен.')
