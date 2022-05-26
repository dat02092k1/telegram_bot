from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup

def get_news():
    list_news = []
    r_data = requests.get("https://vnexpress.net/")
    soup = BeautifulSoup(r_data.text, "html.parser")
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

    return list_news

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Xin chao {update.effective_user.first_name}')

def news(update: Update, context: CallbackContext) -> None:
    data = get_news()
    for news_item in data:
        update.message.reply_text(f'{news_item["link"]}')

updater = Updater('5279853007:AAHANgfhZCEz49dxtFU_FXOxRkOAJ1n6A48')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('news', news))
updater.start_polling()
updater.idle()