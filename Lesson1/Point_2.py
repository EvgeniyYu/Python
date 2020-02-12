seconds = int(input('Enter the time in seconds: '))
hours = seconds // 3600
t = seconds % 3600
minutes = t // 60;
rest_seconds = t % 60;
print('%02d:%02d:%02d' % (hours, minutes, rest_seconds))
