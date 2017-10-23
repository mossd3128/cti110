# CTI-110
# M5HW2: Running Total
# Donald Moss
# 10/22/2017

# Get total
n = int(input('How many numbers to sum? '))
total = 0
for i in range(n):
    s = input('Enter number ' + str(i + 1) + ': ')
    total = total + int(s)
    while keep_on_going <= 0 :
print('The sum is ' + str(total))




