# python program to convert seconds to day, hour, minutes and seconds
time = float(input("Input time in seconds: "))

# convert seconds to day, hour, minutes and seconds

day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time

#print day, hour, minutes and seconds
print('Days', day)
print('Hours', hour)
print('Minutes', minutes)
print('Seconds', seconds)