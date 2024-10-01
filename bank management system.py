import json

# read file , load data
customers_file = open("customers.json" ,'r')
customers_list = json.load(customers_file)
customers_file.close()
choice = None
flag_exit=True
while flag_exit:
    print("***** Welcome to SIC BANK management system! *****")
    choice = input("If you already have an account, enter 'login'.\nIf you don't have an account, enter 'register'.\n")
    if choice not in ["login", "register", "exit"]:
        print("Wrong choice, please try again!")
    if choice == "login":
        login_success = None
        while login_success != True:
            print("*** Welcome to the login page! ***")
            login_ID = int(input("Please enter your ID: "))
            login_Password = int(input("Please enter your password: "))

            for customer in customers_list:
                if customer["ID"] == login_ID and customer["password"] == login_Password:
                    login_success = True
                    break
            else:
                login_success = False

            if login_success:
                choice = -1
                while(choice != 4):
                    print("******************** WELCOME BACK ", customer["name"],"********************")
                    print("Please enter your choice ")
                    print("[0]Deposit")
                    print("[1]Withdraw ")
                    print("[2]Transfer ")
                    print("[3]Check balance & personal info")
                    print("[4]Exit")
                    choice = int(input())

                    if choice==4:
                        flag_exit=False
                        break

                    if choice == 0:
                        # Deposit
                        amount = -1
                        currency = "EGP"
                        while amount < 0.0 or currency not in ("USD", "SAR", "EGP","usd","sar","egp"):
                            print("please enter the amount you want to deposit and the currency in this format '1 EGP'")
                            print("you can USD or SAR or EGP enter currency : ")
                            user_input = input()

                            if len(user_input.split()) !=2:
                                print(" you MISSED the amount or currency, please try again ")
                                break
                            amount, currency = user_input.split()
                            amount = float(amount)
                            if amount < 0.0:
                                print("your amount with NEGATIVE, please try again !")
                                break
                            if currency not in ("USD", "SAR", "EGP","usd","sar","egp"):
                                print("you entered the currency wrong it should be USD or SAR or EGP  !")
                                break

                            print(f"{user_input} was deposited successfully !!")
                            if currency == "USD" or currency == "usd":
                                amount *= 30
                            elif currency == "SAR" or currency == "sar":
                                amount *= 9

                            customer["balance"] += amount
                            print(f"your balance is {customer['balance']}EGP")



                    elif choice == 1:
                        # withdraw
                        amount = -1
                        currency = "EGP"
                        while amount < 0.0 or currency not in ("USD", "SAR", "EGP", "usd", "sar", "egp"):
                            print("please enter the amount you want to deposit and the currency in this format '1 EGP'")
                            print("please enter currency capital with letters : ")
                            user_input = input()

                            if len(user_input.split()) != 2:
                                print(" you MISSED the amount or currency, please try again ")
                                break
                            amount, currency = user_input.split()
                            amount = float(amount)

                            if amount < 0.0:
                                print("your amount with NEGATIVE, please try again !")
                                break

                            if currency not in ("USD", "SAR", "EGP", "usd", "sar", "egp"):
                                print("you entered the currency wrong it should be USD or SAR or EGP  !")
                                break

                            if currency == "USD" or currency == "usd":
                                amount *= 30
                            elif currency == "SAR" or currency == "sar":
                                amount *= 9

                            if customer["balance"] < amount:
                                print("YOUR BALANCE IS LESS THAN THIS AMOUNT !!! \n please try again")
                                break

                            if customer["balance"] >= amount:
                                customer["balance"] -= amount
                                print(f"{amount} EGP was withdrawn successfully!!")
                                print(f"Your balance is {customer['balance']} EGP")

                    elif choice == 2:
                        # Transfer
                        tran_amount = int(input("Please enter the amount you want to transfer \n"))
                        tran_ID = int(input("Please enter the ID of the account you want to transfer money to \n"))
                        other_account = None
                        for cust in customers_list:
                            if cust["ID"] == tran_ID:
                                other_account = cust
                                break

                        if tran_amount > customer["balance"]:
                            print("Insufficient balance.")
                        else:
                            # tran_amount < customer["balance"]
                            if other_account:
                                customer["balance"] -= tran_amount
                                other_account["balance"] += tran_amount
                                print(tran_amount, " EGP  was transferred to ", other_account["name"], "successfully!!")
                                print("your balance is ", customer["balance"], " EGP")
                            else:
                                print("this account doesn't exist.")

                    elif choice == 3:
                        # check info
                        print("ID:",customer["ID"])
                        print("Name:",customer["name"])
                        print("Phone number:",customer["phone_number"])
                        print("Mail:",customer["mail"])
                        print("Gender:",customer["gender"])
                        print("Age:",customer["age"])
                        print("City:",customer["city"])
                        print("Balance:",customer["balance"],"EGP")

                    elif choice != 4:
                        print("invalid choice")
            else:
                print("Incorrect ID or password. Please try again.")


    elif choice == "register":
        name = input(f"Enter your name : ")
        password = int(input(f"Enter your password : "))
        phone_number = input(f"Enter your phone number : ")
        mail = input(f"Enter your mail : ")
        gender = input(f"Enter your gender : ")
        age = int(input(f"Enter your age : "))
        city = input(f"Enter your city : ")
        balance = 0
        cust_id = len(customers_list) + 1

        toAdd = {
            "ID": cust_id,
            "name": name,
            "password": password,
            "phone_number": phone_number,
            "mail": mail,
            "gender": gender,
            "age": age,
            "city": city,
            "balance": balance
        }
        customers_list.append(toAdd)
        print(f"Sign Up successful, your id is {cust_id}")


# write , update file
    customers_file = open("customers.json", "w")
    json.dump(customers_list, customers_file, indent=4)
    customers_file.close()
