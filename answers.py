def calculate_discount(price, discount_percent):
    if discount_percent >= 20 :
        return price - (price * discount_percent / 100)
    else:
        return price


prize=float(input("Enter the prize: "))
discount_percent=float(input("Enter the discount percent: "))
print("The Final Price is: ", calculate_discount(prize, discount_percent))

    