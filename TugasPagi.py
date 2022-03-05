pesan = True
mnm = 0
mkn = 0


struk = open('struk.txt','w')
struk.write('''====- STRUK BELANJAAN ANDA =====\n''')
struk.close()

def total():
  return mkn + mnm

def kembalian(uang):
    angsul = uang - total()
    return angsul


while (pesan):
  print("\nSilahkan Pilih Menu yang Anda inginkan")
  food = int(input("Masukkan kode Makanan (1-5): "))
  if food == 1:
    mkn += 2000
    a = "Pisang Goreng"
    an = 2000
  elif food == 2:
    mkn += 1000
    a = "Tempa Mendoan"
    an = 1000
  elif food == 3:
    mkn += 5000
    a = "Indomie Goreng"
    an = 5000
  elif food == 4:
    mkn += 6000
    a = "Indomie Rebus"
    an = 6000
  elif food == 5:
    mkn += 3000
    a = "Nasi Kucing"
    an = 3000
  else:
    continue

  drink = int(input("Masukkan kode Minuman (1-5): "))
  if drink == 1:
    mnm += 5000
    b = "Kopi Tubruk"
    bn = 5000
  elif drink == 2:
    mnm += 8000
    b = "Wedang Ronde"
    bn = 8000
  elif drink == 3:
    mnm += 6000
    b = "Susu Jahe"
    bn = 6000
  elif drink == 4:
    mnm += 4000
    b = "Susu Hangat"
    bn = 4000
  elif drink == 5:
    mnm += 3000
    b = "Teh Tawar"
    bn = 3000   
  else:
    continue

  print("Total Belanja: ", total())
  
  textstruk = a, an, b, bn
  conv = str(textstruk)

  struk = open("struk.txt", "a")
  struk.write(conv)
  struk.close()

  pesan = input("\nMau tambah pesanan lagi? (y/n)")
  if pesan == "n":
    pesan = False
  elif pesan =="y":
    pesan == True
  else:
    print("Masukkan pilihan yang sesuai (y or n)")
    pass

uang = int(input("Masukkan Uang Anda: "))
kembalian(uang)

struk = open("struk.txt", "a")
struk.write(str(total()))
struk.write(str(uang))
struk.write(str(kembalian(uang)))
struk.close()