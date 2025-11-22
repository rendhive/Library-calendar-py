import calendar

year = 2023
month = 10
first_weekday = calendar.monthcalendar(year, month)[0][0]
print("Hari pertama bulan ini:", calendar.day_name[first_weekday])
# Fungsi: Mengetahui hari pertama dari bulan tertentu.
# Kondisi: Ketika Anda perlu mengetahui hari pertama suatu bulan.
