from src.A_Functions import *
from src.A_AddOns import *
from src.F08_Battle import *
import typing


def Arena(bigdata: dict, user_id: int) -> int:
    # Initialize
    ClearScreen()
    print(text_ascii['arena'])
    total_damage_dealt    : int  = 0
    total_damage_received : int  = 0
    time.sleep(2)
    status: int = 0
    total_oc = 0
    oc_per_stage = [30, 50, 100, 150, 200]

    # Mengulang 5 kali untuk tiap stage
    for stage in range(1, 6):
        print(f"WELCOME TO STAGE {stage}")
        time.sleep(3)

        # Memanggil fungsi Battle dengan setting in_arena = True
        win_battle, damage_dealt, damage_received = Battle(bigdata, user_id=user_id, in_arena= True, level_setting= stage)

        # Mengubah beberapa status data
        total_damage_dealt += damage_dealt
        total_damage_received += damage_received
        status = stage
        
        if not win_battle:
            break

        # Menambahkan oc jika memenangkan stage
        total_oc += oc_per_stage[stage-1]
    
    if win_battle:
        print("Selamat, Anda berhasil menyelesaikan seluruh stage Arena !!!")
    else:
        print(f"GAME OVER! Sesi latihan berakhir pada stage {status}!")

    # Menampilkan statistic arena
    print("============== STATS ==============")
    print(f"Jumlah hadiah   : {total_oc} OC")
    print(f"Jumlah stage    : {status}")
    print(f"Damage dealt    : {total_damage_dealt}")
    print(f"damage received : {total_damage_received}")
    time.sleep(5)
    return total_oc