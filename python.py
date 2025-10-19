from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os
import requests

TOKEN = os.getenv("8239022435:AAFVd9YYT9DcwdbKVlvF70VJ-nDjbLqGHfY")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Salom! Bot ishlayapti. Videoni yuklab olish uchun Instagram yoki boshqa ijtimoiy tarmoqlardan link yuboring (faqat o'zingizga tegishli kontent).")

@dp.message_handler()
async def handle_link(message: types.Message):
    url = message.text.strip()
    # Bu yerda API qo'shasiz: masalan, YOUR_DOWNLOAD_API_ENDPOINT ga POST yoki GET so'rov yuborasiz
    # E'tibor: qonuniy kontent bilan ishlang va mualliflik huquqini hurmat qiling.
    if "instagram.com" in url or "tiktok.com" in url or "youtube.com" in url:
        await message.reply("Link qabul qilindi. Videoni yuklab olish uchun API bilan ishlayman (placeholder).")
        # Misol uchun (bu faqat namuna, real API token va endpoint kerak bo'ladi):
        # api_resp = requests.get("https://example.com/api/download", params={"url": url})
        # if api_resp.status_code == 200:
        #     file_url = api_resp.json().get("file_url")
        #     await bot.send_video(message.chat.id, file_url)
        # else:
        #     await message.reply("Videoni olishda xatolik bo'ldi.")
    else:
        await message.reply("Iltimos, to'g'ri ijtimoiy tarmoq linkini yuboring (instagram/tiktok/youtube).")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
