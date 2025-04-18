import requests
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from io import BytesIO
from PIL import Image
import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()

def NasaNews(date):
    try:
        url = f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date={date}"
        response = requests.get(url)
        data = response.json()

        title = data.get("title", "No title")
        explanation = data.get("explanation", "No explanation available")
        media_type = data.get("media_type", "")
        image_url = data.get("url", "")

        speak(f"Here's the space news for {date}")
        speak(f"Title: {title}")
        speak(explanation)

        if media_type == "image":
            show_image(image_url, title)
        else:
            speak("This one is a video. Opening it in your browser.")
            import webbrowser
            webbrowser.open(image_url)

    except Exception as e:
        speak("Sorry sir, I couldn't fetch the space news.")
        print("Error:", e)

def show_image(url, title):
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.setGeometry(300, 100, 800, 600)
    label = QLabel(window)

    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image.save("nasa_temp_image.jpg")

    pixmap = QPixmap("nasa_temp_image.jpg")
    label.setPixmap(pixmap)
    label.setScaledContents(True)
    label.setGeometry(0, 0, 800, 600)

    window.setWindowTitle(title)
    window.show()
    sys.exit(app.exec_())
