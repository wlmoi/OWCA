from src.A_Functions import *
from src.F00_RNG import *
import typing


def MonsterLevel(monster_data: dict, n_times:int) -> dict:
    for i in range(n_times-1):
        attack: int = int(monster_data['atk_power'] * 11/10)
        defense: int = int(monster_data['def_power'] * 11/10)
        hp: int = int(monster_data['hp'] * 11/10)

        monster_data["atk_power"] = attack
        monster_data["def_power"] = defense
        monster_data["hp"] = hp
    return monster_data

# Use Case
# MonsterLevel(monster_data= {'id': 5, 'type': 'Chacha', 'atk_power': 80, 'def_power': 30, 'hp': 700}, n_times= 2)


def Attack(monster_atk: int, monster_def: int) -> int:
    damage = monster_atk * (130-RNG(60))/100
    damage -= damage * Defend(monster_def)
    # Mengeluarkan damage dealt oleh monster
    return int(damage)

# Use Case
# monsterA_hp -= Attack(monsterB_atk, monsterA_def)


def Defend(monster_def: int) -> float:
    damage_reduction: float = RNG(monster_def)/100
    # Mengeluarkan presentase damage reduction
    return damage_reduction

# Use Case
# damage -= damage * Defend(monster_def)


def MonsterDetail(bigdata, monster_id: int, level: int = 1) -> dict:
    monster_data: list = bigdata['monster'][1:]
    for temp in monster_data:
        data = temp.copy()
        if int(data['id']) == int(monster_id):
            data = MonsterLevel(data, level)
            return data
    return

# Use Case
# MonsterDetail(bigdata, monster_id= 2, level= 2)