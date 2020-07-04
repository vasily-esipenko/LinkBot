from aiogram import Bot, Dispatcher, executor, types
from constants import token, social_networks, urls

bot = Bot(token)
dp = Dispatcher(bot)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row("VK", "Instagram", "Twitter")


@dp.message_handler(commands=["start"])
async def start_answer(message: types.Message):
    await message.answer("Привет, это LinkBot! С моей помошью вы можете получить ссылки на профили в соцсетях.\n Введите юзернейм:")


@dp.message_handler(commands=["help"])
async def help_answer(message: types.Message):
    await message.answer("Возники вопросы? Пишите сюда: @Vasily_Esipenko")


@dp.message_handler(content_types=["text"])
async def text_answer(message: types.Message):
    global username
    if message.text not in social_networks:
        if " " not in message.text:
            username = message.text.lower()
            await message.answer("Отлично! Теперь выберите соцсеть:", reply_markup=markup)
        else:
            await message.answer("Что-то пошло не так... Попробуйте снова")
    elif message.text in urls:
        await message.answer(f"Вот ваша ссылка:\n{urls[message.text].format(username)}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
