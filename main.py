daftar_matkul = []
J = int(input("Masukkan jumlah matkul hari ini: "))
for _ in range(J):
    matkul_id, waktu_mulai, waktu_selesai = input("Masukkan kode matkul, Waktu mulai [0-24], Waktu selesai [0-24] [Contoh: C-TI208, 13, 15]: \n").split(', ')
    waktu_mulai, waktu_selesai = int(waktu_mulai), int(waktu_selesai)
    daftar_matkul.append((matkul_id, waktu_mulai, waktu_selesai, 1))
jadwal_ruang = {i: [True] * 24 for i in range(1, 6+1)}
for matkul_id, waktu_mulai, waktu_selesai, kebutuhan_ruang in daftar_matkul:
    ruang = next(((r for r in range(1, 6+1) if all(jadwal_ruang[r][waktu_mulai:waktu_selesai]) and 6 >= kebutuhan_ruang)), None)
    if ruang:
        for waktu in range(waktu_mulai, waktu_selesai):
            jadwal_ruang[ruang][waktu] = False
        print(f"Matkul dengan kode {matkul_id} dijadwalkan pada ruang D4-{ruang+1} dari jam {waktu_mulai} sampai {waktu_selesai}")
    else:
        print(f"Tidak ada ruang kosong yang memenuhi kebutuhan untuk matkul dengan kode {matkul_id}")