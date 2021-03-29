from datetime import datetime, timedelta


def convert_moth_to_num(month):
    return {
        'Gennaio': 1,
        'Febbraio': 2,
        'Marzo': 3,
        'Aprile': 4,
        'Maggio': 5,
        'Giugno': 6,
        'Luglio': 7,
        'Agosto': 8,
        'Settembre': 9,
        'Ottobre': 10,
        'Novembre': 11,
        'Dicembre': 12,
    }[month]


def format_f1(gp):
    return gp[0]+'\n'\
           +gp[1]+'\n'\
           +'FP1: '+gp[2]+'\n'\
           +'FP2: '+gp[3]+'\n'\
           +'FP3: '+gp[4]+'\n'\
           +'QUALIFICHE: '+gp[5]+'\n'\
           +'GARA: '+gp[6]


def format_motogp(gp):
    return gp[0]+'\n'\
           +gp[1]+'\n'\
           +'FP1: '+gp[2]+'\n'\
           +'FP2: '+gp[3]+'\n'\
           +'FP3: '+gp[4]+'\n'\
           +'FP4: '+gp[5]+'\n'\
           +'QUALIFICHE: '+gp[6]+'\n'\
           +'GARA: '+gp[7]


def build_race_datetime_with_delay(gp):
    race_date_from_csv = gp[0]
    race_time_from_csv = gp[-1]
    race_month = convert_moth_to_num(race_date_from_csv[3:])
    race_date = int(race_date_from_csv[:2])
    race_hour = int(race_time_from_csv[:2])
    race_minute = int(race_time_from_csv[3:])
    return datetime(2021, race_month, race_date, race_hour, race_minute) + timedelta(hours=4)