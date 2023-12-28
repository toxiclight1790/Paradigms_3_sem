from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, CallbackContext, Filters
from database import *
# Шаги для диалога
STEP1, STEP2, STEP3, STEP4, STEP5 = range(5)

# Обработка команды /start
def start(update, context):
    update.message.reply_text("Привет! Я чат-бот. Давай проведем небольшой опрос. Готов?")
    return STEP1

# Обработка первого вопроса
def ask_question1(update, context):
    update.message.reply_text("Отлично! Первый вопрос: Как тебя зовут?")
    return STEP2

# Обработка второго вопроса
def ask_question2(update, context):
    context.user_data['name'] = update.message.text
    update.message.reply_text(f"Приятно познакомиться, {context.user_data['name']}! Теперь второй вопрос: Сколько тебе лет?")
    return STEP3

# Обработка третьего вопроса
def ask_question3(update, context):
    context.user_data['age'] = update.message.text
    update.message.reply_text("Отлично! Третий вопрос: Где ты живешь?")
    return STEP4

# Обработка четвертого вопроса
def ask_question4(update, context):
    context.user_data['location'] = update.message.text
    update.message.reply_text("Хорошо! Четвертый вопрос: Какой твой любимый цвет?")
    return STEP5

# Обработка пятого вопроса
def ask_question5(update, context):
    context.user_data['favorite_color'] = update.message.text
    # Сохранение ответов в базу данных
    save_user_response(update.message.from_user.id, context.user_data)

    update.message.reply_text(f"Отлично, {context.user_data['name']}! Спасибо за ответы. Мы закончили опрос.")
    show_answers(update, context)
    return ConversationHandler.END

def save_user_response(user_id, user_data):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Замените 'user_id' на ваш уникальный идентификатор пользователя
    cursor.execute('''
        INSERT OR REPLACE INTO user_responses (user_id, name, age, location, favorite_color)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, user_data.get('name'), user_data.get('age'), user_data.get('location'), user_data.get('favorite_color')))

    conn.commit()
    conn.close()

# Функция вывода ответов пользователя
def show_answers(update, context):
    user_data = context.user_data
    answers = [
        f"Имя: {user_data.get('name', 'Нет ответа')}",
        f"Возраст: {user_data.get('age', 'Нет ответа')}",
        f"Место жительства: {user_data.get('location', 'Нет ответа')}",
        f"Любимый цвет: {user_data.get('favorite_color', 'Нет ответа')}",
    ]

    response_text = "\n".join(answers)
    update.message.reply_text(f"Вот ваши ответы:\n{response_text}")

# Функция отмены опроса
def cancel(update, context):
    update.message.reply_text("Опрос отменен.")
    return ConversationHandler.END

def main():
    updater = Updater('5996777299:AAFOESn7zVViUhF8sG8rWGgMHWwhRkNmpH8', use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STEP1: [MessageHandler(Filters.text & ~Filters.command, ask_question1)],
            STEP2: [MessageHandler(Filters.text & ~Filters.command, ask_question2)],
            STEP3: [MessageHandler(Filters.text & ~Filters.command, ask_question3)],
            STEP4: [MessageHandler(Filters.text & ~Filters.command, ask_question4)],
            STEP5: [MessageHandler(Filters.text & ~Filters.command, ask_question5)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
        allow_reentry=True,
    )

    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
