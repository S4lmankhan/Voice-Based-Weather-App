import requests
import json
import os

"""
THIS CODE WILL RUN ONLY FOR MAC OS , IF YOU WANT TO RUN THIS ON WINDOWS TRY USING THE WINDOWS VERSION OF THIS CODE USING PYTTSX3 MODULE
"""

print("Welcome to the Digital Weather Application Created By CodeWithSalty on instagram also known as Salmaan "
          "If you want to know the current condition of your city !!!")

os.system(
        "say 'Welcome to the Digital Weather Application. Created By CodeWithSalty on instagram also known as Salmaan"
        " If you want to know the current condition of your city, kindly put the name of your city here or press Q to Exit The Application.'")

while True:

    city = input("Enter the name of your city or press Q to quit -----> : \n ")

    if city == " ":
        print("Please Enter a Proper Name of the City Sir !! ---> ")
        os.system("Please Enter a Proper Name of the City Sir")


    if city.lower() == 'q':
        os.system("say 'Goodbye! Stay safe and have a nice day my friend !'")
        break

    """
    UPDATE YOUR API KEY BELOW ONLY IF U DONT HAVE ANY TRY GETTING YOURS FROM weatherapi.com
    """

    try:
        api_key = "YOUR API KEY !!! "
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

        r = requests.get(url)
        wdic = json.loads(r.text)

        temp_c = wdic["current"]["temp_c"]
        temp_f = wdic["current"]["temp_f"]
        text = wdic["current"]["condition"]["text"]
        last_updated = wdic["current"]["last_updated"]
        wind_kph = wdic["current"]["wind_kph"]
        wind_mph = wdic["current"]["wind_mph"]
        wind_dir = wdic["current"]["wind_dir"]
        pressure_mb = wdic["current"]["pressure_mb"]
        pressure_in = wdic["current"]["pressure_in"]
        precip_mm = wdic["current"]["precip_mm"]
        precip_in = wdic["current"]["precip_in"]
        humidity = wdic["current"]["humidity"]
        cloud = wdic["current"]["cloud"]
        feelslike_c = wdic["current"]["feelslike_c"]
        feelslike_f = wdic["current"]["feelslike_f"]
        vis_km = wdic["current"]["vis_km"]
        vis_miles = wdic["current"]["vis_miles"]
        uv = wdic["current"]["uv"]
        gust_kph = wdic["current"]["gust_kph"]
        gust_mph = wdic["current"]["gust_mph"]

        weather_report = (
            f"The current weather of {city} is {temp_c} degrees Celsius or {temp_f} degrees Fahrenheit. \n"
            f"The condition is {text} and last updated on {last_updated}. \n"
            f"Wind speed is {wind_kph} kilometers per hour or {wind_mph} miles per hour from the {wind_dir} direction. \n"
            f"Pressure is {pressure_mb} millibars or {pressure_in} inches. \n"
            f"Precipitation is {precip_mm} millimeters or {precip_in} inches. \n"
            f"Humidity is {humidity} percent. \n"
            f"Cloud cover is {cloud} percent. \n"
            f"It feels like {feelslike_c} degrees Celsius or {feelslike_f} degrees Fahrenheit.\n"
            f"Visibility is {vis_km} kilometers or {vis_miles} miles. \n"
            f"UV index is {uv}. \n"
            f"Wind gusts are {gust_kph} kilometers per hour or {gust_mph} miles per hour.\n"
        )

        print(weather_report)
        os.system(f"say '{weather_report}'")

    except Exception as e:
        print(f"An error occurred: {e}")
        os.system("say 'There was an error retrieving the weather data. Please try again.'")
