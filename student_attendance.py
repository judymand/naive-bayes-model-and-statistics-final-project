import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np


def get_data():
    df = pd.read_csv("infoperstudents.csv")
    number = LabelEncoder()

    df['day'] = number.fit_transform(df['day'])

    className = {'ח1': 0, 'ח2': 1, 'ח3': 2}
    name = {'אביחי ממן': 0, 'אגם בוחבוט': 1, 'אמבר הרד': 2, 'אנג׳לינה ג׳ולי': 3, 'ביבי נתניהו': 4,
            'בר רפאלי': 5, 'בראד פיט': 6, 'ברק אובמה': 7, 'גיא דהן': 8, 'ג׳ו ביידן': 9, 'ג׳וני דפ': 10,
            'ג׳ייסון סטטהם': 11, 'ג׳סטין ביבר': 12, 'דודו אהרון': 13, 'דודי ביטון': 14, 'דונלד טראמפ': 15,
            'דניאל אסייג': 16, 'טל חדד': 17, 'יאיר לפיד': 18, 'יהודית מנדלבוים': 19, 'יעל בר זוהר': 20,
            'ליאור אוחנה': 21, 'מנדל שמעון עמר': 22, 'נועה קירל': 23, 'נופר צדפיה': 24, 'סיטארה אלייב': 25,
            'עדן דדון': 26, 'עדן מוזס': 27, 'עינב בן חמו': 28, 'שקד בן חמו': 29}
    profession = {'אנגלית': 0, 'גיאוגרפיה': 1, 'היסטוריה': 2, 'חשבון': 3, 'לשון': 4, 'ספרות': 5, 'ערבית': 6, 'פיזיקה': 7,
                  'תנ"ך': 8}
    status = {'evasion': 0, 'home': 1, 'present': 2}
    teacher = {'אושרי גנאח': 0, 'אלון טמנו': 1, 'אלעד דהן': 2, 'גליה מוריוסף': 3, 'חיים כהן': 4,
               'ליאור סבוני': 5, 'סמדר שולמן': 6, 'עוז שלום': 7, 'שלי מיכאלאשוילי': 8, }
    days = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2,
            'Wednesday': 3, 'Thursday': 4}
    hour = {'08': 0, '09': 0, '10': 1, '11': 1, '12': 2, '13': 2}

    df = df.replace({'className': className})
    df = df.replace({'name': name})
    df = df.replace({'profession': profession})
    df = df.replace({'status': status})
    df = df.replace({'teacher': teacher})
    df = df.replace({'wday': days})
    df['time'] = df['time'].str.slice(stop=2)
    df = df.replace({'time': hour})

    target = df['status']
    data = df.drop(columns=['status', '_id', '__v'])

    return data, target
