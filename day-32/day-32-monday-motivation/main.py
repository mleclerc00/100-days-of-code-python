import datetime as dt
import os
import random
import smtplib


def read_quotes() -> list[str]:
    """Reads quotes from a file and returns a list of quotes.

    Returns:
        list[str]: List of quotes.
    """
    with open("quotes.txt", "r") as file:
        quotes_list = file.readlines()
    return quotes_list


def choose_random_quote(quotes_list: list[str]) -> str:
    """Chooses a random quote from a list of quotes.

    Args:
        quotes_list (list[str]): List of quotes.

    Returns:
        str: Random quote.
    """
    random_quote = random.choice(quotes_list)
    return random_quote


def send_email(quote: str) -> None:
    """Sends an email with a motivational quote.

    Args:
        quote (str): Motivational quote.
    """

    # Get email, mail server and password from environment variables
    my_email = os.environ["EMAIL"]
    password = os.environ["PASSWORD"]
    mail_server = os.environ["MAIL_SERVER"]

    # Send email
    with smtplib.SMTP(mail_server, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Motivational Quote\n\n{quote}")


# Get current date and time information
dt_now = dt.datetime.now()

# Check if it is Saturday (weekday 5) and send an email with a random quote
if dt_now.weekday() == 5:
    quotes_list = read_quotes()
    random_quote = choose_random_quote(quotes_list)
    send_email(random_quote)
