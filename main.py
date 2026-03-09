import requests
import datetime
import smtplib
import os


MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

ISS_URL = os.getenv("ISS_URL")
SUN_URL = os.getenv("SUN_URL")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

response = requests.get(url=ISS_URL)
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

def within_range():
    if iss_latitude-5 <= MY_LAT <= iss_latitude+5 and iss_longitude-5 <= MY_LONG <= iss_longitude+5:
        return True
    else:
        return False

def is_dark():
    if time_now.hour > sunset or time_now.hour < sunrise:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url=SUN_URL, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.datetime.now()

#If the ISS is close to my current position
if within_range() and is_dark():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=my_email, to_addrs="bananabottle82@gmail.com",
                            msg="Subject:Look Up!\n\nSpot the International Space Station above you right now.")
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
