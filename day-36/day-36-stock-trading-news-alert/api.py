from typing import Any

import requests


class API:
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.api_url = api_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get_data(self, params: dict[str, str]) -> dict[str, Any]:
        """Get data from the API using the given params.

        Args:
            params (dict[str, str]): The params to use for the API request.

        Returns:
            dict[str, Any]: The data from the API.
        """
        response = self.session.get(self.api_url, params=params)
        response.raise_for_status()
        return response.json()


class NewsAPI(API):
    def __init__(self, api_key: str, api_url: str, news_query: str):
        super().__init__(api_key, api_url)
        self.news_query = news_query

    def get_news(self) -> dict[str, Any]:
        """Get the news data from the API.

        Returns:
            dict[str, Any]: The news data for the news query.
        """
        params = {
            "q": self.news_query,
            "apiKey": self.api_key,
        }
        return self.get_data(params)

    def get_top_three_articles(self):
        """Get the top three articles for the news query. Includes title, description, and url.

        Returns:
            _type_ list[str]: The top three articles for the news query. Includes title, description, and url.
        """
        news = self.get_news()
        articles = news["articles"][:3]
        formatted_articles = self.format_articles(articles)
        return formatted_articles

    def format_articles(self, articles: list[dict[str, str]]) -> list[str]:
        """Format into string containing title, description, and url with newlines.

        Returns:
            _type_: str
        """
        formatted_articles = [
            f"Headline: {article['title']}. \nBrief: {article['description']}, \nURL: {article['url']}"
            for article in articles
        ]
        return formatted_articles


class StockAPI(API):
    def __init__(self, api_key: str, api_url: str, stock_symbol: str):
        super().__init__(api_key, api_url)
        self.stock_symbol = stock_symbol

    def get_stock_data(self):
        """Get the stock data from the API.

        Returns:
            _type_ dict[str, Any]: The stock data for the stock symbol.
        """
        params = {
            "symbol": self.stock_symbol,
            "apikey": self.api_key,
            "function": "TIME_SERIES_DAILY",
        }
        return self.get_data(params)

    def calculate_percentage_change(self) -> float:
        """Calculate the percentage change between the closing price of the stock yesterday and the day before yesterday.

        Returns:
            float: The percentage change between the closing price of the stock yesterday and the day before yesterday.
        """
        time_series_daily = self.get_stock_data()
        closing_prices = [float(value["4. close"]) for value in time_series_daily["Time Series (Daily)"].values()]
        return round((closing_prices[0] - closing_prices[1]) / closing_prices[1] * 100, 2)
