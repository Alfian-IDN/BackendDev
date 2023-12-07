#Type hints
#Untuk buat kode lebih terjaga/aman, dan "membantu python untuk method2 tipe data"
#petunjuk ttg tipe data di Python
#tipe data yg sering kita pakai = str, int, bool, float, list, dict
#tipe data lain = tuple

#Testing

def nama_lengkap(nama_depan : str, nama_belakang : str, umur : int):
    nama_lengkap = f"{nama_depan} {nama_belakang}, berumur {umur}"
    #nama_lengkap2 = nama_depan + " " + nama_belakang + " " + str(umur) # not recomennded
    #return nama_lengkap2

nama_depan = "Abdurochman"
nama_belakang = "Alfian"
umur = 21
fullname = nama_lengkap(nama_depan=nama_depan, nama_belakang=nama_belakang, umur=umur)
print(fullname)

#custom function untuk mengeprint nama lengkapku. nama lengkap