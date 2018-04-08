# Merupakan sebuah program untuk menentukan biaya parkir 
# yang dihitung berdasarkan lama parkir .
# Biaya Parkir 2 jam pertama 2000 per jam berikutnya 500.
def program():
	# print ("*") * 50
	# print ("*      Selamat Datang di Aplikasi Parkir 	 *")
	# print ("*               MALL marimas                     *")
	print ("*") * 50
	platno=(input("*	Masukan No. plat 	: "))
	jam=int(input("*	Masuk Jam 		: "))
	menit=int(input("*	     Menit		: "))
	detik=int(input("*	     Detik		: "))
	t1=menit/60
	t2=detik/60
	totalmasuk=jam+t1+t2
	wktmasuk=totalmasuk
	print("-") * 50
	jam2=int(input("keluar Jam 		: "))
	menit2=int(input("     Menit		: "))
	detik2=int(input("     Detik		: "))
	t3=menit2/60
	t4=detik2/60
	totalkeluar=jam2+t3+t4
	wktkeluar=totalkeluar
	totalwaktu=wktkeluar-wktmasuk
	if(wktkeluar >= wktmasuk):
		jumlah=wktkeluar-wktmasuk
	else :
		jumlah=(12-wktkeluar)-wktmasuk
	if(jumlah > 2):
		biaya=2000+((jumlah-2)*500)
	else:
		biaya=2000
	print ("*") * 50
	print "Jam Masuk 		: ",jam,":",menit,":",detik
	print "Jam Keluar 		: ",jam2,":",menit2,":",detik2
	print "total waktu parkir 	: ",totalwaktu
	print "Biaya Parkir Kendaraan adalah Rp = ",biaya
	print ("*") * 50
	menu()
def menu() :
	print ("#") * 50
	print ("#      Selamat Datang di Aplikasi Parkir 	 #")
	print ("#               MALL marimas                     #")
	print ("#") * 50
	print "# 		1. Masuk 			 #"
	print "# 		2. keluar 			 #"
	print "." *50
	pilih=int(input("	masukan pilihan  (1/2) : "))
	print "\n"

	if(pilih == 1):
		program()
	else:
	 	stop=True

menu()

