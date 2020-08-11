import datetime
import pytz
a=datetime.date.today()
print(type(a))
print(a)
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.time)
s=(datetime.date.today()-datetime.date(1998,10,30)).days

print(s)
print(datetime.datetime.today().weekday())
print(datetime.datetime.today().day)
print(datetime.datetime.today().month)
print(datetime.datetime.today().year)
print(datetime.datetime.today().minute)
print(datetime.datetime.today().hour)
print(datetime.datetime.today().fold)
print(datetime.datetime.today().microsecond)
print(datetime.datetime.today().second)
print(datetime.datetime.today().tzinfo)
print(datetime.datetime.today().__class__)

a=datetime.timedelta(days=10)
b=datetime.timedelta(minutes=90)
c=datetime.timedelta(hours=30)
d=datetime.timedelta()

print(datetime.date.today().strftime('%d %B,%Y'))

for tz in pytz.all_timezones:
    print(tz)
