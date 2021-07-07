base_price = float(input("Enter the base price of a car: "))
tax = base_price * .08
car_license = base_price * .08
dealer_prep = 1000
destination_charge = 400
print("Total price of Car: " \
      + str(base_price + tax + car_license + dealer_prep + destination_charge))
