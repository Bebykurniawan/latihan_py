# READLINES ->
file = open("catatan.txt","r")
teks = file.readlines()
print(teks[0])
print(teks[1])
file.close()

# READ FILE ->
file = open("catatan.txt","r")
print(file.read())
file.close()

# WRITE FILE ->
list = ["Tirta Tukam \n", "Jhuanes Php \n", "Vianok \n", "Julian \n"]
file = open("data.txt","w")
file.writelines(list)
file.close()

# write txt dengan input data
print("======================")
print("      DATA SISWA")
print("======================")

nama = input("Nama : ")
kelas = input("Kelas : ")
alamat = input("Alamat : ")

teks = "\nNama : {nama}\n Kelas: {kelas}\n Alamat : {alamat}".format(nama=nama,kelas=kelas,alamat=alamat)
file_data = open("biodata.txt","a")
file_data.write(teks)
file_data.close()
