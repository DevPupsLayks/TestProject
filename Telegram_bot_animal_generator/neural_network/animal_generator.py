from PIL import Image, ImageDraw
import random

# Функция для генерации изображения с животным
def generate_animal_image() -> Image.Image:
    # Создаем пустое изображение
    image = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(image)

    # Рисуем простое изображение животного (для примера)
    # Здесь можно добавить вызов функции генерации изображения с помощью нейросети
    draw.rectangle([50, 50, 250, 250], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    return image