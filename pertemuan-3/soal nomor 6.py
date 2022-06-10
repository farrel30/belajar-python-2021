#soal nomor 6
# input 0, akan keluar dari loop
counter = 0
total = 0
num = float(input("masukkan angka : "))
while num != 0:
  counter += 1
  total += num
  num = float(input("masukkan angka : "))
if counter ==0:
    counter = 1

print("rata rata : ", round(total/counter, 2))
