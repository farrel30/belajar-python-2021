#Soal Nomor 5
a = []
b = []
while True:
  string = input("masukkan kata : ") 
  if string == '':
    break
  else : 
    if len(string) >= 2:
      a.append(string)
      b.append(len(string))
    
print(a)
print(b) #list untuk banyaknya huruf pada string
print("banyaknya kata yg lebih dari 2 huruf : ", len(a))
