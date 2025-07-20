import telebot
import random
7816727246:AAGhYtaeuJ6FoNMmdmOQV8NoP-2t8GySzBc
TOKEN = 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 Dragon vs Tiger Prediction Bot Started!\n\nType: D | T | D or anything.")

@bot.message_handler(func=lambda m: True)
def predict(message):
    choice = random.choice(['🐲 Dragon', '🐯 Tiger'])
    amount = random.choice(['₹50', '₹100', '₹150', '₹200'])
    logic = random.choice(['Zig-Zag Pattern', 'Mirror Logic', 'Color Inversion', 'Pattern Reversal'])

    reply = f"""🎯 Prediction: {choice}
📊 Logic: {logic}
💸 Suggested Bet: {amount}
"""
    bot.reply_to(message, reply)

print("Bot Running...")
bot.polling()
