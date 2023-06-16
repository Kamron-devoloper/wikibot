import logging
from aiogram import Bot, Dispatcher, executor, types
from checkWiki import check_wiki

TOKEN_API = "6037990470:AAHS1L-kkJ_w7mAqYCgzr1Nfy37BOBDHoNw"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def send_star(msg: types.Massage):
    await msg.reply('bu bot kamronbek tomonidan yaratilgan bu bot wikipediya botidir!!')


@dp.message_handler(commands=['help'])
async def send_help(msg: types.Message):
    await msg.reply('malumotlarga ega bolmoqci bolsangiz qidirayotgan sorovingizni yuboring!!')
 

@dp.message_handler()
async def send_help(msg: types.Message):
    data = check_wiki(msg.text)
    if data['data']:
        await msg.answer(data['summary'])
    elif data['word']:
        answer = ' '
        for i in data['search']:
            answer = answer + i
        await msg.answer(f"siz qidirgan malumot shular emasmi???  {answer}")
    else:
        await msg.reply('siz qidirgan malumot bazadan topilmadi')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
