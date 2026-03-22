import random

angka_rahasia = random.randint(1, 100)
percobaan = 0

print("=== GAME TEBAK ANGKA ===")
print("Tebak angka dari 1 sampai 100!")

while True:
    tebakan = int(input("Masukkan tebakanmu: "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print(f"🎉 Benar! Angkanya {angka_rahasia}")
        print(f"Kamu butuh {percobaan} percobaan")
        break
