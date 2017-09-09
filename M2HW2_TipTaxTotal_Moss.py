# CTI-110
# M2HW2 - Tip Tax Total
# Donald Moss
# 09/09/2017
# Get the meal cost.
meal_cost = float(input('Enter the meal cost: '))

# Calculate the total cost by including tip amount and sales tax.
tip = meal_cost * 0.18
sales_tax = meal_cost * 0.07
total_cost = meal_cost + tip + sales_tax

# Display the total meal cost.
print('The total cost of the meal is $', format(total_cost, '.2f'))

# Display the tip.
print('The amount of the tip is $', format(tip, '.2f'))

# Display the sales tax.
print('The amount of the sales tax is $', format(sales_tax, '.2f'))
