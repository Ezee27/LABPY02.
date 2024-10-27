# Program Kalkulator Sederhana

# Meminta input angka dan operator dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

# Menentukan operasi berdasarkan operator
if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Tidak bisa membagi dengan nol"
else:
    hasil = "Operator tidak valid"

# Menampilkan hasil
print(f"Hasil: {hasil}")
