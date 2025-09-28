STOCK = "TSLA"
COMPANY_NAME = "Tesla"
API_Key_Stock = "###"
AP1_Key_News = "###"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now().strftime("%Y-%m-%d")
yesterday = (datetime.now() + relativedelta(days=-1)).strftime("%Y-%m-%d")
day_before_yesterday = (datetime.now() + relativedelta(days=-4)).strftime("%Y-%m-%d")

parameters_stock = {"function": "TIME_SERIES_DAILY",
                    "symbol": STOCK,
                    "apikey": API_Key_Stock}

data = requests.get(url="https://www.alphavantage.co/query", params=parameters_stock)
stock_data = data.json()

parameters_news = {"q": COMPANY_NAME,
                   "from": today,
                   "sortBy": "popularity",
                   "apiKey": AP1_Key_News}

news = requests.get(url="https://newsapi.org/v2/top-headlines", params=parameters_news)
news_data = news.json()

close_yesterday = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
close_day_before_yesterday = float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])
five_percent = close_day_before_yesterday * 0.05
threshold_lower = close_day_before_yesterday - five_percent
threshold_upper = close_day_before_yesterday + five_percent
if threshold_lower < close_yesterday < threshold_upper:
    print("Get news")
    for num in range(0, 4):
        headlines = news_data["articles"][num]["title"]
        print(headlines)

