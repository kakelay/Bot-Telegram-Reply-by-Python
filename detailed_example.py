"""
This is a detailed example using almost every command of the API
"""

import time

import telebot
from telebot import types

TOKEN = '6405796321:AAEiQ5S7jCshEZmmJ5WJ-ygOuunA8AKx57E'

knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'start'       : 'Get used to the bot',
    'help'        : 'Gives you information about the available commands',
    'sendLongText': 'A test using the \'send_chat_action\' command  ',
    'getImage'    : 'A test using multi-stage messages, custom keyboard, and media sending'
}

imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)  # create the image selection keyboard
imageSelect.add('Mickey', 'Minnie','Kakelay1','Kakelay2','Kakelay3','Kakelay4','Kakelay5','Kakelay6','Kakelay7','Kakelay8','Kakelay9','Kakelay10','Kakelay11','Kakelay12','Kakelay13','Kakelay14','Kakelay15','Kakelay16','Kakelay17','Kakelay18','Kakelay19','Kakelay20')

hideBoard = types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard


# error handling if user isn't known yet
# (obsolete once known users are saved to file, because all users
#   had to use the /start command and are therefore known to the bot)
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0


# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener


# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        bot.send_message(cid, "Hello, stranger, let me scan you...")
        bot.send_message(cid, "Scanning complete, I know you now")
        command_help(m)  # show the new user the help page
    else:
        bot.send_message(cid, "I already know you, no need for me to scan you again!")


# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "The following commands are available: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page


# chat_action example (not a good one...)
@bot.message_handler(commands=['sendLongText'])
def command_long_text(m):
    cid = m.chat.id
    bot.send_message(cid, "If you think so... ")
    bot.send_chat_action(cid, 'typing')  # show the bot "typing" (max. 5 secs)
    time.sleep(3)
    bot.send_message(cid,"Sure, if you ever have more questions or need assistance in the future, don't hesitate to ask. Happy coding, and have a great day!")


# user can chose an image (multi-stage command example)
@bot.message_handler(commands=['getImage'])
def command_image(m):
    cid = m.chat.id
    bot.send_message(cid, "Please choose your image now", reply_markup=imageSelect)  # show the keyboard
    userStep[cid] = 1  # set the user to the next step (expecting a reply in the listener now)


# if the user has issued the "/getImage" command, process the answer
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text

    # for some reason the 'upload_photo' status isn't quite working (doesn't show at all)
    bot.send_chat_action(cid, 'typing')

    if text == 'Mickey':  # send the appropriate image based on the reply to the "/getImage" command
        bot.send_photo(cid, open('rooster.jpg', 'rb'),
                       reply_markup=hideBoard)  # send file and hide keyboard, after image is sent
        userStep[cid] = 0  # reset the users step back to 0  
    elif text == 'Minnie':
        bot.send_photo(cid, open('kitten.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay1':  # Handle the new option
        bot.send_photo(cid, open('kakelay1.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay2':  # Handle the new option
        bot.send_photo(cid, open('kakelay2.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay3':  # Handle the new option
        bot.send_photo(cid, open('kakelay3.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay4':  # Handle the new option
        bot.send_photo(cid, open('kakelay4.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay5':  # Handle the new option
        bot.send_photo(cid, open('kakelay5.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay6':  # Handle the new option
        bot.send_photo(cid, open('kakelay6.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0 
    elif text == 'Kakelay7':  # Handle the new option
        bot.send_photo(cid, open('kakelay7.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay8':  # Handle the new option
        bot.send_photo(cid, open('kakelay8.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay9':  # Handle the new option
        bot.send_photo(cid, open('kakelay9.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay10':  # Handle the new option
        bot.send_photo(cid, open('kakelay10.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay11':  # Handle the new option
        bot.send_photo(cid, open('kakelay11.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay12':  # Handle the new option
        bot.send_photo(cid, open('kakela12.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay13':  # Handle the new option
        bot.send_photo(cid, open('kakelay13.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay14':  # Handle the new option
        bot.send_photo(cid, open('kakelay14.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay15':  # Handle the new option
        bot.send_photo(cid, open('kakelay15.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay16':  # Handle the new option
        bot.send_photo(cid, open('kakelay16.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay17':  # Handle the new option
        bot.send_photo(cid, open('kakelay17.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay18':  # Handle the new option
        bot.send_photo(cid, open('kakelay18.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay19':  # Handle the new option
        bot.send_photo(cid, open('kakelay19.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    elif text == 'Kakelay20':  # Handle the new option
        bot.send_photo(cid, open('kakelay20.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0


    else:
        bot.send_message(cid, "Please, use the predefined keyboard!")
        bot.send_message(cid, "Please try again")

# filter on a specific message
@bot.message_handler(func=lambda message: message.text.lower() == "hi"  )
def command_text_hi(m):
    bot.send_message(m.chat.id, "Hello!!! Can i help you?")
@bot.message_handler(func=lambda message: message.text.lower() == "love")
def command_text_hi(m):
    bot.send_message(m.chat.id, "I love you too!")

@bot.message_handler(func=lambda message: message.text.lower() == "nolove")
def command_text_hi(m):
    bot.send_message(m.chat.id, "I don't love you too!")


# default handler for every other text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    bot.send_message(m.chat.id, "I don't understand \"" + m.text + "\"\nMaybe try the help page at /help")


bot.infinity_polling()
