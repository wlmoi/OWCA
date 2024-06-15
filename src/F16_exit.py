from src.A_AddOns import *
from src.F15_Save import *

def exit(bigdata):
    valid = False
    while valid == False:
        print(text_ascii['exit'])
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if simpan.lower() == 'y':
            save(bigdata)
            valid = True
        elif simpan.lower() == 'n' :
            valid = True
        else:
            valid = False