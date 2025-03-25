import telebot
from deep_translator import GoogleTranslator

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
BOT_TOKEN = "7680215700:AAE6qyXq6GLHJhNblRrefA53nHAZ2H3v3KQ"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome! Use `/translate` like this:\n\n"
                          "1️⃣ `/translate es Hello, how are you?`\n"
                          "2️⃣ Reply to a message with `/translate es`", parse_mode="Markdown")

@bot.message_handler(commands=['translate'])
def translate_command(message):
    try:
        if message.reply_to_message and len(message.text.split()) == 2:
            lang_code = message.text.split()[1]
            text = message.reply_to_message.text
        else:
            parts = message.text.split(" ", 2)
            if len(parts) < 3:
                bot.reply_to(message, "Usage:\n"
                                      "`/translate <lang_code> <text>`\n"
                                      "or reply to a message with `/translate <lang_code>`", parse_mode="Markdown")
                return
            lang_code, text = parts[1], parts[2]

        # Translate the text
        translated_text = GoogleTranslator(source='auto', target=lang_code).translate(text)

        # Send translation result
        bot.reply_to(message, f"**Translation ({lang_code}):**\n{translated_text}", parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

# Start the bot
print("Bot is running...")
bot.infinity_polling()