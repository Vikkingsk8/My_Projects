from aiogram import types, executor, Dispatcher, Bot
from os import getenv
from sys import exit
import logging
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

bot_token = getenv('TOKEN')
if not bot_token:
    exit('ERROR Token is not found')

bot = Bot(bot_token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def starting(message: types.Message):
    await bot.send_message(message.chat.id, 'Здравствуйте Сэр')


@dp.message_handler(content_types='text')
async def search(message: types.Message):
    url = "https://ru.wikipedia.org/w/index.php?go=Перейти&search=" + message.text
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    links = soup.find_all('div', class_='mw-search-result-heading')

    if len(links) > 0:
        url = 'https://ru.wikipedia.org' + links[0].find('a')['href']

    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    driver = webdriver.Chrome(chrome_options=option)
    driver.get(url)

    driver.execute_script('window.scroll(0,200)')
    driver.save_screenshot('img.png')
    driver.close()

    photo = open('img.png', 'rb')
    await bot.send_photo(message.chat.id, photo=photo,
                         caption=f'Вот ссылка:<a href="{url}">жми сюда</a>', parse_mode='HTML')


executor.start_polling(dp)
