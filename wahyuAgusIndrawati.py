print("konversi satuan detik ke jam/menit/detik")
print("========================================")
jumlah_detik =int(input("masukkan angka: "))

jam = jumlah_detik//3600
sisa_detik = jumlah_detik - jam*3600
menit = sisa_detik//60
detik = sisa_detik - (60*menit)

print("%d jam %d menit %d detik"%(jam,menit,detik))