#soal nomor 4

angka = float(input("Panjang gelombang cahaya (nm) : "))

if angka>=380 and angka<450:
  string= "violet" 
elif angka>=450 and angka<495:
  string= "blue" 
elif angka>=495 and angka<570:
  string= "green" 
elif angka>=570 and angka<590:
  string= "yellow" 
elif angka>=590 and angka<620:
  string= "orange" 
elif angka>=620 and angka<=750:
  string= "red"  
else:
  string= "input diluar spektrum yang diketahui"

print("spektrum yang terlihat : " + string)
