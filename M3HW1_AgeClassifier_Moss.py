# CTI-110
# M3HW1 - Age Classifier
# Donald Moss
# 09/24/2017

def main():
    # This program takes a person's age and determines if the person is an infant, child, teenager, or adult.

    # system uses age requirements for determining results.
    infant = 1
    child = 13
    teenager = 18
    adult = 20
    

    
    age = int(input('Enter age: '))

    if age >= adult:
        print('Your age is: adult')
    else:
        if age >= teenager:
            print('Your age is: teenager')
        else:
            if age >= child:
                print('Your age is: child') 
            else:
                if age >= infant:    
                    print('Your age is: infant')
                







# program start
main()
