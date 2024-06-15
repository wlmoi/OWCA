import typing
import datetime as time

def RNG(interval: int) -> int:
    # Fungsi untuk menghasilkan bilangan acak dalam rentang interval
    # seed, a, c, m, random_number = integer
    a = 16523
    c = 19623
    m = 999
    # Definisikan seed dengan nilai awal waktu (timestamp)
    seed = int(time.datetime.now().timestamp())
    # Menggunakan algoritma LCG untuk menghasilkan bilangan acak dalam rentang interval
    random_number = (((a * seed + c) % m) % interval) + 1
    return random_number