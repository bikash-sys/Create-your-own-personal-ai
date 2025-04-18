import random
import pygame
import sys
import threading
from word2number import w2n
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QGridLayout

def speak(text):
    import pyttsx3
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()

def take_command():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=5)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except:
        return "None"

# ------------------- GAME 1: GUESS THE NUMBER -------------------
def guess_the_number():
    speak("Welcome to Guess the Number! I have thought of a number between 1 and 10. Try to guess it!")
    number = random.randint(1, 10)
    attempts = 0

    while True:
        speak("Your guess?")
        user_input = take_command()
        try:
            guess = w2n.word_to_num(user_input)
        except:
            speak("I didn't understand a number. Please try again.")
            continue

        attempts += 1

        if guess == number:
            speak(f"🎉 Correct! You guessed it in {attempts} tries. Impressive!")
            break
        elif guess < number:
            speak("Too low. Try a higher number.")
        else:
            speak("Too high. Try a lower number.")

# ------------------- GAME 2: TIC TAC TOE -------------------
class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 300)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.board = [' '] * 9
        self.buttons = []
        self.current_player = 'X'
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        for i in range(9):
            button = QPushButton('')
            button.setFixedSize(80, 80)
            button.setStyleSheet("font-size: 24px;")
            button.clicked.connect(lambda _, i=i: self.make_move(i))
            self.buttons.append(button)
            layout.addWidget(button, i // 3, i % 3)
        self.setLayout(layout)

    def make_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].setText(self.current_player)

            if self.check_winner(self.current_player):
                if self.current_player == 'X':
                    speak("You win! Congrats!")
                else:
                    speak("Haha, I win. Better luck next time!")
                self.reset_game()
                return
            elif ' ' not in self.board:
                speak("It's a tie!")
                self.reset_game()
                return

            self.current_player = 'O' if self.current_player == 'X' else 'X'
            if self.current_player == 'O':
                self.ai_move()

    def ai_move(self):
        empty = [i for i, val in enumerate(self.board) if val == ' ']
        move = random.choice(empty)
        self.make_move(move)

    def check_winner(self, player):
        combos = [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]
        return any(all(self.board[i] == player for i in combo) for combo in combos)

    def reset_game(self):
        self.board = [' '] * 9
        for button in self.buttons:
            button.setText('')
        self.current_player = 'X'

# ------------------- GAME 3: SNAKE -------------------
def snake_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 400), pygame.NOFRAME)
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    snake = [(100, 50), (90, 50), (80, 50)]
    direction = 'RIGHT'
    apple = (300, 200)
    score = 0

    def move_snake():
        nonlocal snake, apple, score
        x, y = snake[0]
        if direction == 'UP':
            y -= 10
        elif direction == 'DOWN':
            y += 10
        elif direction == 'LEFT':
            x -= 10
        elif direction == 'RIGHT':
            x += 10
        new_head = (x, y)
        if new_head in snake or x < 0 or x > 590 or y < 0 or y > 390:
            speak(f"Oops! You lost. Your score was {score}")
            pygame.quit()
            return False
        snake.insert(0, new_head)
        if new_head == apple:
            score += 1
            speak(f"Great! Score: {score}")
            return True
        else:
            snake.pop()
            return True

    run = True
    while run:
        screen.fill((0, 0, 0))
        for segment in snake:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, 10, 10))
        pygame.draw.rect(screen, (255, 0, 0), (*apple, 10, 10))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_ESCAPE:
                    run = False

        if not move_snake():
            break
        clock.tick(10)

# ------------------- GAME PLAY CONTROLLER -------------------
def game_play():
    speak("Hey there! I currently have three games for you to enjoy.")
    speak("Say the name of the game you want to play: Guess the number, Tic Tac Toe, or Snake Game.")

    while True:
        choice = take_command()

        if 'guess' in choice:
            guess_the_number()
        elif 'tic tac toe' in choice or 'tick tack toe' in choice:
            speak("Launching Tic Tac Toe!")
            app = QApplication(sys.argv)
            game = TicTacToe()
            game.show()
            app.exec_()
        elif 'snake' in choice:
            speak("Launching the classic Snake Game!")
            snake_game()
        elif 'exit' in choice or 'quit' in choice:
            speak("Exiting game mode. Back to command mode.")
            break
        else:
            speak("I didn't catch that. Please say the game name again.")
