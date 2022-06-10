#Soal nomor 3
a = []
while True:
  string = input("masukkan kata : ") 
  if string == '':
    break
  else : 
    a.append(string)
  a = sorted(set(a))
print(a, end=" ")
