from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from botOpenAI import createSystemChat
from service import howToUseThisBot, showAvaliableChar
from genshin import getGenshinInfo
from config import TOKEN_TELE, USERNAME_TELE

# Commands
user_state = {}

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'''🎃✨ Selamat datang di Bot Review Karakter! ✨🎃

Hoo~! Hoo~! Aku Hu Tao, sementara menjadi admin bot ini! 🔥💀 Jangan takut~ aku di sini bukan buat urus pemakaman karakter kalian (kecuali kalau mereka low HP terus nggak pake healer... 😏).

Mau tahu karakter kamu udah bagus atau belum ? Atau sekadar curhat ? Aku siap bantu~!''')
    
    caption = howToUseThisBot()
    with open("TampilkanRincian.png", "rb") as photo:
        await update.message.reply_photo(photo=photo, caption=caption)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """ Perlu bantuan apa ?
- /review - command untuk memberi tahu list 

untuk chat bisa langsung mengirim pesan.

jika ingin memberi saran terkait bot ini silahkan chat pemilik bot 

@Syahrul Ulum

"""
    await update.message.reply_text(message)
    await update.message.reply_text("Untuk saat ini karakter yang dapat direview adalah HuTao")

async def review_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    caption = howToUseThisBot()
    with open("TampilkanRincian.png", "rb") as photo:
        await update.message.reply_photo(photo=photo, caption=caption)

async def uid_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args: 
        uid = context.args[0]  
        genshinInfo = await getGenshinInfo(uid)
        if isinstance(genshinInfo, str):
            return genshinInfo
        
        user_id = update.message.from_user.id
        user_state[user_id] = genshinInfo

        char = showAvaliableChar(genshinInfo.characters)
        if char:
            await update.message.reply_text(char)
        else:
            await update.message.reply_text("Tidak ada karakter yang bisa lihat, silahkan ubah settingan akun terlebih dahulu")
    else:
        await update.message.reply_text("UID tidak ditemukan. \nMasukkan UID dengan format: /uid <YourUID>")

async def char_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if user_state.get(user_id) and user_state.get('genshinInfo'): 
        char = showAvaliableChar(user_state['genshinInfo'])
        if char:
            await update.message.reply_text(char)
        else:
            await update.message.reply_text("Tidak ada karakter yang bisa lihat, silahkan ubah settingan akun terlebih dahulu")
    else:
        await update.message.reply_text("Masukkan UID terlebih dahulu dengan format: /uid <YourUID>")

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = update.message.text.split()[0]
    await update.message.reply_text(f"{command} belum tersedia. \nKetik /help jika membutuhkan bantuan")

# Response
def handle_response(text: str) -> str:
    
    return createSystemChat(text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type # group atau private
    text: str = update.message.text # Text yang diketik

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group': # Membuat kondisi dimana bot bisa berfungsi jika di @ di group
        if USERNAME_TELE in text:
            new_text: str = text.replace(USERNAME_TELE, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} couse error')

if __name__ == '__main__':
    print('Bot Start....')
    app = Application.builder().token(TOKEN_TELE).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('uid', uid_command))
    app.add_handler(CommandHandler('review', review_command))
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    # Message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
