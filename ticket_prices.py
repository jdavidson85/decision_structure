student_price = 5.00
veteran_price = 7.00
sponsor_price = 2.00
retiree_price = 6.00
public_price = 10.00

print("\nPlay Ticket Prices")
print("1. Student Price $5.00")
print("2. Veteran Price $7.00")
print("3. Show Sponsor Price $2.00")
print("4. Retiree Price $6.00")
print("5. General Public Price $10.00\n")

tickets_group = int(input("Enter the Ticket Price Group Number you are purchasing:"))
tickets_purchased = int(input("How many tickets would you like to purchase?"))
if tickets_group == 1:
    print("\nTotal price is $",  format(student_price * tickets_purchased, ".2f"))
elif tickets_group == 2:
    print("\nTotal price is $", format(veteran_price * tickets_purchased, ".2f"))
elif tickets_group == 3:
    print("\nTotal price is $", format(sponsor_price * tickets_purchased, ".2f"))
elif tickets_group == 4:
    print("\nTotal price is $", format(retiree_price * tickets_purchased, ".2f"))
else:
    if tickets_group > 4:
        print("\nTotal price is $", format(public_price * tickets_purchased, ".2f"))
if tickets_group == 1:
    print("Price per ticket is $", format(student_price, ".2f"))
elif tickets_group == 2:
    print("Price per ticket is $", format(veteran_price, ".2f"))
elif tickets_group == 3:
    print("Price per ticket is $", format(sponsor_price, ".2f"))
elif tickets_group == 4:
    print("Price per ticket is $", format(retiree_price, ".2f"))
else:
    if tickets_group > 4:
        print("Price per ticket is $", format(public_price, ".2f"))

# I couldn't figure out how to create the discounts and apply them correctly
