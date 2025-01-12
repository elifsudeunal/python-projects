import json
import os

try:
    from termcolor import cprint  # terminalde renkli yazdırma fonksiyonu
except ImportError:
    def cprint(*args, **kwargs):  # Eğer termcolor kütüphanesi yüklenmediyse, print fonksiyonu kullanılır
        print(*args)

words = ["fan", "adapter", "pen", "mouse", "phone", "headphones", "chestnut", "note", "kid"]

def get_letter():  # Harf alma fonksiyonu, artık global olarak kullanılıyor
    proceed = True
    while proceed:
        letter = input("Enter a letter: ")
        if letter.lower() == "quit":
            cprint("See you next time", color="red", on_color="on_blue")
            exit()  # Program sonlanır
        elif len(letter) == 1 and letter.isalpha():
            proceed = False
        else:
            cprint("Invalid input", color="red", on_color="on_grey")
    
    return letter.lower()

def game_setup():
    global selected_word, visible_word, lives  # visible_word ve diğer değişkenler global yapılıyor
    import random
    selected_word = random.choice(words)
    visible_word = ["-"] * len(selected_word)
    lives = 5

def game_loop():
    global visible_word, lives
    while lives > 0 and selected_word != "".join(visible_word):
        cprint("word: " + "".join(visible_word), color="cyan", attrs=["bold"])
        cprint("lives : <" + "❤" * lives + " " * (5 - lives) + ">", color="cyan", attrs=["bold"])

        entered_letter = get_letter()  # Burada get_letter() fonksiyonu çağrılıyor
        positions = check_letter(entered_letter)
        if positions:
            for p in positions:
                visible_word[p] = entered_letter
        else:
            lives -= 1

def check_letter(entered_letter):
    positions = []
    for index, letter in enumerate(selected_word):
        if letter == entered_letter:
            positions.append(index)
    return positions

def show_scoreboard():
    data = read_settings()
    cprint("|Score\t\tUser|", color="white", on_color="on_grey")
    cprint("|------------------------|", color="white", on_color="on_grey")
    for score, user in data["scores"]:
        cprint("|"+str(score) +"\t\t"+ user+" "*(9-len(user))+"|", color="white", on_color="on_grey")
    cprint("|------------------------|", color="white", on_color="on_grey")

def update_scoreboard():
    data = read_settings()
    data["scores"].append((lives, data["last_user"]))
    data["scores"].sort(key=lambda score_tuple: score_tuple[0], reverse=True)
    data["scores"] = data["scores"][:5]
    write_settings(data)

def game_result():
    if lives > 0:
        cprint("You won", color="yellow", on_color="on_red")
        update_scoreboard()
    else:
        cprint("You lost", color="red", on_color="on_yellow")
    show_scoreboard()

def check_and_create_file():
    write = False
    if os.path.exists("settings.json"):
        try:
            read_settings()
        except ValueError as e:
            cprint("Error: ValueError(" + ",".join(e.args) + ")", color="red", on_color="on_blue", attrs=["bold"])
            os.remove("settings.json")
            write = True
    else:
        write = True

    if write:
        write_settings({"scores": [], "last_user": ""})

def read_settings():
    with open("settings.json") as f:
        return json.load(f)

def write_settings(data):
    with open("settings.json", "w") as f:
        json.dump(data, f)

def update_user_name():
    data = read_settings()
    data["last_user"] = input("Enter your name: ")
    while not data["last_user"] or len(data["last_user"]) > 9:
        data["last_user"] = input("Please enter a name with a length of 9 characters: ")
    write_settings(data)

def user_check():
    data = read_settings()
    print("Last user: " + data["last_user"])
    if not data["last_user"]:
        update_user_name()
    elif input("Is this you? (y/n) ").lower() == "n":
        update_user_name()

def main():
    repeat_game = True
    check_and_create_file()
    cprint("Hello, welcome to Hangman.", color="white", on_color="on_green", attrs=["bold"])
    cprint("Help: During the game, type quit to exit", color="cyan", on_color="on_magenta", attrs=["bold"])
    cprint("-"*30, color="cyan", on_color="on_magenta", attrs=["bold"])
    show_scoreboard()
    user_check()
    while repeat_game:
        game_setup()
        game_loop()
        game_result()
        if input("Continue? (y/n) ").lower() == "n":
            repeat_game = False
    cprint("Goodbye", color="red", on_color="on_white")

main()
