import calendar

year = 2023
total_weeks = sum(1 for month in range(1, 13) for week in calendar.monthcalendar(year, month) if week[0] != 0)
print(f"Jumlah minggu dalam tahun {year}: {total_weeks}")
# Fungsi: Menghitung jumlah minggu dalam tahun tertentu.
# Kondisi: Ketika Anda perlu mengevaluasi jumlah minggu di dalam tahun.
