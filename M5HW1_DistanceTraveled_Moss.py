# CTI-110
# M5HW1: Distance Traveled
# Donald Moss
# 10/22/2017

# Get speed and time
speed = int(input('Enter the speed of the vehicle in miles per hour:'))
time = int(input('Enter the number of hours it has traveled:'))

print('Hour \t\t Distance Traveled')

# Calculate distance 
for time in range(1, time + 1):
    distance = speed * time
    print(time, '\t\t\t', distance)

