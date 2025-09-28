# import smtplib
#
# my_email = "###"
# password = "###"
#
# # smtp.mail.yahoo.com
# # connection = smtplib.SMTP("outlook.office365.com", port=465)
# # connection.starttls()
# # connection.login(user=my_email, password=password)
# # connection.sendmail(from_addr=my_email, to_addrs="###", msg="Hello")
# # connection.close()
#
# with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#     from_addr=my_email,
#     to_addrs='###',
#     msg='Subject:Hello\n\nThis is the body of my email.'
# )

import datetime as dt
import pandas as pd
import random
# now = dt.datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)
# print(now.weekday())

quotes = pd.read_csv("quotes.txt")
quotes_data = pd.DataFrame(quotes)
list_quotes = quotes_data.values


day_of_week = dt.datetime.now().weekday()
if day_of_week == 0:
    print("he")
else:
    print(random.choice(list_quotes)[0])