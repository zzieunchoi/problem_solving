import datetime
a = datetime.date(2021,11,5).strftime("%Y-%m-%d")

b = datetime.datetime.strptime(a, "%Y-%m-%d")
print(type(b))