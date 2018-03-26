# Merupakan sebuah program untuk menentukan biaya parkir 
# yang dihitung berdasarkan lama parkir .
# Biaya Parkir 2 jam pertama 2000 per jam berikutnya 500.

print ("Selamat Datang di Aplikasi Parkir")
platno=(input("Masukan Plat Nomor Kendaraan contoh ('B1234KK') = "))
wktmasuk=int(input("Masukan Jam Masuk Kendaraan = "))
wktkeluar=int(input("Masukkan Jam Keluar Kendaraan = "))
if(wktkeluar >= wktmasuk):
	jumlah=wktkeluar-wktmasuk
else :
	jumlah=(12-wktkeluar)-wktmasuk
if(jumlah > 2):
	biaya=2000+((jumlah-2)*500)
else:
	biaya=2000
print("Biaya Parkir Kendaraan adalah Rp = ",biaya)

