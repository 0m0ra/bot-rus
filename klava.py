from aiogram import  Bot , executor , types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



from config import TOKEN_API 

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb =  ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/help')).insert(KeyboardButton('/description')).add(KeyboardButton(""))


HELLP_COMMAND =""" 
<b>/help </b> - <em>список команд</em>
<b>/start </b> - <em>старт бота</em>
<b>/description - </b> - <em>описание бота</em>"""

async def on_startup(_):
    print('я запустился!')


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, text= HELLP_COMMAND, parse_mode="HTML", reply_markup=kb)
    await message.delete()
    
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, text= "Добро пожаловать к нам !", parse_mode="HTML", reply_markup=kb) 
    await message.delete()
    
    
@dp.message_handler(commands=["description"])
async def desc_command(message: types.Message):
    await bot.send_message(message.from_user.id, text= "????", parse_mode="HTML", reply_markup=kb) 
    await message.delete()

    
if __name__== "__main__":
   executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
