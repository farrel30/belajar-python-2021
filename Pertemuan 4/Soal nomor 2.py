#Soal Nomor 2
# For loop
c = []
n = int(input("Berapa angka yang ingin dimasukkan ? "))
for i in range(1, n+1):
  angka = int(input("masukkan angka : "))
  if angka != 0 :
    c.append(angka)

c = sorted(c, reverse=True)
print(c)



#While Loop
b = []
while True : 
  angka = input("masukkan angka : ")
  if angka == '' :
    break
  elif angka!= '0' :
    b.append(int(angka))
b = sorted(b, reverse=True)
print(b)
