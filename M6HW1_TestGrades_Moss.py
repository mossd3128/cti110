# Write a program that asks the user to enter five test grades. The program should
# then display a letter grade for each score, and finally the average test score.
# November 12, 2017
# CTI-110 M6HW1_TestGrades
# Donald Moss

# Calculate average
def calc_average(total):
    return total / 5

def main():
    score1 = 0.0
    score2 = 0.0
    score3 = 0.0
    score4 = 0.0
    score5 = 0.0
    avg = 0.0

    score1 = getScore1()
    score2 = getScore2()
    score3 = getScore3()
    score4 = getScore4()
    score5 = getScore5()

    findAvg = calc_average(score1, score2, score3, score4, score5)
    letterGrade = determine_grade(findAvg)

# Table for displaying grades.
    print('Score\t\t Numeric Grade   Letter Grade')
    print('------------------------------------------------')
    print('Score 1:\t', score1, '\t\t', determine_grade(score1))
    print('Score 2:\t', score2, '\t\t', determine_grade(score2))
    print('Score 3:\t', score3, '\t\t', determine_grade(score3))
    print('Score 4:\t', score4, '\t\t', determine_grade(score4))
    print('Score 5:\t', score5, '\t\t', determine_grade(score5))

    print('Your final average is: ', findAvg, ',', 'This is your letter   grade: ', letterGrade)

# Input scores for calculating
def getScore1():
    score1 = float(input('Enter score 1: '))
    return score1
def getScore2():
    score2 = float(input('Enter score 2: '))
    return score2
def getScore3():
    score3 = float(input('Enter score 3: '))
    return score3
def getScore4():
    score4 = float(input('Enter score 4: '))
    return score4
def getScore5():
    score5 = float(input('Enter score 5: '))
    return score5

def calc_average(score1, score2, score3, score4, score5):
    total = score1 + score2 + score3 + score4 + score5
    avg = total / 5
    return avg

def determine_grade(findAvg):
    if findAvg >= 90 and findAvg <= 100:
        grade = 'A'
        return grade
    elif findAvg >= 80 and findAvg <= 89:
        grade = 'B'
        return grade
    elif findAvg >= 70 and findAvg <= 79:
        grade = 'C'
        return grade
    elif findAvg >= 60 and findAvg <= 69:
        grade = 'D'
        return grade
    else:
        grade = 'F'
        return grade


# Call the main function.
main()
