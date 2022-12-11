from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *



app = ApplicationBuilder().token("5863041847:AAGqxOcna1arB0o2duKC6EwcdPbEZrbSalk").build()

# Команды прописываются какие бот будет выполнять
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("dif_float", dif_float_command))
app.add_handler(CommandHandler("mult_float", mult_float_command))
app.add_handler(CommandHandler("div_float", div_float_command))
app.add_handler(CommandHandler("sum_complex", sum_complex_command))
app.add_handler(CommandHandler("dif_complex", dif_complex_command))
app.add_handler(CommandHandler("mult_complex", mult_complex_command))
app.add_handler(CommandHandler("div_complex", div_complex_command))



print ('server start')
app.run_polling()
