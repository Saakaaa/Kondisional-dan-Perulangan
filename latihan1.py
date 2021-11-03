def main():
    #cetak judul program
    print("Menentukan Nilai Maksimum dua bilangan")

    #input user
    a = int(input("masukkan bilangan pertama: ",))
    b = int(input("masukkan bilangan kedua: "))

    #menentukan bilangan dengan if else
    if a > b:
        maks = a
    else:
        maks = b
        

    #mencetak nilai maksimum
    print("Nilai Terbesar Adalah %d" % maks)

if __name__=='__main__':
    main()
        
