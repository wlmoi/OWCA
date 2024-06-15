from src.A_AddOns import *

# Fungsi untuk mendapatkan role
def get_user_role(bigdata, username):
    # Memuat data pengguna dari file CSV
    user_data = [[value for value in user.values()] for user in bigdata['user']]

    # Mencari peran pengguna berdasarkan username
    for user in user_data:
        if len(user) >= 4:  # Pastikan ada cukup banyak kolom dalam baris pengguna
            if username == user[1]:
                return user[3]  # Mengembalikan peran pengguna

    # Jika username tidak ditemukan, kembalikan None
    return None

def get_user_id(bigdata, username):
    # Memuat data pengguna dari file CSV
    user_data = [[value for value in user.values()] for user in bigdata['user']]

    # Mencari id pengguna berdasarkan username
    for user in user_data:
        if len(user) >= 4:  # Pastikan ada cukup banyak kolom dalam baris pengguna
            if username == user[1]:
                return user[0]  # Mengembalikan id pengguna

    # Jika username tidak ditemukan, kembalikan None
    return None

# Fungsi untuk mengenkripsi password
def enkripsi_password(password):
    # Inisialisasi string kosong untuk password yang dienkripsi
    encrypted_password = ""
    # Alfabet kecil dan besar sebagai referensi
    alfabet_kecil = 'abcdefghijklmnopqrstuvwxyz'
    alfabet_besar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Loop melalui setiap karakter dalam password
    for i in range(len(password)):
        char = password[i]
        # Jika karakter adalah huruf kecil
        if char.islower():
            # Cari posisi karakter dalam alfabet kecil
            posisi = alfabet_kecil.find(char)
            # Hitung posisi baru setelah pergeseran 3
            posisi_baru = (posisi + 3) % 26
            # Tambahkan karakter yang telah dienkripsi ke hasil
            encrypted_password += alfabet_kecil[posisi_baru]
        # Jika karakter adalah huruf besar
        elif char.isupper():
            # Cari posisi karakter dalam alfabet besar
            posisi = alfabet_besar.find(char)
            # Hitung posisi baru setelah pergeseran 3
            posisi_baru = (posisi + 3) % 26
            # Tambahkan karakter yang telah dienkripsi ke hasil
            encrypted_password += alfabet_besar[posisi_baru]
        else:
            # Jika karakter bukan huruf alfabet, tambahkan tanpa enkripsi
            encrypted_password += char
    
    # Mengembalikan password yang telah dienkripsi
    return encrypted_password

# Fungsi untuk mendekripsi password
def dekripsi_password(encrypted_password):
    # Inisialisasi string kosong untuk password yang didekripsi
    decrypted_password = ""
    # Alfabet kecil dan besar sebagai referensi
    alfabet_kecil = 'abcdefghijklmnopqrstuvwxyz'
    alfabet_besar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Loop melalui setiap karakter dalam password yang dienkripsi
    for i in range(len(encrypted_password)):
        char = encrypted_password[i]
        # Jika karakter adalah huruf kecil
        if char.islower():
            # Cari posisi karakter dalam alfabet kecil
            posisi = alfabet_kecil.find(char)
            # Hitung posisi baru setelah pergeseran 3 ke kiri
            posisi_baru = (posisi - 3) % 26
            # Tambahkan karakter yang telah didekripsi ke hasil
            decrypted_password += alfabet_kecil[posisi_baru]
        # Jika karakter adalah huruf besar
        elif char.isupper():
            # Cari posisi karakter dalam alfabet besar
            posisi = alfabet_besar.find(char)
            # Hitung posisi baru setelah pergeseran 3 ke kiri
            posisi_baru = (posisi - 3) % 26
            # Tambahkan karakter yang telah didekripsi ke hasil
            decrypted_password += alfabet_besar[posisi_baru]
        else:
            # Jika karakter bukan huruf alfabet, tambahkan tanpa dekripsi
            decrypted_password += char
    
    # Mengembalikan password yang telah didekripsi
    return decrypted_password


# Fungsi untuk login
def login(bigdata):
    print(text_ascii['login'])
    user_data = {"user_id"  : None,
                 "username" : None,
                 "role"     : None,
                 "status"   : False}
    
    usernamePengguna = input("Masukkan username : ")
    passwordPengguna = input("Masukkan password : ")

    matriks_user = [[value for value in user.values()] for user in bigdata['user']]

    check_username = False
    check_pw = False
    
    for user in matriks_user:
        if len(user) >= 3:  # Pastikan ada cukup banyak kolom dalam baris data yang diberikan
            if usernamePengguna == user[1]:
                check_username = True
                if passwordPengguna == user[2]:
                    check_pw = True
                    break

    if not check_username:
        print("Username salah")
        return user_data
    
    elif not check_pw:
        print("Password salah")
        return user_data
    
    else:
        user_data['user_id'] = int(get_user_id(bigdata, usernamePengguna))
        user_data['username'] = usernamePengguna
        user_data['role'] = get_user_role(bigdata, usernamePengguna)
        user_data['status'] = True
        print("Login berhasil!")
        return user_data