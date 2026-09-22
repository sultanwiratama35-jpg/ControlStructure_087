# Meminta user memasukkan nilai dalam bentuk persen
nilai = float(input("Masukkan nilai Anda (%): "))

# Mengecek apakah nilai 90 atau lebih
if nilai >= 90:
    print("Excellent performance")

# Jika tidak mencapai 90, cek apa nilai 80 atau lebih
elif nilai >= 80:
    print("Very Good performance")

# Jika tidak mencapai 80, cek apa nilai 70 atau lebih
elif nilai >= 70:
    print("Good performance")

# Jika tidak mencapai 70, cek apakah nilai 60 atau lebih
elif nilai >= 60:
    print("Average performance")

# Jika nilai kurang dari 60
else:
    print("Below average performance")