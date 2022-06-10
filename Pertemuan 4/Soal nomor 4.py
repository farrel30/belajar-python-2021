#Soal Nomor 4
b = []
while True : 
  angka = input("masukkan angka : ")
  if angka == '':
    break
  else : 
    b.append(int(angka))
b = sorted(b)
print(b)
