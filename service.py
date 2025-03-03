
def showAvaliableChar(characters):
    allChar = ""
    no = 1
    for char in characters:
        allChar += f'{no}. /{char.name.replace(" ","")}\n'
        no += 1

    return allChar

def howToUseThisBot():
    message = ''' Untuk Review Karakter bisa ikutin step ini yaa~!
1. Pastikan karakter akun anda seperti gambar ini!
2. Masukkan UID melalui chat bot ini dengan format: /uid <YourUID> (contoh /uid 805498710)
3. List Karakter anda akan terlihat, pilih karakter yang ingin direview atau chat bot ini dengan format: /<NamaChar> (contoh /HuTao /Furina)

Bot akan Mereview karakter tersebut 😄!! 
Jika ingin review char lain lakukan step 3 aja yaa~
Jika build didalam game berubah maka lakukan step dari awal agar data nya keupdate 😉'''
    return message