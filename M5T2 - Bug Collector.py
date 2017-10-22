# CTI-110
# M5Lab2
# Donald Moss
# 10/22/2017

# Initialize the accumulater.
total = 0
# Get the bugs collected for each day.
for day in range (1, 7):
    # Prompt the user.
    print('Enter the bugs collected on day', day)

    # Input the number of bugs.
    bugs = int(input())

    # Add bugs to total.
    total += bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')
