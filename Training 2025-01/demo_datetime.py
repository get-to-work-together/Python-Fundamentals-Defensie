from datetime import date
import dateutil
import locale

locale.setlocale(locale.LC_ALL, 'nl_NL')

d0 = date.today()
d1 = date(2025, 12, 31)

ndays = (d1 - d0).days
nweeks = ndays // 7

print(d0)
print(d1)
print(f'Nog {ndays} dagen')
print(f'Nog {nweeks} weken')

d3 = d0 + dateutil.relativedelta.relativedelta(months=6)
print(d3)

print(d0.strftime('%A %d %B %Y'))
