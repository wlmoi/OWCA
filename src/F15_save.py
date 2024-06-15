import os
import time

def tulis_csv(data, folder, file):
    with open(os.path.join(folder, file), "w") as f:
        if data:
            for row in data:
                f.write(';'.join(map(str, row.values())) + '\n')

def save(bigdata: dict):
    address = input('Masukkan nama folder: ')
    originalinput = address
    address = os.path.join("data", address)
    print()
    for i in range(4):
        print('Saving' + '.' * i, end='\r')
        time.sleep(0.5)

    if not os.path.exists(address):
        os.makedirs(address)
        for i in range(4):
            print('Membuat folder ' + originalinput + '.' * i, end='\r')
            time.sleep(0.5)

    # menyimpan data ke file
    tulis_csv(bigdata['user'], address, 'user.csv')
    tulis_csv(bigdata['monster'], address, 'monster.csv')
    tulis_csv(bigdata['monster_shop'], address, 'monster_shop.csv')
    tulis_csv(bigdata['monster_inventory'], address, 'monster_inventory.csv')
    tulis_csv(bigdata['item_shop'], address, 'item_shop.csv')
    tulis_csv(bigdata['item_inventory'], address, 'item_inventory.csv')
    print('\nData telah disimpan pada folder ' + originalinput + '!')