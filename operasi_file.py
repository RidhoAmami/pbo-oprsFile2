#fungsi baca
def baca(nama):
    try:
        with open(nama, 'r') as file:
            isi = file.read()
            print(f"Isi file :{nama}->\n{isi}")
    except FileNotFoundError as err:
        print ("Terjadi kesalahan: {}".format(err))

#fungsi tulis
def tulis(nama, newTeks):
    with open(nama, 'w') as file_tulis:
        file_tulis.write(newTeks)

# Contoh penggunaan
intro = "puja : hai kids"
inti = "puja : this is your dad"
penutup = "puja : ayahmu sekarang bisa jamsut"
tambahan = "kameramen : ayahmu sakit nak"
tulisan = "tugas operasi file/tulisBaru.txt"
teksBaru = "\n{}\n{}\n{}\n{}".format(intro, inti, penutup, tambahan)

tulis(tulisan, teksBaru)

baca(tulisan)

print ("contoh error")
