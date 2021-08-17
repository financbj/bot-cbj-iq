from telegram.ext import Updater, CommandHandler

def welcome(update, context):
    firstName = update.message.from_user.first_name
    message = 'Olá, ' + firstName + '!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    token = '1989338038:AAEbA22He8x7PjElXKs2uuXq56wf7ifwfWM'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    updater.start_polling()
    print("Olá, eu sou o " + str(updater))
    updater.idle()

if __name__ == "__main__":
    main()
