import csv
import datetime
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
    month = datetime.date.today().month
    day = datetime.date.today().day
    with open('timetable_f1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for gp in csv_reader:
            gp_date = gp[0]
            if month <= utils.convert_moth_to_num(gp_date[3:]) and day <= int(gp_date[:2]):
                print(utils.format_f1(gp))
                update.message.reply_text(utils.format_f1(gp))
                break
