import asyncio
import json 
import pprint
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import spoonacular as sp


from aiogram import html # html matn formati
from aiogram import F # message filter

from config import BOT_TOKEN
from api import search_from_api

api = sp.API("668584543a0f48948d42408f93c840d7")

bot = Bot(token=BOT_TOKEN) # configdan bot tokeni olindi
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello! Enter your search food name:")

@dp.message(F.text)
async def search_music(message: types.Message):
    response = api.search_recipes_by_ingredients(message.text)
    data = response.json()
    print()
    if not response:
        await message.answer(html.bold("Not found !"), parse_mode="HTML")
    else: 
        for recipe in data:
            title = recipe['title']
            img = recipe["image"]
            await message.answer(html.bold(f"Title: {title} Img: {img}"), parse_mode="HTML")
            await message.content_type

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())