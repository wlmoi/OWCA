# Mengimport modul yang penting
from src.A_Functions import *
from src.A_AddOns import *
from src.F05_Monster import *
from src.F06_Potion import *
from src.F00_RNG import RNG
from src.F07_Inventory import *
from src.F05_Monster import *
from src.B03_MonsterBall import *

import time


def PrintMonster(side: str, monster_data: dict, monster_level: int, status: str = None) -> None:
    # Menentukan pihak
    if side == "opponent":
        print(monster_ascii[monster_data['type']])
        PrintTerrain('grass')

        # Menentukan apakah akan diprint saat di awal
        if status == "beginning":
            print(f"RAWRRR, Monster {monster_data['type']} telah muncul !!!\n")

        DisplayMonsterStat(monster_data=monster_data, monster_level= monster_level)
        return
    elif side == "player":
        print(monster_ascii[monster_data['type']])

        # Menentukan apakah akan diprint saat di awal
        if status == "beginning":
            print(f"GO, {monster_data['type']}!!\n")

        DisplayMonsterStat(monster_data=monster_data, monster_level= monster_level)
        return


def DisplayMonsterStat(monster_data: dict, monster_level: int) -> None:
    print("Name      :", monster_data["type"])
    print("ATK Power :", monster_data["atk_power"])
    print("DEF Power :", monster_data["def_power"])
    print("HP        :", monster_data["hp"])
    print("Level     :", monster_level)
    return


def MonsterAppear(monster_pool: dict) -> tuple[int, int]:

    # Menentukan monster appear dari RNG
    monster_appear_id    = RNG(len(monster_pool))
    time.sleep(1)
    monster_appear_level = RNG(5)

    return monster_appear_id, monster_appear_level

