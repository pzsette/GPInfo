from secrets import telegram_token
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from f1_commands import next_f1_gp, calendar_f1
from motogp_commands import next_motogp_gp, calendar_motogp

TOKEN = telegram_token


def help(update, context):
    help_msg = '/calf1 -> Calendario F1\n'\
               +'/calmotogp -> Calendario MotoGP\n'\
               +'/nextf1 -> Orari prossimo gp F1\n'\
               +'/nextmotogp -> Orari prossimo gp MotoGP'
    update.message.reply_text(help_msg)


if __name__ == '__main__':
    upd = Updater(TOKEN, use_context=True)
    disp = upd.dispatcher

    disp.add_handler(CommandHandler("nextf1", next_f1_gp))
    disp.add_handler(CommandHandler("nextmotogp", next_motogp_gp))
    disp.add_handler(CommandHandler("calf1", calendar_f1))
    disp.add_handler(CommandHandler("calmotogp", calendar_motogp))
    disp.add_handler(CommandHandler("help", help))


    upd.start_polling()
    upd.idle()
