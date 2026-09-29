# =========================
#     PRODUCT CATALOGUE
# =========================

product1 = "Laptop"
product2 = "Mouse"
product3 = "Keyboard"
product4 = "Monitor"

product1_price = 60000
product2_price = 1500
product3_price = 3000
product4_price = 25000

product1_stock = 5
product2_stock = 20
product3_stock = 10
product4_stock = 7

total = 0
change = 0


while True:
    print('''Available products are: 
    1. Laptop
    2. Mouse
    3. Keyboard
    4. Monitor
    ''')  

    choice = int(input("Enter choice(1,2...): "))
    
    if choice == 1:
        print(f"You chose {product1}")
        print(f"remaining {product1}s are {product1_stock} going at {product1_price} each")
        quantity = int(input("How many do you want: "))
        if quantity > product1_stock:
            print(f"remaining {product1}s are {product1_stock} only")
        else:
            total = product1_price * quantity
            print(f"Total amount is: {total}ksh")
            remaining_stock = product1_stock - quantity
            print(f"remaining {product1}s are {remaining_stock}")
            print()
            payment_amt = int(input("Enter amount to pay: "))
            if payment_amt >= total:
                change = payment_amt - total
                print(f"Change: {change}")
                print("Purchase successful")

                purchase_option = input("Would you like to continue? yes/no: ")
                if purchase_option == "yes":
                    continue
                else:
                    print("Thank you for shopping!")
                    break
            else:
                print("Can't complete purchase")



    elif choice == 2:
        print(f"You chose {product2}")
        print(f"remaining {product2}s are {product2_stock} going at {product2_price} each")
        quantity = int(input("How many do you want: "))
        if quantity > product2_stock:
            print(f"remaining {product2}s are {product2_stock} only")
        else:
            total = product2_price * quantity
            print(f"Total amount is: {total}ksh")
            remaining_stock = product2_stock - quantity
            print(f"remaining {product2}s are {remaining_stock}")
            print()
            payment_amt = int(input("Enter amount to pay: "))
            if payment_amt >= total:
                change = payment_amt - total
                print(f"Change: {change}")
                print("Purchase successful")


                purchase_option = input("Would you like to continue? yes/no: ")
                if purchase_option == "yes":
                    continue
                else:
                    print("Thank you for shopping!")
                    break
            else:
                print("Can't complete purchase")

    elif choice == 3:
        print(f"You chose {product3}")
        print(f"remaining {product3}s are {product3_stock} going at {product3_price} each")
        quantity = int(input("How many do you want: "))
        if quantity > product3_stock:
            print(f"remaining {product3}s are {product3_stock} only")
        else:
            total = product3_price * quantity
            print(f"Total amount is: {total}ksh")
            remaining_stock = product3_stock - quantity
            print(f"remaining {product3}s are {remaining_stock}")
            print()
            payment_amt = int(input("Enter amount to pay: "))
            if payment_amt >= total:
                change = payment_amt - total
                print(f"Change: {change}")
                print("Purchase successful")

                purchase_option = input("Would you like to continue? yes/no: ")
                if purchase_option == "yes":
                    continue
                else:
                    print("Thank you for shopping!")
                    break
            else:
                print("Can't complete purchase")

    elif choice == 4:
        print(f"You chose {product4}")
        print(f"remaining {product4}s are {product4_stock} going at {product4_price} each")
        quantity = int(input("How many do you want: "))
        if quantity > product4_stock:
            print(f"remaining {product4}s are {product4_stock} only")
        else: 
            total = product4_price * quantity
            print(f"Total amount is: {total}ksh")
            remaining_stock = product4_stock - quantity
            print(f"remaining {product4}s are {remaining_stock}")
            print()
            payment_amt = int(input("Enter amount to pay: "))
            if payment_amt >= total:
                change = payment_amt - total
                print(f"Change: {change}")
                print("Purchase successful")


                purchase_option = input("Would you like to continue? yes/no: ")
                if purchase_option == "yes":
                    continue
                else:
                    print("Thank you for shopping!")
                    break
            else:
                print("Can't complete purchase")

    else:
        print("Invalid Choice")
    
