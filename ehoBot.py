# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message
# from aiogram.filters import Command
# BOT_TOKEN = '6871019854:AAFJ-IWN1a-KdDyOb21tVcjUttAxbgOT2gE'
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()
#
#
# #реагирует на команду /start
# async def procces_start_command(message: Message):
#     await message.answer('привет!\nменя зовут Эхо бот\nнапиши что нибудь')
# # на /help
# async def procces_help_command(message: Message):
#     await message.answer('Отправь мне сообщение, и я отправлю тебе твое же сообщение')
#
# async def send_echo_photo(message: Message):
#     if message.photo:
#         await message.reply_photo(photo=message.photo[0].file_id, caption='ваша фотография')
#     else:
#         # Если в сообщении нет фотографии, отправляем сообщение об ошибке
#         await message.reply(text="Кажется, в вашем сообщении нет фотографии.")
#
# async def send_echo(message: Message):
#     if isinstance(message.text, str):
#         await message.reply(text=message.text)
#     # else:
#     #     await message.reply(text="Что-то пошло не так. Пожалуйста, отправьте текстовое сообщение.")
#
#
# #регистрируем хэндлеры
#
#
# dp.message.register(procces_start_command, Command('/start'))
# dp.message.register(procces_help_command, Command('/help'))
# dp.message.register(send_echo)
# dp.message.register(send_echo_photo, F.photo)
#
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     dp.run_polling(bot)
#
#
#
#
#
