nilai_siswa = [85, 90, 70, 60, 60, 95, 100, 87, 88, 93]

rata_rata = sum(nilai_siswa) / len(nilai_siswa)

print("nilai rata_rata siswa adalah : ", rata_rata)

nilai = float(input("Masukkan nilai anda : "))

if nilai > rata_rata:
    print("Nilai anda diatas rata_rata")
elif nilai == rata_rata:
    print("Nilai anda sama dengan rata-rata")
else :
    print("Nilai anda dibawah rata-rata")