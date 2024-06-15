from src.A_AddOns import *

def Help2(status: dict):
    print(text_ascii['help'])
    if not status['status']:
        print("============================")
        print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
        print("1. Login: Masuk ke dalam akun yang sudah terdaftar")
        print("2. Register: Membuat akun baru")
        choice = input(">>> ")
        return choice
    
    elif status['role'] == 'admin':
        print(f"============================\nHalo Admin. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:") 
        print("1. Logout: Keluar dari akun yang sedang digunakan")
        print("2. Monster: Mengatur Monster")
        print("3. Shop: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
        choice = input(">>> ")
        return choice

    else:
        print(f"=============================\nHalo Agent. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:") 
        print("1. Logout: Keluar dari akun yang sedang digunakan")
        print("2. Monster: Melihat owca-dex yang dimiliki oleh Agent")
        choice = input(">>> ")
        return choice
