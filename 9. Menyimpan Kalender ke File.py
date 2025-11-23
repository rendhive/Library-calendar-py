import calendar

year = 2023
with open('calendar_2023.txt', 'w') as f:
    f.write(calendar.calendar(year))
print("Kalender 2023 telah disimpan ke file.")
# Fungsi: Menyimpan kalender tahun tertentu ke dalam file teks.
# Kondisi: Ketika Anda perlu menyimpan informasi kalender untuk referensi di masa depan.
