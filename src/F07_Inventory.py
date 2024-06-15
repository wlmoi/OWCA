from src.A_Functions import *
from src.F05_Monster import *
import typing

def DisplayMonsterStat(monster_data: dict, monster_level: int) -> None:
    print("Name      :", monster_data["type"])
    print("ATK Power :", monster_data["atk_power"])
    print("DEF Power :", monster_data["def_power"])
    print("HP        :", monster_data["hp"])
    print("Level     :", monster_level)
    return


def ShowInventory(bigdata, user_id) -> None:
    inventory: dict = (InventoryUserDict(bigdata, user_id= user_id))
    data_monster = inventory['monster']
    data_item = inventory['item']
    counter: int = 1
    ClearScreen()
    print(text_ascii['inventory'])

    inventory_2: list = []
    for i in range(len(data_monster)):
        temp = ['monster']
        for values in inventory['monster'][i].values():
            if values != 'user_id':
                temp.append(values)
        inventory_2.append(temp)

    for i in range(len(data_item)):
        temp = ['item']
        for values in inventory['item'][i].values():
            if values != 'user_id':
                temp.append(values)
        inventory_2.append(temp)


    print(f"============== Inventory User: {user_id} ==============")
    # Print Monster in Inventory
    banyak_monster = len(inventory['monster'])
    for i in range(banyak_monster):
        print(counter, end=") Monster       | ")
        for key, values in inventory['monster'][i].items():
            if key != 'user_id':
                print(key, ':', values, end=", ")
        print()
        counter += 1

    # Print Item in Inventory
    banyak_item = len(inventory['item'])
    for i in range(banyak_item):
        print(counter, end=") ")
        if inventory['item'][i]['type'] == 'monsterball':
            print("Monsterball   ", end="| ")
        else:
            print("Potion        ", end="| ")
        for key, values in inventory['item'][i].items():
            if key != 'user_id':
                print(key, ':', values, end=", ")
        print()
        counter += 1

    # checking to show detail item
    print("===============================================")
    print("Ketikkan id untuk menampilkan item:")
    id = input(">>> ").upper()

    while id != "KELUAR":
        if id.isdigit():
            DetailItem(bigdata, int(id), inventory_2)
        print("Ketikkan id untuk menampilkan item:")
        id = input(">>> ").upper()
        if id == "KELUAR":
            break
    return

# Use Case
# ShowInventory(bigdata, 3)


def DetailItem(bigdata: dict, item_id: int, inventory: dict):
    # Mencari value dari tiap item/monster
    banyak_id: int = len(inventory)
    if 0 < item_id <= banyak_id:
        if inventory[item_id-1][0] == 'monster':
            monster_data = MonsterDetail(bigdata, monster_id=inventory[item_id-1][2], level=inventory[item_id-1][3])
            DisplayMonsterStat(monster_data=monster_data, monster_level=inventory[item_id-1][2])
            print("\n")
        elif inventory[item_id-1][0] == 'item':
            if inventory[item_id-1][2] == 'monsterball':
                print(f"MonsterBall\nQuantity:  {inventory[item_id-1][1]}\n")
            else:
                print(f"Potion\nType       : {inventory[item_id-1][2]}\nQuantity   : {inventory[item_id-1][1]}\n")
    else:
        print("ID tidak tersedia")
    return


def InventoryUserDict(bigdata: dict, user_id: int) -> dict:
    data_monster: list = bigdata['monster_inventory']
    data_item: list = bigdata['item_inventory']
    inventory: dict = {'monster' : [], 'item' : [],}
    for i in range(1, len(data_monster)):
        if int(data_monster[i]['user_id']) == user_id:
            inventory['monster'].append(data_monster[i])
    
    for i in range(1, len(data_item)):
        if int(data_item[i]['user_id']) == user_id:
            inventory['item'].append(data_item[i])
    # print(inventory)
    return inventory

def UserInventory(user_id: int, bigdata: dict, type: str) -> list:
    data = bigdata[type][1:]
    list_item = []
    for i in data:
        if int(i['user_id']) == user_id:
            temp = i
            list_item.append(temp)
    return list_item

# Use Case
# UserInventory(3, bigdata, 'monster_inventory')