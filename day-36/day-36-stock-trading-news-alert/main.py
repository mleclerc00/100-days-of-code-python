from os import environ

from twilio.rest import Client

from api import NewsAPI, StockAPI

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_URL = "https://www.alphavantage.co/query"
STOCK_API_KEY = environ["STOCK_API_KEY"]

NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = environ["NEWS_API_KEY"]

TWILIO_ACCOUNT_SID = environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = environ["TWILIO_AUTH_TOKEN"]
TWILIO_PHONE_NUMBER = environ["TWILIO_PHONE_NUMBER"]
MY_PHONE_NUMBER = environ["MY_PHONE_NUMBER"]


# Get the percentage change between the closing price of the stock yesterday and the day before yesterday.
tesla_stock = StockAPI(STOCK_API_KEY, STOCK_API_URL, STOCK)
tesla_percentage_change = tesla_stock.calculate_percentage_change()

# determine if the percentage change is positive or negative
if tesla_percentage_change > 0:
    emoji = "🔺"
else:
    emoji = "🔻"

# if the percentage change is greater than 5%, send a text message
if abs(tesla_percentage_change) > 4:
    # Get the top three articles for the news query. Includes title, description, and url.
    tesla_news = NewsAPI(NEWS_API_KEY, NEWS_API_URL, COMPANY_NAME)
    tesla_articles = tesla_news.get_top_three_articles()

    # define message body
    newlines = "\n\n"
    message_body = f"{STOCK}: {emoji}{tesla_percentage_change}% \n\n{newlines.join(tesla_articles)}"

    # Send a text message with the percentage change and the top three articles for the news query.
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message_body,
        from_=TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER,
    )
    print(message.status)
