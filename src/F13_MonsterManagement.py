from src.A_Functions import *
import typing

def MonsterManagement(bigdata: dict):
    ClearScreen()
    print(text_ascii['monster'])
    while True:
        print("\n====================================================")
        print("1. Tampilkan semua Monster")
        print("2. Tambah Monster baru")
        print("3. Keluar")
        while True:
            choice: any = input(">>> Pilih Aksi: ")
            if ManualIsDigit(choice):
                choice = int(choice)
                break
            else:
                print("Oops, input salah!")

        if choice == 1:
            print("\nID | Type           | ATK Power | DEF Power | HP   ")
            print("====================================================")
            for monster in bigdata['monster'][1:]:
                print(f"{monster['id']:>2} | {monster['type']:<14} | {monster['atk_power']:>9} | {monster['def_power']:>9} | {monster['hp']:>4}")
        elif choice == 2:
            print("Mulai pembuatan monster!!")
            available_type = []
            for monster in bigdata['monster'][1:]:
                available_type.append(monster['type'])
            monster_type = input("Masukkan nama monster: ")
            if monster_type in available_type:
                print("Nama sudah terdaftar, coba lagi!")
            else:
                while True:
                    monster_atk = input(">>> Masukkan ATK Power: ")
                    if ManualIsDigit(monster_atk):
                        monster_atk = int(monster_atk)
                        break
                    else:
                        print("Oops, input salah!")

                while True:
                    monster_def = input(">>> Masukkan DEF Power: ")
                    if ManualIsDigit(monster_def):
                        monster_def = int(monster_def)
                        break
                    else:
                        print("Oops, input salah!")
                
                while (monster_def < 0) or (monster_def > 50):
                    print("DEF Power harus bernilai 0-50, coba lagi!")
                    monster_def = input(">>> Masukkan DEF Power: ")
                    monster_def = int(monster_def)

                while True:
                    monster_hp = input(">>> Masukkan HP: ")
                    if ManualIsDigit(monster_hp):
                        monster_hp = int(monster_hp)
                        break
                    else:
                        print("Oops, input salah!")

                print("Monster baru berhasil dibuat")
                new_monster = {
                    'id' : (bigdata['monster'][-1]['id'] + 1),
                    'type': monster_type,
                    'atk_power' : monster_atk,
                    'def_power' : monster_def,
                    'hp'        : monster_hp,
                }
                confirmation = input(">>> Tambahkan Monster ke database (Y/N): ")
                if confirmation == 'Y':
                    bigdata['monster'].append(new_monster)
                elif confirmation == 'N':
                    print("Monster gagal ditambahkan")
        elif choice == 3:
            return bigdata
        else:
            ClearScreen()