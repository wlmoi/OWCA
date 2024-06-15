from src.A_Functions import *
from src.A_AddOns import *
import os
import sys
import time
import argparse
import typing

def CariFolder(nama_folder,address):
    # {Fungsi ini mencari folder pada direktori}
    if nama_folder == '':
        print(f'Tidak ada nama folder yang diberikan!')
        return(False)
    else:
        if os.path.exists(address):
            return(True)
        else: 
            print(f'\nFolder "{nama_folder}" tidak ditemukan.')
            return(False)

def Load():
    parser = argparse.ArgumentParser() # membuat argument
    parser.add_argument('folder_simpan', help='folder tempat tersimpan')
    args = parser.parse_args() # wadah argumen
    address = os.getcwd() ;'?' ; args.folder_simpan
    xtrapath = sys.argv[1]

    # validasi address
    valid = False
    valid = CariFolder(args.folder_simpan,address)
    if valid : # jika folder address ada
        print(text_ascii['loading1'])
        time.sleep(0.5)
        ClearScreen()
        print(text_ascii['loading2'])
        time.sleep(0.5)
        ClearScreen()
        print(text_ascii['loading3'])
        time.sleep(0.5)
        ClearScreen()
        print(text_ascii['loading4'])
        time.sleep(0.5)
        print()
        #membuat bigdata
        bigdata : dict = {'user' : [],
                          'monster': [],
                          'monster_shop' :[],
                          'monster_inventory':[],
                          'item_shop' : [],
                          'item_inventory' : []}
        bigdata['user'] = AmbilData(address + '/data/' + xtrapath + '/user.csv')
        bigdata['monster'] = AmbilData(address + '/data/' + xtrapath + '/monster.csv')
        bigdata['monster_shop'] = AmbilData(address + '/data/' + xtrapath + '/monster_shop.csv')
        bigdata['monster_inventory'] =AmbilData(address + '/data/' + xtrapath + '/monster_inventory.csv')
        bigdata['item_shop']= AmbilData(address + '/data/' + xtrapath + '/item_shop.csv')
        bigdata['item_inventory'] = AmbilData(address + '/data/' + xtrapath + '/item_inventory.csv')
        return (True,bigdata)
    else: # jika masukan kosong
        print("Tidak ada nama folder yang diberikan!")
        return(False,{})