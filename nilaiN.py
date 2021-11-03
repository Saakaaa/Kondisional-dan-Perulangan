import random

jumlah = int(input("Masukkan Nilai N :"))
for i in range(jumlah):
    i=random.uniform(0.0,0.5)
    print("Masukkan Data : 1 =>",i)

jawab ="betul"
hitung = 0
while (jawab):
    hitung +=1
    jawab =input ("----SELESAI----")
