import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram.types import CallbackQuery
from google_trans_new import google_translator
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

TOKEN = os.environ.get("TOKEN", "")

APP_ID = int(os.environ.get("APP_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

Deccan = Client(
        "ggt",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=APP_ID
    )
    
START_TEXT = """
Hello {}, 
I am <b>Google Translator Bot.</b>

Send me a <b>word/sentence.</b> I will Translate it to you ✅

Click /help for more details..

<b>▷ Made With ❤ By @ZauteKm.</b>
"""
HELP_TEXT = """
Hey, 
It's not complicated 🤭

<b><u>Follow these Steps.</u></b>
▷ Just send me a Word/Sentence/Paragraph.
▷ Select the Language and I will translate it you!

<b><u>Languages :-</u></b>
English, Tamil, Telugu, Hindi, Kannada, Malayalam, Urdu, Punjabi, Spanish, Korean, Japanese, Chinese, Greek, Italian, Vietnamese, Nepali
 
<b>▷ Made With ❤ By @ZauteKm.</b>
"""
ABOUT_TEXT = """
⭕️<b>🤖 My Name : Google Translator Bot</b>

⭕️<b>📝 Language :</b> <code>Python3</code>

⭕️<b>📚 Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a>

⭕️<b>📡 Hosted on :</b> <a href='https://heroku.com/'>Heroku</a>

⭕️<b>👥 Support Group :</b> <a href='https://t.me/joinchat/qvArnd0aDlkzNjM1'>Luishai Help DesK</a>

⭕️<b>📢 Updates Channel :</b> <a href='https://t.me/LushaiTech'>LushaiTech</a>
"""

DONATE_TEXT = """<b>Thanks for Clicking Donate Command.</b>

The bot is free to use and always will be!
But running this bot on server costs money, If you like this bot and want it to keep running, please support.

To donate you can choose any of these options and send any amount that you wish.

<b>▷ Made With ❤ By @ZauteKm.</b>
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👥 Group', url='https://t.me/joinchat/qvArnd0aDlkzNjM1'),
        InlineKeyboardButton(' Channel 📢', url='https://telegram.me/LushaiTech')
        ],[
        InlineKeyboardButton('🗣 Feedback', url='https://telegram.me/ZauteBot'),
        InlineKeyboardButton('Bot Lists 🤖', url='https://t.me/TG_BotList/37'),
        InlineKeyboardButton('Music 👨‍🎤', url='https://t.me/joinchat/7gSUxv6vgQE3M2Fl')
        ],[
        InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://youtube.com/c/ZauteKm')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👥 Group', url='https://t.me/joinchat/qvArnd0aDlkzNjM1'),
        InlineKeyboardButton(' Channel 📢', url='https://telegram.me/LushaiTech')
        ],[
        InlineKeyboardButton('🗣 Feedback', url='https://telegram.me/ZauteBot'),
        InlineKeyboardButton('Bot Lists 🤖', url='https://t.me/TG_BotList/37'),
        InlineKeyboardButton('Music 👨‍🎤', url='https://t.me/joinchat/7gSUxv6vgQE3M2Fl')
        ],[
        InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://youtube.com/c/ZauteKm')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👥 Group', url='https://t.me/joinchat/qvArnd0aDlkzNjM1'),
        InlineKeyboardButton(' Channel 📢', url='https://telegram.me/LushaiTech')
        ],[
        InlineKeyboardButton('🗣 Feedback', url='https://telegram.me/ZauteBot'),
        InlineKeyboardButton('Bot Lists 🤖', url='https://t.me/TG_BotList/37'),
        InlineKeyboardButton('Music 👨‍🎤', url='https://t.me/joinchat/7gSUxv6vgQE3M2Fl')
        ],[
        InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://youtube.com/c/ZauteKm')
        ]]
    )
DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('💸 PayPal', url='https://t.me/Zautebot'),
        InlineKeyboardButton('UPI 🤑', url='https://t.me/zautebot')
        ],[
        InlineKeyboardButton('👥 Group', url='https://t.me/joinchat/qvArnd0aDlkzNjM1'),
        InlineKeyboardButton(' Channel 📢', url='https://telegram.me/LushaiTech')
        ],[
        InlineKeyboardButton('🗣 Feedback', url='https://telegram.me/ZauteBot'),
        InlineKeyboardButton('Bot Lists 🤖', url='https://t.me/TG_BotList/37'),
        InlineKeyboardButton('Music 👨‍🎤', url='https://t.me/joinchat/7gSUxv6vgQE3M2Fl')
        ],[
        InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://youtube.com/c/ZauteKm')
        ]]
    )

@Deccan.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["donate"]))
async def donate(bot, update):
    await update.reply_text(
        text=DONATE_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=DONATE_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )
	
@Deccan.on_message(filters.text & filters.private )
def echo(client, message):
 
 keybord = InlineKeyboardMarkup( [
        [
            InlineKeyboardButton("English", callback_data='en'),
            InlineKeyboardButton("Tamil", callback_data='ta'),
            InlineKeyboardButton("Telugu",callback_data='te')
        ],
        [   InlineKeyboardButton("Hindi", callback_data='hi'),
        InlineKeyboardButton("Kannada", callback_data='kn'),
        InlineKeyboardButton("Malayalam",callback_data= 'ml')
        ],
        [InlineKeyboardButton("Urdu", callback_data ='ur'),
	InlineKeyboardButton("Punjabi", callback_data='pa'),
	InlineKeyboardButton("Spanish", callback_data='es')
	],
        [InlineKeyboardButton("Korean", callback_data='ko'),
         InlineKeyboardButton("Japanese", callback_data='ja'),
         InlineKeyboardButton("Chinese", callback_data='zn-cn')
        ],
        [InlineKeyboardButton("Greek", callback_data='el'),
         InlineKeyboardButton("Italian", callback_data='it'),
         InlineKeyboardButton("Nepali", callback_data='ne')
        ]
    ]
 
 )

 
 message.reply_text("Select language 👇",reply_to_message_id = message.message_id, reply_markup = keybord)
    
    
@Deccan.on_callback_query()
async def translate_text(bot,update):
  tr_text = update.message.reply_to_message.text
  cbdata = update.data
  translator = google_translator()
  translated_text = translator.translate(tr_text,lang_tgt=cbdata)
  await update.message.edit(translated_text)
  	

Deccan.run()
