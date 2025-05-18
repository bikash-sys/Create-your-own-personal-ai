
## 🤖 Jarvis - Python Voice Assistant

**Jarvis** is a desktop-based virtual assistant built using Python. Inspired by Iron Man’s J.A.R.V.I.S., this assistant can perform tasks such as telling the time and date, searching the web, opening applications, fetching information, and responding to basic commands through voice interaction.

---

### 🚀 Features 

- 🔊 Voice recognition and response (via `speech_recognition` and `pyttsx3`)
- 🕓 Tells current time and date
- 🌐 Google, Wikipedia, and YouTube search
- 📂 Opens system applications (e.g. Chrome, Notepad, VS Code)
- 💬 Greets user based on time of day
- 🎵 Plays music from your local folder
- 📧 Sends emails (optional, if SMTP configured)
- 🧠 Extensible: Add more tasks with ease

---

### 📦 Requirements

Install dependencies using pip:

```bash
pip install pyttsx3 SpeechRecognition wikipedia pywhatkit pyjokes pyautogui
```

You may also need:

- Python 3.8+
- [pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) (for microphone input, Windows users can download `.whl`)

---

### 🧠 How It Works

Jarvis listens to your voice commands using a microphone and matches keywords to execute pre-defined actions.

Example:

- "What is the time?" → tells the current time
- "Open YouTube" → opens youtube.com in browser
- "Search for Python tutorials" → performs Google search

---

### ▶️ Usage

Run the assistant:

```bash
python jarvis.py
```

Then speak commands like:

- `"Hello Jarvis"`
- `"What is the time?"`
- `"Open Notepad"`
- `"Search Wikipedia for Python"`
- `"Play music"`
- `"Tell me a joke"`

---

### 🛠️ Customization

You can customize:

- Voice (male/female) via `pyttsx3.init()` properties
- Add new commands inside the `while True:` loop
- Connect to APIs (weather, news, etc.)
- Add a GUI using Tkinter or PyQt if needed

---

### 🔐 Optional: Email Setup

To enable email sending, configure your email credentials securely (avoid hardcoding in the script):

```python
server.login(EMAIL, PASSWORD)  # Use environment variables instead
```

---

### 📁 Project Structure

```
jarvis/
├── jarvis.py
├── music/           # local songs for play music feature
└── README.md
```

---

### ✨ Future Ideas

- Add AI chatbot (e.g., ChatGPT API)
- Integrate with smart devices
- Schedule tasks or alarms
- Add GUI interface

---

### 📜 License

Open-source project for educational purposes. Customize freely!

---
