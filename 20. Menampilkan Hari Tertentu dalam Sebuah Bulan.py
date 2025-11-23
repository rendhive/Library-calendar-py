import calendar

year = 2023
month = 10
day = 4
if day in calendar.monthcalendar(year, month)[(day // 7)]:
    print(f"{day} {calendar.month_name[month]} {year} jatuh pada hari {calendar.day_name[calendar.weekday(year, month, day)]}")
else:
    print("Hari tidak ada dalam bulan ini.")
# Fungsi: Menampilkan hari tertentu dalam bulan dengan pengecekan.
# Kondisi: Ketika Anda perlu mengetahui hari dari tanggal tertentu dalam bulan.
