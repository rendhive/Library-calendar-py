import calendar

month_days = calendar.monthcalendar(2023, 10)
print("Hari dalam bulan ini:")
for week in month_days:
    for day in week:
        if day != 0:
            print(day, end=' ')
print()  # Menambahkan newline
# Fungsi: Menampilkan semua hari dalam bulan tanpa spasi kosong.
# Kondisi: Ketika Anda perlu mengekstrak semua hari dengan fokus.
