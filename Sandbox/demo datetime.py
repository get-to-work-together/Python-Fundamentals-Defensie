from datetime import datetime
import time

dd = input('Geef een datum [dd-mm-yyyy]: ')

d = datetime.strptime(dd, '%d-%m-%Y')

print('Het is vandaag', d.strftime('%A %d %B %Y'), 'week', d.strftime('%V'))

time.sleep(2)

print('he he')

