a = float (input("Masukkan angka pertama: "))
b= float (input("Masukkan angka kedua: "))
c = float (input("Masukkan angka ketiga: "))

if a > b and a > c:
    largest = a
    print("Angka pertama adalah yang terbesar", largest)
elif b > a and b > c:
    largest = b
    print("Angka adalah yang terbesar", largest)   
elif c > a and c > 2:
    largest = c
    print("Angka adalah yang terbesar", largest)     
else:
    print("Tidak ada angka yang terbesar")