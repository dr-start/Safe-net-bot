from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = '7412729802:AAE1HeIZ0iwHKP2wj3A4a0nhh3pNO3LjjH4'
CHANNEL_USERNAME = '@SafeNet_V2ray'
YOUR_LINK = 'vless://b204cddf-d3df-4efa-95dc-aeafeedfaf66@a2.gozarino.com:2121/?type=tcp&encryption=none&flow=xtls-rprx-vision&sni=journalofbigdata.springeropen.com&fp=randomized&security=reality&pbk=YWfCdTnr4FAOMYTY2dLrMtQUokyxOGpPhYEEszPj20E&sid=#%F0%9F%87%A9%F0%9F%87%AA%20%D8%B3%D8%B1%D9%88%D8%B1%20%D8%A7%D8%B6%D8%B7%D8%B1%D8%A7%D8%B1%DB%8C%20%C2%B2'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("عضویت در کانال ✅", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")],
        [InlineKeyboardButton("بررسی عضویت ✅", callback_data="check_membership")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("سلام! برای دریافت لینک، لطفاً اول در کانال ما عضو شو:", reply_markup=reply_markup)

async def check_membership(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
    status = member.status

    if status in ['member', 'administrator', 'creator']:
        await query.answer()
        await query.edit_message_text("✅ عضویت تأیید شد! اینم لینکت:")
        await context.bot.send_message(chat_id=user_id, text=f"🌐 لینک: {YOUR_LINK}")
    else:
        await query.answer()
        await query.edit_message_text("❌ هنوز عضو کانال نیستی. لطفاً عضو شو و دوباره امتحان کن.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(check_membership, pattern="check_membership"))

app.run_polling()