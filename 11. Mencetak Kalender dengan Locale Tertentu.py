import calendar

import locale
locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')  # Mengatur locale ke Bahasa Indonesia
year = 2023
month = 10
print(calendar.month(year, month))
# Fungsi: Menampilkan kalender dengan nama bulan dan hari dalam bahasa lokal.
# Kondisi: Ketika Anda perlu menampilkan dengan bahasa tertentu sesuai kebutuhan pengguna.
