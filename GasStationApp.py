"""Gas Station App. Developed by Nhi Dang.

App menu allows a customers to fill gas, and a manager to get sales information, reset totals, and change gas prices.
Prices: 3.70, 3.90, 4.10$ per gallon.
Display the selected grade, the price and total sales, total number of gallons sold of each grade.

input: grade(int), num_gallons(float)
output: fill shows grade(int), rate and price(floats), sales show total number of gallons solde of each grade and total sales,
prices show the per gallons price for each grade of fuel and prompts manager to enter new prices,
end_of_day shows number of gallons sold each fuel and prompt manager whether to reset or not.
"""

#globals
price1 = 3.7 #price per gallons of Regular
price2 = 3.9 #price per gallons of Extra
price3 = 4.1 #price per gallons of Premium
total_gallons1 = 0 #number of Regular gallons sold
total_gallons2 = 0 #number of Extra gallons sold
total_gallons3 = 0 #number of Premium gallons sold
total_sales = 0 #total sales across orders


#functions

def fill():
    """input: grade(int), num_gallons(float)
    output: price(float) """

    global total_gallons1, total_gallons2, total_gallons3, total_sales, price1, price2, price3
    print('Choose 1.Regular  2.Extra  3.Premium ')
    print(f'{price1}$, {price2}$, {price3}$ per gallon')
    grade = int(input('Enter 1/2/3:\n>'))

    if grade == 1:
        rt = float(price1)
        graded = 'Regular'
    elif grade == 2:
        rt = float(price2)
        graded = 'Extra'
    elif grade == 3:
        rt = float(price3)
        graded = 'Premium'
    else:
        print('Invalid! Please enter 1..3')
    
    print(f'Your selection:{graded}  ${rt} per gallon')

    num_gallons = float(input('Enter the number of gallons filled:'))

    if num_gallons != 0:
        price = rt * num_gallons
        print(f'Price:{price:.2f}')
    else:
        print('Operation Cancelled')
        return 

    #updates
    if grade == 1:
        total_gallons1 += num_gallons
        price = num_gallons * rt
    elif grade == 2:
        total_gallons2 += num_gallons
        price = num_gallons * rt
    else:
        total_gallons3 += num_gallons
        price = num_gallons * rt 
    
    total_sales += price 

    

def sales():
    """input: none  output: total_gallons1, total_gallons2, total_gallons3(all floats) """

    global total_gallons1, total_gallons2, total_gallons3, total_sales
    
    print(f'Gallons sold: Regular: Extra: Premium\nTotal\t: {total_gallons1}\t:{total_gallons2}\t: {total_gallons3} \nTotal sales:{total_sales:.2f} ')

def prices():
    """input: price1_change, price2_change, price3_change (all strs)
    output: price1, price2, price3 (all floats) """ 

    global total_gallons1, total_gallons2, total_gallons3, total_sales, price1, price2, price3
    print(f'Prices: Regular, Extra, Premium:\n{price1}$, {price2}$, {price3}$ per gallon')
    print('For each grade, when prompted, enter new price, or hit Return if price stays the same.')
    price1_change = input('Enter a new price for Regular: >>>')
    price2_change = input('Enter a new price for Extra: >>>')
    price3_change = input('Enter a new price for Premium: >>>')
    update = int(input('Enter 1 to Confirm change of prices, 0 to Cancel!'))

    if update:
        if price1_change:
            price1 = float(price1_change)
        if price2_change:
            price2 = float(price2_change)
        if price3_change:
            price3 = float(price3_change)
        print(f'New prices:\nRegular:{price1}\nExtra:{price2}\nPremium:{price3} ')
    else:
        print('Cancle! Nothing changed!')

def end_of_day():
    """Reset or not reset data at the end of the day!
    input: reset(str)  output: none """

    global total_gallons1, total_gallons2, total_gallons3, total_sales
    print(f'Gallons sold: Regular: Extra: Premium\nTotal\t: {total_gallons1}\t:{total_gallons2}\t: {total_gallons3} \nTotal sales:{total_sales:.2f} ')
    end = int(input('Enter 1 for Reset or 0 for Not reset:'))
    if end:
        total_gallons1 = 0
        total_gallons2 = 0
        total_gallons3 = 0
        total_sales = 0 
        print(f'Prices per gallon:\nRegular:{price1}  Extra:{price2}  Premium:{price3} ')
        print('Get ready for a new day!')
    else:
        print('No reset!!!')



#main
quit = False
while not quit:
    print('1.Fill  2. Sales  3.Prices  4.End of Day  5.Exit')
    choice = int(input('Enter choice:'))
    if choice == 1:
        fill()
    elif choice == 2:
        sales()
    elif choice == 3:
        prices()
    elif choice == 4:
        end_of_day()
    elif choice == 5:
        quit = True
    else:
        print('Invalid choice!')

print('Bye!!!')

