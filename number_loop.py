print("===== CALCULATOR =====")
print("+ = plus\n- = minus\n* = kali\n/ = bagi\nkeluar")

status = input("status mesin: ")

while status == "on":
    while status== "off":
        break
    operator = input("nilai operator: ").lower()
    if operator == "plus" :
        angka1 = int(input("masukan nilai angka: "))
        angka2 = int(input("masukan nilai angka: "))
        hasil = angka1 + angka2
        print("hasilnya adalah: ", hasil)
    elif operator == "minus":
        angka1 = int(input("masukan nilai angka: "))
        angka2 = int(input("masukan nilai angka: "))
        hasil = angka1 - angka2
        print("hasilnya adalah: ", hasil)
    elif operator == "kali":
        angka1 = int(input("masukan nilai angka: "))
        angka2 = int(input("masukan nilai angka: "))
        hasil = angka1 * angka2
        print("hasilnya adalah: ", hasil)
    elif operator == "bagi":
        angka1 = int(input("masukan nilai angka: "))
        angka2 = int(input("masukan nilai angka: "))
        hasil = angka1 // angka2
        print("hasilnya adalah: ", hasil)       
    elif operator == "keluar":
        break