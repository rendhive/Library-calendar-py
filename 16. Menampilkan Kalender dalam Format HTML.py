import calendar

year = 2023
html_calendar = calendar.HTMLCalendar()
html_code = html_calendar.formatyear(year)
print("Kalender HTML 2023:")
print(html_code)
# Fungsi: Menghasilkan kalender dalam format HTML.
# Kondisi: Ketika Anda perlu menampilkan kalender di aplikasi web.
