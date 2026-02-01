import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "BOT_TOKEN_СЮДА"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

drivers = set()

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🚕 Вызвать такси")
    kb.add("🚖 Стать водителем")
    await msg.answer("🚖 Добро пожаловать в Taxi Bot!", reply_markup=kb)

@dp.message_handler(text="🚖 Стать водителем")
async def driver(msg: types.Message):
    drivers.add(msg.from_user.id)
    await msg.answer("✅ Вы добавлены как водитель")

@dp.message_handler(text="🚕 Вызвать такси")
async def order(msg: types.Message):
    if not drivers:
        await msg.answer("❌ Сейчас нет водителей")
        return
    for d in drivers:
        await bot.send_message(d, "📥 Новый заказ!")
    await msg.answer("🔍 Поиск водителя...")

if __name__ == "__main__":
    executor.start_polling(dp)
