#soal nomor 7
n = int(input("masukkan jumlah anggota : "))
biaya = 0
for i in range(n):
  usia = int(input("masukkan usia : "))
  if usia < 2 : 
    biaya +=0
  elif usia >2 and usia <= 12:
    biaya += 14
  elif usia > 65:
    biaya += 18
  else : 
    biaya += 23  
print(biaya)
