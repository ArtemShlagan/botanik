import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '7948359394:AAGTjMM5lzF71spdWdGiW6WSNsbMeVl9BFo'  # Замените на ваш токен

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    greeting_text = (
        "Привет, я онлайн-помощник Ботаник. Я собрал все актуальные курсы для удаленной работы.\n"
        "Курсы все актуальны, информация в них тоже актуальная. После прохождения курса - "
        "Ты будешь обладать базовыми способностями, которые дальше сможешь применять и улучшать самостоятельно. "
        "В конце каждого курса будет интересный канал на конкретную тематику.\n\n"
        "Всё это - абсолютно БЕСПЛАТНО! \n"
        "Подписывайся!\n"
        "Учись!\n"
        "Зарабатывай!"
    )
    await message.answer(greeting_text)
    
    courses_text = (
        "Вот список всех курсов:\n"
        "1. [Арбитраж Трафика](https://t.me/+4G1vsRfmJnA0MTAy)\n"
        "2. [SMM](https://t.me/+qwUmG0TtfIk4OTU6)\n"
        "3. [SEO](https://t.me/+36ucmKGt8ao5ZGFi)\n"
        "4. [Копирайтинг](https://t.me/+2l2YeUzz3rIwNjVi)\n"
        "5. [Аналитика Данных](https://t.me/+tfDg4t_2ACpmNjQy)\n"
        "6. [Дропшиппинг](https://t.me/+wNZwBLf45pQ1ZTVi)\n"
        "7. [Продажи и Маркетинг](https://t.me/+DLozqHh60lswNWFi)\n"
        "8. [3D-Моделирование](https://t.me/+UbzLut55SsVhZjcy)\n"
        "9. [Видеомонтаж](https://t.me/+e1TJOEqcEQg1MTYy)\n"
        "10. [Программирование](https://t.me/+YjjGMi7AepM4YTZi)\n"
        "11. [Adobe Photoshop](https://t.me/+spqMkCxmvTIxOTU6)\n"
        "12. [Дизайн и Графика](https://t.me/+_-oI3xgFqYYyMjU6)"
    )
    await message.answer(courses_text, parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
