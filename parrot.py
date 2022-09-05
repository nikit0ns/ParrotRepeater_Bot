from distutils.command.config import config
from logging import disable
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config

bot = Bot(token=config.TOKEN) #Ваш токен
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_answer(message: types.Message):
    await message.answer("👋 <b>Привіт,</b> @" + message.from_user.username + "<b>.</b>\n✏️ <b>Просто напиши щось.</b> \n🦜 <b>Я буду повторювати за тобою.</b>", parse_mode="HTML")
    


@dp.message_handler(commands=['help'])
async def cmd_answer(message: types.Message):
    await message.answer("⁉️<b> Якщо у вас є проблеми.</b> \n✉️ <b>Напишіть мені</b> <a href='https://t.me/nikit0ns'>@nikitons</a><b>.</b>", disable_web_page_preview=True, parse_mode="HTML")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(chat_id=msg.from_user.id, text=f"<b>{msg.text}</b>", parse_mode="HTML")


if __name__ == '__main__':
    executor.start_polling(dp)