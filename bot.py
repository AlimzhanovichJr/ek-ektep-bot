import telebot

TOKEN = "8342901777:AAFV9xMIFrwBmIoBWrhVgMgJ4C5e_pk5KwA"
bot = telebot.TeleBot(TOKEN)

# Ескі вебхукты өшіру (409 қатесін болдырмау үшін)
try:
  bot.delete_webhook(drop_pending_updates=True)
except Exception:
  pass

# ӨЗІҢНІҢ Telegram ID-ің
ADMIN_CHAT_ID = 5338916652


@bot.message_handler(func=lambda message: True)
def handle_incoming_message(message):
  user_id = message.chat.id
  username = message.from_user.username or "Юзернеймі жоқ"
  first_name = message.from_user.first_name or "Аты жоқ"

  if user_id == ADMIN_CHAT_ID:
    try:
      parts = message.text.split(" ", 1)
      target_user_id = int(parts[0])
      reply_text = parts[1]
      bot.send_message(target_user_id, reply_text)
      bot.reply_to(message, "✅ Хабарлама жіберілді!")
    except Exception as e:
      bot.reply_to(
          message,
          f"❌ Қате! Дұрыс жазу форматы: `USER_ID Мәтін`\nҚате мәліметі: {e}",
          parse_mode="Markdown",
      )
  else:
    forward_text = (
        f"📩 **Жаңа хабарлама келді!**\n"
        f"👤 Кімнен: {first_name} (@{username})\n"
        f"🆔 ID: `{user_id}`\n\n"
        f"💬 Мәтін: {message.text}"
    )
    bot.send_message(ADMIN_CHAT_ID, forward_text, parse_mode="Markdown")


print("Бот іске қосылды, хабарламаларды күтіп тұр...")
bot.infinity_polling(skip_pending=True)

калай 24/7 токтамай жасайтын кыламын
