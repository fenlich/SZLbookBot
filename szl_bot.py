import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    filters, 
    MessageHandler,
    PicklePersistence,
    ApplicationBuilder,
    CommandHandler, 
    ContextTypes, 
    CallbackQueryHandler,
    ConversationHandler,
    )
import pandas as pd
from random import choice
from config import TOKEN
import requests
from io import BytesIO
from PIL import Image

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

booklist = pd.read_csv('books.csv')
def get_book(genre):
    book = booklist.loc[booklist['genre'] == genre, ['author','title', 'description', 'year', 'country', 'cover']]
    book = book.to_dict('records')
    rndm = choice(book)
    return (rndm['author'] + '\n' + rndm['title'] + '\n' + str(rndm['year']) + '\n' + rndm['country'] + '\n' + rndm['description'] + '\n' + str(rndm['cover']))

def get_image(image_url):
    r = requests.get(image_url)
    if r.status_code == 200:
        return BytesIO(r.content)
    return None


#Stages
START, MENU = range(2)
#Stage defs for genres
FANTASY, ROMANCE, FIC, DETECTIVE, COMEDY, HISTORY, THRILLER, MAGREAL, PSYCHOLOGY, PHILOSOPHY, ADVENTURES, RAISING, DYSTOPIA = range(2, 15)

END = ConversationHandler.END

def again():
    global reply_markup
    keyboard = [
        [
            InlineKeyboardButton("Заново", callback_data=str(MENU)),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)



#здесь добавляются функции (команды)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Send a message when the command /start is issued."""
    keyboard = [
        [InlineKeyboardButton("Подобрать книгу", callback_data=str(MENU))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Привет, нечего читать? Жми на кнопку!", reply_markup=reply_markup)
    return START

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Sends a message with inline buttons attached."""
    
    keyboard = [
        [
            InlineKeyboardButton("Фэнтези", callback_data=str(FANTASY)),
            InlineKeyboardButton("Любовный роман", callback_data=str(ROMANCE)),
            InlineKeyboardButton("Фантастика", callback_data=str(FIC))
        ],
        [
            InlineKeyboardButton("Детектив", callback_data=str(DETECTIVE)),
            InlineKeyboardButton("Триллер", callback_data=str(THRILLER)),
            InlineKeyboardButton("Психология", callback_data=str(PSYCHOLOGY))
        ],
        [
            InlineKeyboardButton("Приключения", callback_data=str(ADVENTURES)),
            InlineKeyboardButton("Антиутопия", callback_data=str(DYSTOPIA)),
            InlineKeyboardButton("Философия", callback_data=str(PHILOSOPHY))
        ],
        [
            InlineKeyboardButton("Магический реализм", callback_data=str(MAGREAL)),
            InlineKeyboardButton("Роман воспитания", callback_data=str(RAISING))
        ],
        [
            InlineKeyboardButton("Комедия", callback_data=str(COMEDY)),
            InlineKeyboardButton("Исторический роман", callback_data=str(HISTORY))
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query = update.callback_query
    await query.answer()
    await context.bot.send_message(update.effective_chat.id, text="Пожалуйста, выбери жанр :)", reply_markup=reply_markup)
    return MENU



async def fantasy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('фэнтези').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

async def romance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('любовный роман').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

async def fiction(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('фантастика').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

async def detective(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('детектив').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

async def comedy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('комедия').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

async def history(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('история').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

async def thriller(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('триллер').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

async def magreal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('магический реализм').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

async def psychology(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('психология').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

async def phylosophy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('философия').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

async def adventures(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('приключения').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

async def raising(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('роман воспитания').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

async def dystopia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    again()

    query = update.callback_query
    await query.answer()
    book = get_book('антиутопия').split("\n")
    image_url = book[-1]
    print(image_url)
    image = get_image(image_url)
    await context.bot.send_photo(update.effective_chat.id, image, caption="\n".join(book[:-1]), reply_markup=reply_markup)
    return MENU

#здесь функции реализуются
if __name__ == '__main__':
    persistence = PicklePersistence(filepath="szl_bot")
    application = ApplicationBuilder().token(TOKEN).persistence(persistence).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START: [CallbackQueryHandler(menu, pattern="^" + str(MENU) + "$"),],
            MENU: [
                CallbackQueryHandler(fantasy, pattern="^" + str(FANTASY) + "$"),
                CallbackQueryHandler(romance, pattern="^" + str(ROMANCE) + "$"),
                CallbackQueryHandler(fiction, pattern="^" + str(FIC) + "$"),
                CallbackQueryHandler(detective, pattern="^" + str(DETECTIVE) + "$"),
                CallbackQueryHandler(comedy, pattern="^" + str(COMEDY) + "$"),
                CallbackQueryHandler(history, pattern="^" + str(HISTORY) + "$"),
                CallbackQueryHandler(thriller, pattern="^" + str(THRILLER) + "$"),
                CallbackQueryHandler(magreal, pattern="^" + str(MAGREAL) + "$"),
                CallbackQueryHandler(psychology, pattern="^" + str(PSYCHOLOGY) + "$"),
                CallbackQueryHandler(phylosophy, pattern="^" + str(PHILOSOPHY) + "$"),
                CallbackQueryHandler(adventures, pattern="^" + str(ADVENTURES) + "$"),
                CallbackQueryHandler(raising, pattern="^" + str(RAISING) + "$"),
                CallbackQueryHandler(dystopia, pattern="^" + str(DYSTOPIA) + "$"),
                CallbackQueryHandler(menu, pattern="^" + str(MENU) + "$"),
                ],
        },
        fallbacks=[CommandHandler("start", start)],
        name='my_szlbot',
        persistent=True,
    )

   
    application.add_handler(conv_handler)
  

    application.run_polling()
    
