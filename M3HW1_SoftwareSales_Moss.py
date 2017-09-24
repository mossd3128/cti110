# CTI-110
# M3HW2-Software Sales
# Donald Moss
# 09/024/2017

def main():
    # Get the packages purchased.
    packages_purchased = float(input('Enter the packages purchased: '))

    # Calculate packages purchased by the retail cost of one package.
    total_cost = packages_purchased * 99.00

    # Display the total cost.
    print('The total cost is $', format(total_cost, '.2f'))

    # Get total cost of packages with discount included from bulk purchases.

    if packages_purchased >= 100:
        packages_purchased * 0.40
    else:   
        if packages_purchased <= 99:
            packages_purchased * 0.30
        else:    
            if packages_purchased <= 49:
                packages_purchased * 0.20
            else:    
                if packages_purchased <= 19:
                    packages_purchased * 0.10

    # Display the total cost with discount
    print('The total cost with discount is $', format(total_cost, '.2f'))




# program start

main()
