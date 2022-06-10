#Soal Nomor 1
# For loop
b = []
n = int(input("Berapa angka yang ingin dimasukkan ? "))
for i in range(1, n+1):
  angka = int(input("masukkan angka : "))
  if angka != 0 :
    b.append(angka)

b = sorted(b)
print(b)

######
#While Loop

b = []
while True : 
  angka = input("masukkan angka : ")
  if angka == '' :
    break
  elif angka!= '0' :
    b.append(int(angka))
b = sorted(b)
print(b)
