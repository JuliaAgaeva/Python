from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import*
import datetime

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name} ')
    
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f' {datetime.datetime.now().time()} ')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/help\n/sum\n/dif_float\n/mult_float\n/div_float\n/sum_complex\n/dif_complex\n/mult_complex\n/div_complex\n ')

# Далее идет тема алгоритмов
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
 #сообщение пользователя помещяем в отдельную переменную
    msg=update.message.text
    print(msg)
# разбираем текстовое сообщение
    items = msg.split() # / sum 123 5445
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} + {y}= {x+y} ')

async def dif_float_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg=update.message.text
    print(msg)
    items = msg.split() 
    x=float(items[1])
    y=float(items[2])
    await update.message.reply_text(f'{x}-{y}={x-y} ')

async def mult_float_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg=update.message.text
    print(msg)
    items = msg.split()
    x=float(items[1])
    y=float(items[2])
    await update.message.reply_text(f'{x}*{y}={x*y} ')

async def div_float_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg=update.message.text
    print(msg)
    items = msg.split() 
    x=float(items[1])
    y=float(items[2])
    await update.message.reply_text(f'{x}/{y}={x/y} ')

async def sum_complex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)

    msg=update.message.text
    print(msg)
    items = msg.split() 
    x=complex(items[1])
    y=complex(items[2])
    await update.message.reply_text(f'{x}+{y}={x+y} ')

async def dif_complex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg=update.message.text
    print(msg)
    items = msg.split()
    x=complex(items[1])
    y=complex(items[2])
    await update.message.reply_text(f'{x}-{y}={x-y} ')

async def mult_complex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg=update.message.text
    print(msg)
    items = msg.split() 
    x=complex(items[1])
    y=complex(items[2])
    await update.message.reply_text(f'{x}*{y}={x*y} ')

async def div_complex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg=update.message.text
    print(msg)
    items = msg.split() 
    x=complex(items[1])
    y=complex(items[2])
    await update.message.reply_text(f'{x}/{y}={x/y} ')