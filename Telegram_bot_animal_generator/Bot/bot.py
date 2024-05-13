from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from neural_network.animal_generator import generate_animal_image
# Функция для обработки команды /start
def start(update: Bot, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который генерирует картинки с животными. Введите /generate, чтобы получить картинку.')

# Функция для обработки команды /generate
def generate(update: Bot, context: CallbackContext) -> None:
    # Генерируем изображение с животным
    animal_image = generate_animal_image()
    # Отправляем изображение пользователю
    update.message.reply_photo(animal_image)
    pass

# Функция для запуска бота
def main() -> None:
    token = "7162762804:AAFpHcd57Ns6KjyEWnAwWTqsIM3eSLjsq9k"  # Получение токена из переменной окружения
    updater = Updater.from_token(token)
    dispatcher = updater.dispatcher

    # Добавляем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("generate", generate))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    bot_main()