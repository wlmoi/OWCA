from src.A_Functions import *
from src.F07_Inventory import UserInventory


def Laboratory(bigdata, user_id):
    # Initialize
    cost = [100, 300, 600, 1000]
    user_oc = bigdata['user'][user_id]['oc']
    ClearScreen()
    print(text_ascii['laboratory'])

    # print all monster
    user_monster = UserInventory(user_id, bigdata, 'monster_inventory')
    print("============ MONSTER LIST ============")
    counter = 0
    for monster in user_monster:
        counter = counter + 1
        print("%i. " %(counter)," Monster ID: ",monster['monster_id'], ", level: ", monster['level'])
    
    # print cost
    print()
    print("1. Level 1 -> Level 2: 100 OC")
    print("2. Level 2 -> Level 3: 300 OC")
    print("3. Level 3 -> Level 4: 600 OC")
    print("4. Level 4 -> Level 5: 1000 OC")
    print()

    # input monster
    choice = int(input("Monster ID\n>>> ")) - 1
    if choice > len(user_monster):
        print("Oops, input anda salah")
        time.sleep(2)
        return bigdata
    monster = user_monster[choice]
    upgrade_cost = cost[monster['level'] -1 ]
    if monster['level'] == 5:
        print("Maaf, monster yang Anda pilih sudah memiliki level maksimum")
    else:
        print(f"{monster['monster_id']} akan diupgrade menjadi level {monster['level'] + 1}")
        print(f"Harga untuk melakukan upgrade adalah {upgrade_cost}")
        confirmation = input(">>> Lanjutkan upgrade (Y/N): ")
        if confirmation == "Y" and user_oc >= upgrade_cost:
            monster['level'] += 1
            bigdata['user'][user_id]['oc'] -= upgrade_cost
            print("selamat kamu berhasil upgrade monstermu!")
        else:
            print("tidak berhasil")
    time.sleep(3)
    return bigdata