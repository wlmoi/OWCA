from src.F05_Monster import *
from src.A_AddOns import *
from src.A_Functions import *
from src.F07_Inventory import *


def DisplayItems(bigdata: dict, item_type: str) -> None:
    # Jika ingin menampilkan 'monster'
    if item_type == "monster":
        
        monster_temp: list = bigdata['monster_shop'][1:]
        monster_shop: list = []
        
        # Mencari data stock dan price setiap monster
        for monster in monster_temp:
            # Mengambil MonsterDetail
            data: dict = MonsterDetail(bigdata, monster_id=monster['monster_id'])
            
            id_temp = data['id']
            for i in bigdata['monster_shop']:
                if i['monster_id'] == id_temp:
                    temp_index: int = bigdata['monster_shop'].index(i)
            
            data['stock'] = monster_temp[temp_index-1]['stock']
            data['price'] = monster_temp[temp_index-1]['price']

            # Memasukkan data setiap monster ke monster_shop
            monster_shop.append(data)

        # Menampilkan tabel 'monster' dari monster_shop
        print("ID | Type           | ATK Power | DEF Power | HP   | Stok | Harga")
        print("==================================================================")
        for monster in monster_shop:
            print(f"{monster['id']:>2} | {monster['type']:<14} | {monster['atk_power']:>9} | {monster['def_power']:>9} | {monster['hp']:>4} | {monster['stock']:>4} | {monster['price']:>6}")
    
    # Jika ingin menampilkan 'potion
    elif item_type == "potion":

        item_temp: list = bigdata['item_shop'][1:]
        item_shop: list = []

        # Mencari data potion
        for id in range(len(item_temp)):
            temp: dict = {'id' : id+1}
            temp.update(item_temp[id])
            # Memasukkan data setiap potion ke item_shop
            item_shop.append(temp)

        # Menampilkan tabel 'potion' dari item_shop
        print("ID | Type                 | Stok | Harga")
        print("=========================================")
        for potion in item_shop:
            if potion['stock'] > 0:
                print(f"{potion['id']:>2} | {potion['type']:<20} | {potion['stock']:>4} | {potion['price']:>5}")


def BuyItem(bigdata, user_id, item_type):
    # Input item_id
    item_id = InputVerifier("Masukkan id")

    # Mengambil data oc dari user_id
    oc = bigdata['user'][user_id]['oc']

    # Jika item_type 'monster'
    if item_type == "monster":
        # Cari monster yang sesuai dengan item_id
        monster: dict = next((m for m in bigdata['monster_shop'] if m['monster_id'] == item_id), None)

        # Jika monster ditemukan, oc memenuhi, dan stock memenuhi
        if monster and monster['stock'] > 0 and oc >= monster['price']:
            # Mengurangi stock dan oc user
            bigdata['monster_shop'][item_id]['stock'] -= 1
            bigdata['user'][user_id]['oc'] -= monster['price']

            # Mencari data dari monster
            monster_type: str = bigdata['monster'][monster['monster_id']]['type']
            temp: dict = {
                "user_id"    : user_id,
                "monster_id" : monster['monster_id'],
                'level'      : 1, }
            
            # Tambahkan monster yang dibeli ke inventory agen
            print(f"Berhasil membeli monster: {monster_type}. Monster sudah masuk ke inventory-mu!")
            bigdata['monster_inventory'].append(temp)
            return bigdata
        
        # Jika tidak ditemukan
        else:
            # Jika salah, berikan pesan error
            if not monster:
                print(f"Monster dengan ID {item_id} tidak ditemukan.")
            elif monster['stock'] <= 0:
                print(f"Monster {bigdata['monster'][monster['monster_id']]['type']} dengan ID {monster['monster_id']} tidak tersedia.")
            else:
                print(f"OC-mu tidak cukup untuk membeli monster {bigdata['monster'][monster['monster_id']]['type']}.")
            return bigdata

    # Jika item_type 'potion'
    elif item_type == "potion":
        # Input Quantity potion
        quantity: int = InputVerifier("Masukkan jumlah")

        # Cari potion yang sesuai dengan item_id
        potion: dict = bigdata['item_shop'][item_id]

        # Jika item ditemukan, oc memenuhi, dan stock memenuhi
        if potion and potion['stock'] >= quantity and oc >= potion['price'] * quantity:
            # Mengurangi stock dan oc user
            bigdata['user'][user_id]['oc'] -= potion['price'] * quantity
            potion['stock'] -= quantity

            # Tambahkan potion yang dibeli ke inventory agen
            add_potion: dict = next((p for p in bigdata['item_inventory'] if (p['user_id'] == user_id and p['type'] == potion['type'])), None)
            # Jika item sudah ada di inventory
            if add_potion:
                item_index: int = bigdata['item_inventory'].index(add_potion)
                bigdata['item_inventory'][item_index]['quantity'] += quantity
            # Jika item belum ada di inventory
            else:
                temp: dict = {
                    'user_id'   : user_id,
                    'type'      : potion['type'],
                    'quantity'  : quantity,
                }
                bigdata['item_inventory'].append(temp)
            print(f"Berhasil membeli item: {quantity} {potion['type']}. Item sudah masuk ke inventory-mu!")
        
        # Jika tidak ditemukan
        else:
            # Jika salah, berikan pesan error
            if not potion:
                print(f"Potion dengan ID {item_id} tidak ditemukan.")
            elif potion['stock'] < quantity:
                print(f"Stok potion {potion['type']} dengan ID {item_id} tidak mencukupi.")
            else:
                print(f"OC-mu tidak cukup untuk membeli {quantity} {potion['type']}.")


def Shop(bigdata, user_id):
    # Mengambil data oc dari user_id
    oc = bigdata['user'][user_id]['oc']

    ClearScreen()
    print(text_ascii['shop'])

    while True:
        # Menerima input action
        action = input("\nAKSI ( Lihat / Beli / Keluar )\n>>> ").upper()

        # Jika input salah
        if action not in ["LIHAT", "BELI", "KELUAR"]:
            print("Oops, input salah!")
        
        elif action == "LIHAT":
            item_type = input("\nLihat ( Monster / Potion )\n>>> ").lower()
            if item_type not in ["monster", "potion"]:
                print("Oops, input salah!")
            else:
                DisplayItems(bigdata, item_type)

        elif action == "BELI":
            item_type = input("\nBeli ( monster / potion )\n>>> ").lower()
            print(f"Jumlah O.W.C.A. Coin-mu sekarang: {oc}\n")
            if item_type not in ["monster", "potion"]:
                print("Oops, input salah!")
            else:
                BuyItem(bigdata, user_id, item_type)
    
        elif action == "KELUAR":
            print("Sampai belanja lagi!")
            break
    
    ClearScreen()
    return bigdata