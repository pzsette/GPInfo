import csv
from datetime import datetime
import utils


def calendar_f1(update, context):
    with open('timetable_f1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        calendar = ''
        for gp in csv_reader:
            calendar += gp[0]+' - '+gp[1]+'\n'
        print(calendar)
        update.message.reply_text(calendar)


def next_f1_gp(update, context):
    now = datetime.now()
    with open('timetable_f1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for gp in csv_reader:
            race_datetime = utils.build_race_datetime_with_delay(gp)
            if now < race_datetime:
                print(utils.format_f1(gp))
                update.message.reply_text(utils.format_f1(gp))
                break
