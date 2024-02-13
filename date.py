import datetime


# 1
def five():
    today = datetime.date.today()
    return today - datetime.timedelta(days=5)


# 2
def yest_today_tomorrow():
    today = datetime.date.today()
    return {'yesterday': today - datetime.timedelta(days=1),
            'today': today,
            'tomorrow': today + datetime.timedelta(days=1)}


# 3
def microsec():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')


# 4
def difference(date1, date2):
    return (date2 - date1).total_seconds()


