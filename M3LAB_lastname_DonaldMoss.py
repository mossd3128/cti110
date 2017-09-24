# CTI-110
# M3Lab: Debugging
# Donald Moss
# 09/24/2017
# I was supposed to put a comment here
# My Last Name

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 100
    B_score = 90
    C_score = 80
    D_score = 70
    F_score = 60

    
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score > B_score:
            print('Your grade is: A')
        else:
            if score > C_score:
                print('Your grade is: B') 
            else:
                if score > D_score:    
                    print('Your grade is: C')
                else:
                    if score > F_score:
                        print('Your grade is: D')
                    else:
                            if score <= F_score:
                                print('Your grade is: F')    







# program start
main()
