import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORDS_FILE = os.path.join(BASE_DIR, "words.txt")
GALLOWS_DIR = os.path.join(BASE_DIR, "gallows")
MAX_MISTAKES = 6

words = {}          
secret_word = ""    
description = ""    
opened = []         
used = []          
mistakes = 0       


def load_words():
    with open(WORDS_FILE, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                word, text = line.split(";")
                words[word.lower()] = text


def choose_word():
    global secret_word, description
    secret_word = random.choice(list(words))
    description = words[secret_word]


def prepare_mask():   
    global opened
    opened = ["_"] * len(secret_word)


def is_won():
    return "_" not in opened


def is_lost():
    return mistakes >= MAX_MISTAKES


def is_game_on():
    return not is_won() and not is_lost()


def is_valid_letter(text):
    return len(text) == 1 and text.isalpha()


def is_repeated(letter):
    return letter in used


def is_in_word(letter):
    return letter in secret_word



def ask_letter():
    letter = input("Назовите букву: ").strip().lower()
    while not is_valid_letter(letter):
        print("Нужно ввести одну букву!")
        letter = input("Назовите букву: ").strip().lower()
    return letter


def open_letter(letter):
    used.append(letter)
    for index, char in enumerate(secret_word):
        if char == letter:
            opened[index] = letter


def add_mistake(letter):
    global mistakes
    used.append(letter)
    mistakes += 1



def read_gallows():
    path = os.path.join(GALLOWS_DIR, f"stage_{mistakes}.txt")
    with open(path, encoding="utf-8") as file:
        return file.read()


def show_welcome():
    print("Виселица на поле чудес")
    print(f"Слово из {len(secret_word)} букв.")


def show_state():
    print()
    print("Описание:", description)
    print("Слово:   ", " ".join(opened))
    print("Названо: ", ", ".join(used))


def show_repeated():
    print("Эта буква уже была!")


def show_hit():
    print("Есть такая буква!")


def show_miss():
    print("Нет такой буквы!")
    print(read_gallows())


def show_result():
    if is_won():
        print(f"\nПоздравляем! Вы угадали слово: {secret_word}")
    else:
        print(f"\nВы проиграли. Было загадано слово: {secret_word}")
