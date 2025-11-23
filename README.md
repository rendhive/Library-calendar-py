# Library-calendar-py

Penggunaan Modul calendar di Python

Modul simpel tapi powerful buat ngulik kalender

Modul calendar adalah bagian dari Python Standard Library, jadi kamu bisa langsung pakai tanpa instalasi tambahan. Cocok buat aplikasi yang butuh informasi tanggal, penjadwalan, statistik waktu, sampai bikin tampilan kalender di CLI atau web.



📚 Daftar Isi

Instalasi

Penggunaan Dasar

Menampilkan Kalender Bulanan

Menampilkan Kalender Tahunan

Mengetahui Hari Pertama Bulan

Mengetahui Apakah Suatu Tahun Kabisat

Menghitung Jumlah Hari dalam Sebuah Bulan


Kondisi Penggunaan

Referensi


🛠 Instalasi

Tidak perlu instal apa pun. Modul calendar sudah otomatis tersedia di Python 3.x.


🚀 Penggunaan Dasar

📆 Menampilkan Kalender Bulanan

import calendar

year = 2023
month = 10

print(calendar.month(year, month))

📅 Menampilkan Kalender Tahunan

import calendar

year = 2023

print(calendar.calendar(year))

🗓 Mengetahui Hari Pertama Bulan

import calendar

year = 2023
month = 10

first_day = calendar.monthcalendar(year, month)[0][0]
print("Hari pertama bulan ini:", calendar.day_name[first_day])

🔢 Mengecek Tahun Kabisat

import calendar

year = 2024

print(calendar.isleap(year))  # True jika kabisat

📊 Menghitung Jumlah Hari dalam Bulan

import calendar

year = 2023
month = 10

days_in_month = calendar.monthrange(year, month)[1]
print(f"Banyaknya hari di bulan {month}/{year}: {days_in_month} hari")


---

🎯 Kondisi Penggunaan

Modul calendar cocok dipakai ketika kamu butuh:

Menampilkan data kalender untuk aplikasi CLI atau web.

Mengevaluasi tanggal (hari apa, jumlah hari, kabisat, dll).

Analisis berbasis waktu seperti statistik transaksi per hari/bulan.

Generate HTML kalender (karena modul ini juga punya HTMLCalendar).



---

📖 Referensi

Dokumentasi resmi Python: calendar
https://docs.python.org/3/library/calendar.html