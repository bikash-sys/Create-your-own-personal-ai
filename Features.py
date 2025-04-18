import requests
import webbrowser
from pyttsx3 import init

def speak(text):
    engine = init('sapi5')
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()

def My_Location():
    try:
        response = requests.get("https://ipinfo.io").json()
        loc = response['loc']  # Latitude and Longitude
        city = response.get('city', 'Unknown city')
        region = response.get('region', '')
        country = response.get('country', '')

        speak(f"You are currently in {city}, {region}, {country}")
        speak(f"Your coordinates are {loc.replace(',', ' and ')}")

        print(f"City: {city}, Region: {region}, Country: {country}, Coordinates: {loc}")
        webbrowser.open(f"https://www.google.com/maps?q={loc}")
        
    except Exception as e:
        speak("Sorry, I couldn't fetch your location.")
        print("Location Error:", e)


import requests
import webbrowser
from pyttsx3 import init

def speak(text):
    engine = init('sapi5')
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()

def GoogleMaps(place):
    try:
        url = f"https://nominatim.openstreetmap.org/search"
        params = {
            'q': place,
            'format': 'json'
        }

        res = requests.get(url, params=params).json()

        if res:
            location = res[0]
            lat = location['lat']
            lon = location['lon']
            display = location.get('display_name', '')
            address = location.get('address', {})
            city = address.get('city') or address.get('town') or address.get('village') or "Unknown city"
            country = address.get('country', "Unknown country")

            speak(f"{place} is located in {city}, {country}")
            speak(f"Its coordinates are {lat} and {lon}")

            print(f"{place} ➤ City: {city}, Country: {country}, Coords: {lat}, {lon}")
            webbrowser.open(f"https://www.google.com/maps?q={lat},{lon}")
        else:
            speak(f"Sorry, I couldn't find {place} on the map.")
            print("No results found.")

    except Exception as e:
        speak("An error occurred while locating the place.")
        print("GoogleMaps Error:", e)
 

 
def Dateconverter(date_str):
    try:
       
        parts = date_str.lower().replace("and", "").split()
        parts = [p for p in parts if p.isdigit()]
        
        if len(parts) == 3:
            year, month, day = parts
            final_date = f"{year.zfill(4)}-{month.zfill(2)}-{day.zfill(2)}"
            print("Formatted date:", final_date)
            return final_date
        else:
            print("Could not parse date from input:", date_str)
            return None
    except Exception as e:
        print("Error in Dateconverter:", e)
        return None

