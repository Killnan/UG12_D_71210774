# Ronand Joy 71210774
# Soal 1

a = int(input("Masukkan awal deret : "))
b = int(input("Masukkan akhir deret : "))

x = []
if (a + 1) % 2 == 0:
     for i in range (a+1,b,2):
         if i % 3 == 0 or i % 7 == 0: continue
         print ( i , end = " " )

else:
     for i in range (a , b , 2):
         if i % 3 == 0 or i % 7 == 0 : continue
         print (i , end = " ")