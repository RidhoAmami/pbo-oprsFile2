class operasiFile ():
    def __init__(self):
        pass

    def bacaFile(self, file):
        try:
            with open(file, "r") as baca:
                catatan=baca.read()
                print('hasil dari :', file, '\n->', catatan)
        except FileNotFoundError as lost:
            return "File Tidak Ditemukan: {}".format(lost)


    def tulisFile(self, file, isi ,metode):
        if metode == 'w':
            try:
                with open(file, "w") as tulis:
                    tulis.write(isi)
                    print('teks berhasil ditulis ke : ', file)
            except Exception as e:
                print("Terjadi kesalahan saat menulis file {}: {}".format(file, e))
        else:
            try:
                with open(file, 'a') as tambah:
                    tambah.write(isi)
                    print('teks berhasil ditambah ke : ', file)
            except Exception as e:
                print(f"Terjadi kesalahan saat menambah tulisan ke file {file}: {e}")
            
objek=operasiFile()
objek.tulisFile("test.txt", "\ntambahan.", 'w')
objek.bacaFile('test.txt')
objek.tulisFile('test.txt', '\nIni adalah penambahan', 'a')
objek.bacaFile('test.txt')


