print("======================")
print("      DATA SISWA")
print("======================")

nama = input("Nama : ")
kelas = input("Kelas : ")
alamat = input("Alamat : ")

teks = "\nNama : {nama}\n Kelas: {kelas}\n Alamat : {alamat}".format(nama=nama,kelas=kelas,alamat=alamat)
file_data = open("biodata.txt","a") #todo: Mode write diganti menjadi Mode Append !
file_data.write(teks)
file_data.close()
