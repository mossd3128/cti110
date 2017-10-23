# CTI-110
# M5HW3: Factorial
# Donald Moss
# 10/22/2017

while True:
    number1=int(input("Enter number "))
    number2=number1+1
    multipliers=list()
    for i in range(number1,0,-1):
        multipliers.append(i)
        #print(i)
    import operator
    import functools
    result = functools.reduce(operator.mul,multipliers, 1)
    print(result)




