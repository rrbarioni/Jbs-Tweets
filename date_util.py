from datetime import date
from dateutil.relativedelta import *

def month_after(date_s):
	year =  int(date_s[:4])
	month = int(date_s[5:7])
	day =   int(date_s[8:10])
	day_after = date(year, month, day) + relativedelta(months=+1)

	year_s = str(day_after.year)
	month_s = str(day_after.month)
	if (day_after.month < 10):
		month_s = "0" + month_s
	day_s = str(day_after.day)
	if (day_after.day < 10):
		day_s = "0" + day_s

	return year_s + "-" + month_s + "-" + day_s

def day_after(date_s):
	year =  int(date_s[:4])
	month = int(date_s[5:7])
	day =   int(date_s[8:10])
	day_after = date(year, month, day) + relativedelta(days=+1)

	year_s = str(day_after.year)
	month_s = str(day_after.month)
	if (day_after.month < 10):
		month_s = "0" + month_s
	day_s = str(day_after.day)
	if (day_after.day < 10):
		day_s = "0" + day_s

	return year_s + "-" + month_s + "-" + day_s
