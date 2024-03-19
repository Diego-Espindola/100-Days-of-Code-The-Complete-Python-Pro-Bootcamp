import requests
from twilio.rest import Client
from info import stock_api_key, news_api_key, phone_number, account_sid, auth_token, from_number

# noinspection SpellCheckingInspection
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PERCENTAGE_LIMIT = 2


def send_sms(body, to=phone_number):
    client = Client(account_sid, auth_token)

    try:
        client.messages.create(
            from_=from_number,
            body=body,
            to=to
        )
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending SMS: {e}")


def api_get(url, **kwargs):
    try:
        r = requests.get(url, params=kwargs)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return {}


def main():
    try:
        data = api_get(
            url="https://www.alphavantage.co/query",
            function="TIME_SERIES_DAILY",
            symbol=STOCK,
            apikey=stock_api_key
        )
        data = data.get("Time Series (Daily)", {})
        dates = list(data)
        yesterday = dates[1]
        the_day_before_yesterday = dates[2]

        final_value = float(data[yesterday].get('4. close', 0))
        initial_value = float(data[the_day_before_yesterday].get('1. open', 0))
        percentage_increase = ((final_value - initial_value) / initial_value) * 100
        print(f"Percentage Increase: {percentage_increase}%")

        if abs(percentage_increase) > PERCENTAGE_LIMIT:
            data = api_get(
                url="https://newsapi.org/v2/everything",
                q=COMPANY_NAME,
                from_='2024-02-19',
                sortBy="publishedAt",
                apiKey=news_api_key
            )
            articles = data.get('articles', [])[:3]
            percentage_increase = round(percentage_increase, 2)
            for article in articles:
                headline = article.get('title', 'No title available')
                brief = article.get('description', 'No description available')
                message = (f"{STOCK}: {'🔺' if percentage_increase > 0 else '🔻'}{abs(percentage_increase)}%"
                           f"\nHeadline: {headline}\nBrief: {brief}")
                send_sms(message)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