def Battle(bigdata: dict, user_id: int, in_arena: bool = False, level_setting: int = None):
    # Initialize
    ClearScreen()
    monster_pool   : list = bigdata['monster'][1:]
    exit_battle    : bool = False
    win_battle     : bool = False
    used_potion    : bool = False
    damage_dealt   : int  = 0
    damage_received: int  = 0
    turn_count     : int  = 1
    oc_gain        : int  = 0

    # Monster Musuh
    # Menentukan monster yang akan muncul secara random
    monster_appear_id, monster_appear_level = MonsterAppear(monster_pool)
    monster_appear = dict(monster_pool[monster_appear_id - 1])

    # Jika di arena, level sudah ditetapkan
    if in_arena:
        monster_appear_level = level_setting
    
    # Menyesuaikan data monster berdasarkan level monster
    MonsterLevel(monster_appear, monster_appear_level)
    PrintMonster(side="opponent", monster_data=monster_appear, monster_level=monster_appear_level, status="beginning")
    

    # Monster User
    print("\n============ MONSTER LIST ============")
    user_monster_pool = UserInventory(user_id=user_id, bigdata=bigdata, type="monster_inventory")
    user_inventory_pool = UserInventory(user_id=user_id, bigdata=bigdata, type="item_inventory")
    
    # Display monster yang ada pada inventory user
    id_count = 1
    for monster in user_monster_pool:
        print(f"{id_count}. {MonsterDetail(bigdata, monster['monster_id'], monster['level'])['type']}")
        id_count += 1
    if not in_arena:
        print(f"{id_count}. Keluar")

    # Memilih monster yang akan digunakan
    while True:
        user_choice = InputVerifier("\nPilih monster untuk bertarung")
        user_choice = int(user_choice)
        if user_choice == id_count and not in_arena:
            return 0
        elif user_choice > len(user_monster_pool):
            print("Pilihan nomor tidak tersedia!")
        else:
            user_choice -= 1
            ClearScreen()
            break

    # Mendapatkan data monster user
    user_monster_level = user_monster_pool[user_choice]['level']
    user_monster = dict(next((m for m in bigdata['monster'] if m['id'] == user_monster_pool[user_choice]['monster_id']), None))
    user_monster = (MonsterDetail(bigdata, monster_id=user_monster['id'], level=user_monster_level))

    PrintMonster(side="player", monster_data=user_monster, monster_level=user_monster_level, status='beginning')

    # Battle Loop
    while (user_monster['hp'] > 0) and (monster_appear['hp'] > 0):
        print(f"\n============ Your Turn! (turn: {turn_count}) ============")
        # Pilihan jika di luar arena
        if not in_arena:
            print("""1. Attack\n2. Use Potion\n3. Use Monster Ball\n4. Quit""")
        # Pilihan jika di arena
        elif in_arena:
            print("""1. Attack\n2. Use Potion\n3. Quit""")

        choice = input(">>> ")        

        ClearScreen()
        if monster_appear['hp'] <= 0 or user_monster['hp'] <= 0:
            break

        if choice == "1":
            print(f"============ TURN {turn_count} - {user_monster['type']} ============")
            # Monster User
            damage_dealt += Attack(user_monster['atk_power'], monster_appear['def_power'])
            monster_appear['hp'] -= Attack(user_monster['atk_power'], monster_appear['def_power'])
            # Mengecek HP Monster
            if monster_appear['hp'] <= 0:
                monster_appear['hp'] = 0
                PrintMonster(side="opponent", monster_data=monster_appear, monster_level=monster_appear_level)
                break

            # Musuh Attack
            damage_received += Attack(monster_appear['atk_power'], user_monster['def_power'])
            user_monster['hp'] -= Attack(monster_appear['atk_power'], user_monster['def_power'])
            # Mengecek HP Monster
            if user_monster['hp'] < 0:
                ClearScreen()
                print("Kamu kalah pertandingan ini")
                break
            
            PrintMonster(side="opponent", monster_data=monster_appear, monster_level=monster_appear_level)

            # Processing Other Turn
            time.sleep(RNG(2))
            ClearScreen()
            print(f"============ TURN {turn_count} - {user_monster['type']} ============")
            MonsterBattle(ascii_1=monster_ascii[monster_appear['type']], ascii_2=monster_ascii[user_monster['type']], detail_1=monster_appear, detail_2=user_monster, level_1=monster_appear_level, level_2=user_monster_level)
            turn_count += 1
        
        # Jika pilihan potion dan belum menggunakan potion
        elif choice == "2" and not used_potion:
            PrintMonster(side="player", monster_data=user_monster, monster_level=user_monster_level)
            print("============ POTION LIST ============")
            user_monster, used_potion = PotionMenu(user_inventory_pool, user_monster)
            PrintMonster(side="player", monster_data=user_monster, monster_level=user_monster_level)
            continue
        
        # Jika pilihan potion tetapi sudah menggunakan potion
        elif choice == "2" and used_potion:
            PrintMonster(side="player", monster_data=user_monster, monster_level=user_monster_level)
            print("\nAnda sudah memakai potion")

        # Jika memilih Monster Ball di luar arena
        elif choice == "3" and not in_arena:
            monster_before = len(user_monster_pool)
            amount_monsterball = next((i for i in bigdata['item_inventory'] if (i['user_id'] == user_id) and (i['type'] == 'monsterball')), None)
            if amount_monsterball and (amount_monsterball['quantity'] > 0):
                MonsterBall(user_monster_pool, user_id, monster_appear_id, monster_appear_level)
                amount_monsterball['quantity'] -= 1
                monster_after = len(user_monster_pool)
                # Berhasil menangkap Monster
                if monster_after > monster_before:
                    monster_catched_data = {
                        'user_id'   : user_id,
                        'monster_id': monster_appear_id,
                        'level'     : monster_appear_level
                    }
                    bigdata['monster_inventory'].append(monster_catched_data)
                    break
                else:
                    PrintMonster(side="player", monster_data=user_monster, monster_level=user_monster_level)
            else:
                print("Anda tidak mempunyai monsterball.")

        # Exit battle
        elif (choice == "4" and not in_arena) or (choice =="3" and in_arena):
            exit_battle = True
            break
        
        # Jika input selain yang dimaksud
        else:
            print(f"GO, {user_monster['type']}!!\n")
            PrintMonster(side="player", monster_data=user_monster, monster_level=user_monster_level)
            print("\nInput Anda salah!")

    # Pengecekan HP
    if monster_appear['hp'] <= 0:
        print(f"Kamu berhasil mengalahkan {monster_appear['type']}!")
        # Jika tidak di arena, oc yang didapatkan akan RNG
        if not in_arena:
            oc_gain = 5 + RNG(25)
            print(f"Kamu mendapatkan {oc_gain} OC!")
        win_battle = True
    elif exit_battle:
        print("Kamu meninggalkan battle ini.")

    if not in_arena:
        return oc_gain
    elif in_arena:
        return win_battle, damage_dealt, damage_received