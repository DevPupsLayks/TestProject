from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from neural_network.animal_generator import generate_animal_image
# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который генерирует картинки с животными. Введите /generate, чтобы получить картинку.')

# Функция для обработки команды /generate
def generate(update: Update, context: CallbackContext) -> None:
    # Генерируем изображение с животным
    animal_image = generate_animal_image()
    # Отправляем изображение пользователю
    update.message.reply_photo(animal_image)
    pass

# Функция для запуска бота
def main() -> None:
    # Замените 'YOUR_TOKEN' на ваш токен Telegram бота
    updater = Updater(token="7162762804:AAFpHcd57Ns6KjyEWnAwWTqsIM3eSLjsq9k")
    dispatcher = updater.dispatcher

    # Добавляем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("generate", generate))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()