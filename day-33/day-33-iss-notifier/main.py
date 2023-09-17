import os
import smtplib
import time
from datetime import datetime
from typing import Union

import requests


def get_sunset_data(latitude: float, longitude: float, formatted: int = 0) -> dict[str, dict[str, str]]:
    """Get sunset and sunrise data from API

    Args:
        latitude (float): latitude of the location
        longitude (float): longitude of the location
        formatted (int, optional): 0 for 24-hour time format and 1 for 12-hour time format. Defaults to 0.

    Returns:
        dict[str, dict[str, str]]: sunset and sunrise data
    """
    response = requests.get(
        f"https://api.sunrise-sunset.org/json?lat=&{latitude}&lng={longitude}&formatted={formatted}"
    )
    response.raise_for_status()
    return response.json()


def get_iss_location() -> dict[Union[str, int], dict[str, str]]:
    """Get ISS location from API

    Returns:
        dict[Union[str, int], dict[str, str]]: ISS location data
    """
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    return response.json()


def get_hour(time: str) -> int:
    """Get hour from time

    Args:
        time (str): time in format "2021-08-25T18:59:00+00:00"

    Returns:
        int: hour
    """
    return int(time.split("T")[1].split(":")[0])


def is_dark(sunset: int, sunrise: int, time_now: int) -> bool:
    """Check if it is dark

    Args:
        sunset (int): Hour of sunset
        sunrise (int): Hour of sunrise
        time_now (int): Current hour

    Returns:
        bool: True if it is dark, False otherwise
    """
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


def iss_is_close() -> bool:
    """Check if ISS is close

    Returns:
        bool: True if ISS is close, False otherwise
    """
    if (
        local_latitude - 5 <= iss_latitude <= local_latitude + 5
        and local_longitude - 5 <= iss_longitude <= local_longitude + 5
    ):
        return True
    return False


# Get local coordinates
local_latitude = float(os.environ["LATITUDE"])
local_longitude = float(os.environ["LONGITUDE"])

# Get sunset and sunrise time
sunset_data = get_sunset_data(local_latitude, local_longitude)
sunset = get_hour(sunset_data["results"]["sunset"])
sunrise = get_hour(sunset_data["results"]["sunrise"])

# Get ISS location
iss_location = get_iss_location()
iss_latitude = float(iss_location["iss_position"]["latitude"])
iss_longitude = float(iss_location["iss_position"]["longitude"])

# Get current time
time_now = datetime.now().hour

# Run every minute
while True:
    time.sleep(60)
    # Check if it is dark and ISS is close
    if is_dark(sunset, sunrise, time_now) and iss_is_close():
        # Send email notification
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.environ["EMAIL"], password=os.environ["PASSWORD"])
            connection.sendmail(
                from_addr=os.environ["EMAIL"],
                to_addrs=os.environ["EMAIL"],
                msg="Subject:Look Up\n\nThe ISS is above you in the sky.",
            )
