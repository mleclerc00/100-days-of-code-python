import datetime as dt
import os
import random
import smtplib
import sys

import pandas as pd


def get_random_letter() -> str:
    """Chooses a random letter from the letter_templates folder

    Returns:
        str: The contents of the letter
    """
    if not os.path.exists("./letter_templates") or not os.listdir("./letter_templates"):
        print("No letter templates found")
        sys.exit(1)
    letters = os.listdir("./letter_templates")
    letter = random.choice(letters)
    with open(f"./letter_templates/{letter}") as file:
        letter = file.read()
    return letter


def send_email(email: str, message: str) -> None:
    """Sends an email to the specified email address

    Args:
        email (_type_): email address to send to
        message (_type_): message to send
    """
    try:
        my_email = os.environ["EMAIL"]
        password = os.environ["PASSWORD"]
        mail_server = os.environ["MAIL_SERVER"]
    except KeyError:
        print("Environment variables not set[EMAIL, PASSWORD, MAIL_SERVER]")
        return
    with smtplib.SMTP(mail_server, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{message}")


def get_birthdays() -> list[list[str]]:
    """Gets the birthdays from the birthdays.csv file

    Returns:
        list[list[str]]: A list of lists containing the email and name of the people who have birthdays today
    """
    today = dt.datetime.now()
    today_tuple = (today.month, today.day)
    try:
        birthdays = pd.read_csv("birthdays.csv")
    except FileNotFoundError:
        print("birthdays.csv not found")
        sys.exit(1)
    birthdays_dict = birthdays.to_dict(orient="records")
    today_birthdays = [
        [birthday["email"], birthday["name"]]
        for birthday in birthdays_dict
        if (birthday["month"], birthday["day"]) == today_tuple
    ]
    return today_birthdays


def send_all_emails() -> None:
    """Sends all the emails to the people who have birthdays today"""
    birthdays = get_birthdays()
    for birthday in birthdays:
        letter = get_random_letter()
        letter = letter.replace("[NAME]", birthday[0])
        send_email(birthday[1], letter)


send_all_emails()
