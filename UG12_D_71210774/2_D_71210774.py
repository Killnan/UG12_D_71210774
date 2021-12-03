# Ronand Joy 71210774
# Soal 2

a = input("Hi Kiko, Silahkan Masukkan hari yang ingin Anda telusuri: ")
hari_1 = ("kelas ke-1 Algorima Graf","kelas ke-3 Sistem Operasi","kelas ke-4 PAK")
hari_2 = ("kelas ke-2 Matematika Teknik","kelas ke-4 Bhs Indonesia","kelas ke-6 PKN")
hari_3 = ("kelas ke-2 Sistem Basis Data","kelas ke-4 Praktikum Sistem Basis Data")
hari_4 = ("kelas ke-1 IMK","kelas ke-3 LogMat","kelas ke-4 Praktekkom")

if a == "senin" :
    for i in range(len(hari_1)):
        print(hari_1[i])
elif a == "selasa" :
    for i in range(len(hari_2)):
        print(hari_2[i])
elif a == "rabu" :
    for i in range(len(hari_3)):
        print(hari_3[i])
elif a == "kamis" :
    for i in range(len(hari_4)):
        print(hari_4[i])
elif a == "jumat" :
    print("Hari Jumat Anda tidak ada kelas")