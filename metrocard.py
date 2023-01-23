# give function metrocard_calculator and give two parameter number of rides, and refill_amount
def metrocard_calculator(number_rides, refill_amount):
    # give base price discount, unlimited discount, unlimted rides,bulk ride
    base_price = 2.75
    bulk_discount = 0.05
    unlimited_discount = 0.10
    unlimited_rides = 30
    bulk_rides = 20
    # use if elif condition number of rides 0 return invail input beacuse number must be a positive integer
    if number_rides < 0:
        return "Invalid input. Number of rides must be a positive integer."
    # unless the number of rides is greater than a certain threshold bulk_rides in which case a bulk discount is applied
    elif number_rides < bulk_rides:
    # when number of rides less than bulk ride return number of rides * base price
        return number_rides * base_price
    #greater than another threshold unlimited_rides in which case a different discount is applied
    elif number_rides < unlimited_rides:
        return (number_rides * base_price) - (bulk_discount * (number_rides * base_price))
    # if the number of rides is equal or greater than unlimited_rides, the final price is computed as refill_amount
    else:
        return refill_amount - (unlimited_discount * refill_amount)
    #input from the user which is the number of rides they want to take.  
    #input from the user which is the refill amount for the metro card
number_rides = int(input("Enter the number of rides: "))
refill_amount = float(input("Enter the refill amount: "))

# final price calculate
print("MetroCard Price: $" + str(metrocard_calculator(number_rides, refill_amount))) 