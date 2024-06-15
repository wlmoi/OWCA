# MAIN
# # Main merupakan program utama yang menerima input perintah lalu menjalankan fungsi berdasarkan perintah yang diinput
from src.A_Functions import *
from src.B04_Minigame import *
from src.B05_Peta_Kota_Danville import *
from src.F00_RNG import *
from src.F01_Register import *
from src.F02_Login import *
from src.F03_Logout import *
from src.F04_Help import *
from src.F05_Monster import *
from src.F06_Potion import *
from src.F07_Inventory import *
from src.F08_Battle import *
from src.F09_Arena import *
from src.F10_Shop_Currency import *
from src.F11_Laboratory import *
from src.F12_ShopManagement import *
from src.F13_MonsterManagement import *
from src.F14_Load import *
from src.F15_Save import *
from src.F16_Exit import * 

import typing
# * =- Import semuanya

def main():
    user_data: dict = {"user_id"  : None,
                       "username" : None,
                       "role"     : None,
                       "status"   : False}
    ClearScreen()
    loaded, bigdata = Load()
    if not loaded:
        return

    ClearScreen()
    print(text_ascii['welcome'])
    LoopBreaker = True
    while (LoopBreaker == True):
        choice = input(">>> ").upper()
        if choice == "REGISTER":
            ClearScreen()
            Registrasi(bigdata)
        elif choice == "LOGIN":
            if not user_data['status']:
                ClearScreen()
                user_data = login(bigdata)
                agent_position = (1,1)
                if user_data['status']:
                    loggedin = True
                    while loggedin:
                        condition, agent_position = peta_kota_danville(bigdata, user_data, agent_position)
                        if condition == "End":
                            break
                        elif condition == "Semak":
                            bigdata['user'][user_data['user_id']]['oc'] = Battle(bigdata, user_id=user_data["user_id"])
                        elif condition == "Arena":
                            bigdata['user'][user_data['user_id']]['oc'] = Arena(bigdata, user_id=user_data['user_id'])
                        elif condition == "Inventory":
                            ShowInventory(bigdata, user_id=user_data['user_id'])
                        elif (condition == "Shop") and (user_data['role'] == 'agent'):
                            bigdata = Shop(bigdata, user_id=user_data['user_id'])
                        elif (condition == "Shop") and (user_data['role'] == 'admin'):
                            bigdata = ShopManagement(bigdata)
                        elif condition == "Laboratorium":
                            bigdata = Laboratory(bigdata, user_id=user_data['user_id'])
                        elif (condition == "Monster") and (user_data['role'] == 'admin'):
                            bigdata = MonsterManagement(bigdata)
                        elif (condition == "Minigame"):
                            bigdata = Minigame(bigdata, user_id=user_data['user_id'])
                        elif (condition == "Logout"):
                            logout(user_data['status'])
                            user_data = {"user_id"  : None,
                                         "username" : None,
                                         "role"     : None,
                                         "status"   : False}
                            break
                        
            else:
                print("Kamu sudah login")
                
        elif choice == "HELP":
            ClearScreen()
            Help2(user_data)
        elif choice == "EXIT":
            ClearScreen()
            LoopBreaker = False
            print(text_ascii['exit'])
            print("Apakah anda ingin melakukan penyimpanan?")
            ans = input(("Y/N: ")).upper()
            if(ans == "N"):
                print("Terima kasih karena anda telah memainkan game ini! Sampai jumpa! ╲⎝⧹ ( ͡° ͜ʖ ͡°) ⎠╱")
            elif(ans == "Y"):
                save(bigdata)
        elif choice == "LOGOUT":
            if logout(login_state= user_data["status"]):
                user_data = {"user_id"  : None,
                             "username" : None,
                             "role"     : None,
                             "status"   : False}
                
if __name__ == '__main__':
    main()