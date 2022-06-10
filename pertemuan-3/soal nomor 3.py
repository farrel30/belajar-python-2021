#soal nomor 3
angka = float(input("kekuatan gempa (Magnitude) : "))
if angka < 2:
  string = "micro"
elif angka>=2 and angka<3:
  string= "very minor" 
elif angka>=3 and angka<4:
  string= "minor" 
elif angka>=4 and angka<5:
  string= "light" 
elif angka>=5 and angka<6:
  string= "moderate" 
elif angka>=6 and angka<7:
  string= "strong" 
elif angka>=7 and angka<8:
  string= "major" 
elif angka>=8 and angka<10:
  string= "great" 
else:
  string= "meteoric"

print("gempa tersebut gempa jenis " + string)
