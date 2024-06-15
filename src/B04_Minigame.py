from src.F00_RNG import *
from src.A_Functions import *
from src.A_AddOns import *
import time


def Minigame(bigdata: dict, user_id: int) -> dict:
    while True:
        # Initialize
        ClearScreen()
        print(text_ascii['minigame'])
        print("======== List Minigame ========")
        print("1. Jackpot")
        print("2. Hangman")
        print("3. Quit")
        # Input
        choice: int = InputVerifier("")
        if choice == 1:
            bigdata = PlayJackpot(bigdata, user_id)
        elif choice == 2:
            bigdata = PlayHangman(bigdata, user_id)
        elif choice == 3:
            break
    return bigdata


def PlayHangman(bigdata: dict, user_id: int) -> dict:
    ClearScreen()
    print(text_ascii['hangman'])
    print("\n============================")
    choice: str = "Y"
    # Mengulang sampai choice sama dengan 'N'
    while choice == ("Y"):
        choice = input("\nMulai bermain dengan 300 oc (Y/N)\n>>> ").upper()
        if choice == "Y":
            if bigdata['user'][user_id]['oc'] >= 300:
                bigdata['user'][user_id]['oc'] -= 300
                bigdata['user'][user_id]['oc'] += Hangman()
            else:
                print("OC kamu tidak mencukupi..")
        elif choice == "N":
            return bigdata


def Hangman(bigdata: dict,  user_id: int) -> int:

    # Memilih kata random
    chosen_word = hangman_words[RNG(len(hangman_words))]
    word_length = len(chosen_word)
    # Initialize
    end_of_game = False
    lives = 5
    oc_gain = 0

    # Display kata dengan '_'
    display = []
    for _ in range(word_length):
        display += "_"
    
    print(f"{ManualJoin(display, ' ')}")

    # Mengulang sampai nyawa habis
    while not end_of_game:
        guess = input("Tebak huruf: ").lower()
        # Jika tebakan ada pada chosen_word
        if guess in display:
            print(f"Anda telah memilih huruf {guess}")
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        # Jika tebakan tidak ada pada chosen_word

        if guess not in chosen_word:
            print(f"Kamu menebak {guess}, tetapi tidak ada di kata.\nNyawamu berkurang satu")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("Kamu kalah.")
        print(f"{ManualJoin(display, ' ')}")

        # Mengecek apakah sudah terjawab semua atau belum
        if "_" not in display:
            end_of_game = True
            oc_gain = 500
            print("Kamu menang 500 oc.")
        print(hangman_stages[lives])

    return oc_gain

def PlayJackpot(bigdata, user_id):
    ClearScreen()
    print(text_ascii['jackpot'])
    print("""
======= DAFTAR ITEM ========
1. Topi     : 50 OC
2. Pedang   : 100 OC
3. Koin     : 200 OC
4. Potion   : 300 OC
5. Monster  : 500 OC""")
    
    choice = "Y"
    while choice == ("Y"):
        choice = input("\nMulai bermain dengan 500 oc (Y/N)\n>>> ").upper()
        if choice == "Y":
            if bigdata['user'][user_id]['oc'] >= 500:
                bigdata['user'][user_id]['oc'] -= 500
                bigdata['user'][user_id]['oc'] += Jackpot()
            else:
                print("OC kamu tidak mencukupi..")
        elif choice == "N":
            return bigdata

def Jackpot():
    oc = 0
    jackpot_item = {
        'topi'   : 50,
        'pedang' : 100,
        'koin'   : 200,
        'potion' : 300,
        'monster': 500,
    }

    ClearScreen()
    item_1 = PickItem()
    
    print("---------------------------------------")
    print(f"---- {item_1} |         |         -----")
    print("---------------------------------------")

    time.sleep(RNG(2))
    ClearScreen()
    item_2 = PickItem()
    print("---------------------------------------")
    print(f"---- {item_1} | {item_2} |        -----")
    print("---------------------------------------")

    time.sleep(RNG(2))
    ClearScreen()
    item_3 = PickItem()
    
    print("---------------------------------------")
    print(f"---- {item_1} | {item_2} | {item_3} -----")
    print("---------------------------------------")
    
    if item_1 == item_2 == item_3:
        print("Anda mendapatkan monster")
        return oc
    else:
        oc = jackpot_item[item_1] + jackpot_item[item_2] + jackpot_item[item_3]
        print(oc)
        return oc

def PickItem():
    item = RNG(5)
    if item == 1:
        return "topi"
    elif item == 2:
        return "pedang"
    elif item == 3:
        return "koin"
    elif item == 4:
        return "potion"
    elif item == 5:
        return "monster"