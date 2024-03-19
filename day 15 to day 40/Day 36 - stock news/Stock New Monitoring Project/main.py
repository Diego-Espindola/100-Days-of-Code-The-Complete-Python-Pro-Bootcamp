import requests
from twilio.rest import Client
from info import stock_api_key, news_api_key, phone_number, account_sid, auth_token

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def send_sms(body, to=phone_number):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_="+17814233150",
      body=body,
      to=to
    )
    print(message.sid)


def api_get(url, **kwargs):
    r = requests.get(url, params=kwargs)
    return r.json()


def main():
    ## STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    data = api_get(
        url="https://www.alphavantage.co/query",
        function="TIME_SERIES_DAILY",
        symbol=STOCK,
        apikey=stock_api_key
    )
    data = data["Time Series (Daily)"]
    dates = list(data)
    yesterday = dates[1]
    the_day_before_yesterday = dates[2]

    final_value = float(data[yesterday]['4. close'])
    initial_value = float(data[the_day_before_yesterday]['1. open'])
    percentage_increase = ((final_value - initial_value) / initial_value) * 100
    print(percentage_increase)
    if abs(percentage_increase) > 5:
        print('Get News')

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    data = api_get(
        url="https://newsapi.org/v2/everything",
        q=COMPANY_NAME,
        from_='2024-02-19',
        sortBy="publishedAt",
        apiKey=news_api_key
    )
    articles = data['articles'][:3]
    print(articles)
    ## STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    for article in articles:
        headline = article['title']
        brief = article['description']
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


if __name__ == "__main__":
    main()
