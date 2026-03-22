# Kalkulator Sederhana Python
# Mendukung +, -, *, /

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        raise ValueError("Pembagian dengan nol tidak diperbolehkan.")
    return a / b

def main():
    print("=== Kalkulator Sederhana ===")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    
    try:
        pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
        if pilihan not in (1, 2, 3, 4):
            print("Pilihan tidak valid.")
            return
        
        # Input angka
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        
        # Proses perhitungan
        if pilihan == 1:
            hasil = tambah(a, b)
            simbol = "+"
        elif pilihan == 2:
            hasil = kurang(a, b)
            simbol = "-"
        elif pilihan == 3:
            hasil = kali(a, b)
            simbol = "*"
        elif pilihan == 4:
            hasil = bagi(a, b)
            simbol = "/"
        
        print(f"Hasil: {a} {simbol} {b} = {hasil}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
