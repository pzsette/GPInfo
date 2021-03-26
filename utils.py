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