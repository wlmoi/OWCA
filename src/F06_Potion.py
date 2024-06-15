import typing
from src.A_Functions import *

def PotionMenu(user_inventory, monster_data) -> tuple[dict, bool]:
    # Print Menu Potion
    count = 1
    for i in range(len(user_inventory)):
        print(f"{count}. {user_inventory[i]['type']} (Qty: {user_inventory[i]['quantity']})")
        count += 1
    print(f"{count}. Cancel")

    # Input pengguna
    user_choice = int(input("Potion digunakan: "))
    # Jika memilih potion yang ada
    if user_choice <= len(user_inventory):
        user_inventory[user_choice-1]['quantity'] -= 1
        if user_inventory[user_choice-1]['type'] == 'strength':
            monster_data = StrengthPotion(monster_data)
        elif user_inventory[user_choice-1]['type'] == 'resilience':
            monster_data = ResiliencePotion(monster_data)
        elif user_inventory[user_choice-1]['type'] == 'healing':
            monster_data = HealingPotion(monster_data)
        ClearScreen()
        return monster_data, True

    # Jika memilih keluar
    elif user_choice == (len(user_inventory) + 1 ):
        ClearScreen()
        return monster_data, False


def StrengthPotion(monster_data: dict) -> dict:
    monster_data['atk_power'] = round(float(monster_data['atk_power'] * 1.1))
    return monster_data


def ResiliencePotion(monster_data: dict) -> dict:
    monster_data['def_power'] = round(float(monster_data['def_power'] * 1.1))
    return monster_data


def HealingPotion(current_monster_data: dict, monster_data: dict) -> int:
    current_monster_data['hp'] = current_monster_data['hp'] * 1.25
    if current_monster_data['hp'] > monster_data['hp']:
        current_monster_data['hp'] = monster_data['hp']
    return current_monster_data
