from src.A_AddOns import *

# Fungsi logout
def logout(login_state):
    # Lakukan login terlebih dahulu
    if login_state:
        print("Anda berhasil ...")
        print(text_ascii['logout'])
        return True
    else:
        print("Anda tidak berhasil logout.")
        return False