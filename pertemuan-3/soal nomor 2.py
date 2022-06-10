#soal nomor 2
number = {
     '3' : 'tiga' ,
     '4' : 'empat',
     '5' : 'lima',
     '6' : 'enam',
     '7' : 'tujuh',
     '8' : 'delapan',
     '9' : 'sembilan',
    '10' : 'sepuluh'
}
sisi = input('masukkan jumlah sisi :')
if sisi in number:
  ubah = ''.join(number[i] for i in sisi.split())
  print("itu adalah bentuk segi"+ubah) 

else : 
  print("maaf, ilmu saya belum sampai situ")
