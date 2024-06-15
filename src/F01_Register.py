from src.A_AddOns import *

# Registrasi
def Registrasi(bigdata):
    print()
    print(text_ascii['register'])
    print('{:^80s}'.format("="*80))
    print()

    data = [[value for value in user.values()] for user in bigdata['user']]
    monster_data = [[value for value in user.values()] for user in bigdata['monster']]

    while True:
        usernamePendaftar = input("Masukkan username : ")
        passwordPendaftar = input("Masukkan password : ")
        if PeriksaUsernameUnik(data, usernamePendaftar) == False:
            # Memeriksa ketentuan username
            print("Username", usernamePendaftar, "sudah terpakai! Silakan isi ulang form dengan username lain.")
            print()
        else:
            PeriksaKPassword(bigdata, usernamePendaftar, passwordPendaftar, monster_data, data)
            print(bigdata['user'])
            return bigdata

# Fungsi untuk memeriksa apakah username sudah terpakai
def PeriksaUsernameUnik(data, usernamePendaftar):
    for row in data:
        if len(row) >= 2 and usernamePendaftar == row[1]: # Kolom 1 untuk username
            return False  # Tandai bahwa username tidak unik
    return True  # Tandai bahwa username unik


# Fungsi untuk memeriksa ketentuan username
def PeriksaKUsername(bigdata, usernamePendaftar, passwordPendaftar, monster_data, data):
    # Memeriksa apakah username mengandung karakter yang diizinkan
    if all(char.isalnum() or char in '_-' for char in usernamePendaftar):
        # Menambahkan akun baru
        bigdata = TambahAkunBaru(bigdata, usernamePendaftar, passwordPendaftar, monster_data, data)
    else:
        print("Username hanya dapat mengandung huruf alfabet (A-Za-z), underscore (_), strip (-), dan angka (0-9). Silakan isi ulang form dengan username yang sesuai.")
        Registrasi(bigdata)

# Fungsi untuk memeriksa ketentuan password
def PeriksaKPassword(bigdata, usernamePendaftar, passwordPendaftar, monster_data, data):
    # Memeriksa apakah password memiliki panjang minimal 8 karakter
    if len(passwordPendaftar) >= 8:
        # Memeriksa apakah password mengandung setidaknya satu huruf besar, satu huruf kecil, dan satu angka
        if any(char.isupper() for char in passwordPendaftar) and any(char.islower() for char in passwordPendaftar) and any(char.isdigit() for char in passwordPendaftar):
            # Memeriksa apakah password tidak mengandung username
            if usernamePendaftar not in passwordPendaftar:
                # Memeriksa apakah password mengandung karakter yang diizinkan
                if all(char.isalnum() or char in '_-' for char in passwordPendaftar):
                    # Memeriksa apakah password tidak berisi spasi
                    if ' ' not in passwordPendaftar:
                        # Menjalankan fungsi untuk memeriksa username
                        PeriksaKUsername(bigdata, usernamePendaftar, passwordPendaftar, monster_data, data)
                    else:
                        print("Password tidak boleh mengandung spasi. Silakan isi ulang form dengan password yang sesuai.")
                        Registrasi(bigdata)
                else:
                    print("Password hanya dapat mengandung huruf alfabet (A-Za-z), underscore (_), strip (-), dan angka (0-9). Silakan isi ulang form dengan password yang sesuai.")
                    Registrasi(bigdata)
            else:
                print("Password tidak boleh mengandung username. Silakan isi ulang form dengan password yang sesuai.")
                Registrasi(bigdata)
        else:
            print("Password harus terdiri dari setidaknya satu huruf besar (A-Z), satu huruf kecil (a-z), dan satu angka (0-9). Silakan isi ulang form dengan password yang sesuai.")
            Registrasi(bigdata)
    else:
        print("Password harus memiliki panjang minimal 8 karakter. Silakan isi ulang form dengan password yang sesuai.")
        Registrasi(bigdata)


# Fungsi untuk memilih monster
def PilihMonster(monster_data):
    while True:
        print("Silahkan pilih salah satu monster sebagai monster awalmu.")
        print("1. Pikachow")
        print("2. Bulbu")
        print("3. Zeze")
        print("4. Zuko")
        print("5. Chacha")
        pilihan = ""
        while pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4" and pilihan != "5":
          pilihan = input("Monster Pilihanmu: ")
          if pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4" and pilihan != "5":
            print("Ulangi Input!")
        b = int(pilihan)
        if pilihan.isdigit() and 1 <= int(pilihan) <= len(monster_data) - 1:
          monster_id = int(pilihan)
          monster_type = monster_data[monster_id][1]
          monster_atk_power = monster_data[monster_id][2]
          monster_def_power = monster_data[monster_id][3]
          monster_hp = monster_data[monster_id][4]
          if b == 1:
            print(monster_ascii['Pikachow'])
          if b == 2:
              print(monster_ascii['Bulbu'])
          if b == 3:
            print(monster_ascii['Zeze'])
          if b == 4:
           print(monster_ascii['Zuko'])
          if b == 5:
            print(monster_ascii['Chacha'])
  
          print("Anda memilih monster dengan detail sebagai berikut:")
          print("Type:", monster_type)
          print("ATK Power:", monster_atk_power)
          print("DEF Power:", monster_def_power)
          print("HP:", monster_hp)
          a = input("Kamu yakin memilih monster ini? (y/n) ")
          if a == "y":
            return int(pilihan)
          elif a == "n":
            print("Silahkan Pilih lagi!")
            print()
          else:
            print("invalid input, pilih lagi!!")
        else:
            print("ID monster tidak valid. Silakan pilih lagi!")


# Fungsi untuk menambahkan akun baru ke dalam data
def TambahAkunBaru(bigdata, usernamePendaftar, passwordPendaftar, monster_data, data):
    # Menemukan ID terakhir dan menambahkannya satu angka di atasnya
    id_akhir = data[-1]
    last_id = int(data[-1][0])
    new_id = last_id + 1

    # Memilih monster
    monster_id = PilihMonster(monster_data)
    monster_type = monster_data[monster_id][1]

    # Menampilkan informasi registrasi
    print("Registrasi berhasil untuk username", usernamePendaftar, "dengan monster", monster_type)
    data_user = {
        'id'        : new_id,
        'username'  : usernamePendaftar,
        'password'  : passwordPendaftar,
        'role'      : 'agent',
        'oc'        : 0,
    }
    data_monster = {
       'user_id'    : new_id,
       'monster_id' : monster_id,
       'level'      : 1,
    }
    # Menyimpan perubahan ke file CSV
    bigdata['monster_inventory'].append(data_monster)
    bigdata['user'].append(data_user)
    return bigdata