import requests
import datetime
import time
import smtplib

MY_LAT = 123 #Your latitude
MY_LNG = 321 #Your longitude
MY_EMAIL = "test@gmail.com" #Your mail
MY_PASSWORD = "test" #Your app password


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if iss_latitude >= MY_LAT -5 and iss_latitude <= MY_LAT +5 and iss_longitude >= MY_LNG -5 and iss_longitude <= MY_LNG +5:
        return True
        
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if time_now.hour <= sunrise and time_now.hour >= sunset:
       return True

time_now = datetime.datetime.now()

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():    
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, 
                to_addrs="test@gmail.com", #address mail
                msg=f"Subject: Look up in the sky\n\n The ISS is above you."
                )