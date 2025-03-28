#### Bank of Samuel
# Project
# Create Customer Names, Pin, Balance
customerName=["samuel","susan","jayden","david","hannah","suseela"] #List
customerBalance=[200000,200000,500000,500000,500000,1000000]        #List
customerPin=["1234","1111","0000","2222","3333","7777"]             #List
accountBalance=0
accountWithdrawl=0
accountDeposit=0
counter1=1  # This variable is used to keep track of the number of accounts being created in the while loop inside option 1
counter2=6  # Every new customer is stored at index counter2, which starts at 6 (since 6 accounts already exist).
            # This variable is used as an index to append new customers to the customerName, customerPin, and customerBalance lists.
            # So, counter2 is incremented for the next customer.
i=0


while True:
    print("<><><><><><><><>  *   Welcome to Bank of Samuel  *   <><><><><><><><>")
    print("------------------*------------------------------*-------------------")
    print("<><><><><><><><>  *  1. Open a new account       *   <><><><><><><><>")
    print("<><><><><><><><>  *  2. Deposit money            *   <><><><><><><><>")
    print("<><><><><><><><>  *  3. Withdraw money           *   <><><><><><><><>")
    print("<><><><><><><><>  *  4. Check account balance    *   <><><><><><><><>")
    print("<><><><><><><><>  *  5. Close the account        *   <><><><><><><><>")
    print("<><><><><><><><>  *  6. Privilege Customers List *   <><><><><><><><>")
    print("<><><><><><><><>  *  7. Exit                     *   <><><><><><><><>")
    selectOption=input("Please choose the option: ")


    # Option 1 from the menu: Open a new account
    if selectOption=="1":
        print("Please enter your details to create the account")
        no_of_customers=int(input("Number of customers: "))
        i=i+no_of_customers         # This keeps track of the total number of customers.
        
        if i>4:     #Maximum number of customers is 4, since 6 accounts are already in the system which makes a total of 10 customers per bank.
            print("Exceeded maximum number of customers. Please visit the nearest branch to open a new account")
            i=i-no_of_customers     # This ensures the i value which is 4, doesn't exceed the limit.
        else:
            #The while loop will run according to the no.of customers
            while counter1<=i:      # This loop runs for the number of customers being added (no_of_customers).
                                    # Initially, counter1=1, and it increments with every new customer.
                                    # When counter1>i, the loop stops.

                name=input("Please enter your full name: ")
                customerName.append(name)   # takes the input from name and appends to customerName
                pin=str(input("Please enter the pin: "))
                customerPin.append(pin)     # takes the input from pin and appends to customerPin
                accountBalance=0
                accountDeposit=int(input("Please enter the amount to deposit to start an account: "))#takes the input and assign it to accountDeposit
                accountBalance=accountBalance+accountDeposit    # 0=0+500(if accountDeposit is 500)
                customerBalance.append(accountBalance)          # (append 500 to customerBalance)
                print("\nName = ",end='')
                print(customerName[counter2])
                print("Pin = ",end='')
                print(customerPin[counter2])
                print("Balance = ",end='')
                print(customerBalance[counter2])
                counter1=counter1+1
                counter2=counter2+1
                print("\nCongratulations!!! You are now one of the privilege customer of this bank")
                print("Your new debit card and pin will be delivered to your address shortly")
                print("IMPORTANT: Please do not disclose your pin")
                print("******************************************")
        selectOption=input("Press enter to return to the menu or exit")

    #Option 2 from the menu: Deposit the money
    elif selectOption=="2":
        print("You have choosen the option to deposit the money")
        n=0  # This initializes a variable n to 0. It's being used as a condition for a while loop later. The loop will run as long as n is less than 1. The value of n will likely be changed inside the loop to eventually exit it.
        while n<1:  # This while loop will run as long as n is less than 1. Since n starts at 0, this loop will run at least once. After a successful deposit (if the name and pin match), n is set to 1 (n = n + 1), which causes the loop to stop.
            k=-1    # Here, k is initialized to -1. This variable is used as an index to loop through the customer names list (customerName). Starting from -1 is just a way to ensure that the first iteration of the loop starts at index 0 when k is incremented.
            name=input("Please enter your name: ")
            pin=input("Please enter the pin: ")
            while k<len(customerName)-1:    # Loop through all customer names to verify the credentials.
                k=k+1                       # Increment k to move through the list of customer names.
                if name==customerName[k]:
                   if pin==customerPin[k]:
                        n=n+1               # If name and pin matches, n is set to 1 to stop the while loop.
                        print("Your current account balance is: ")
                        print(customerBalance[k])
                        accountDeposit=eval(input("Please enter the amount to deposit: "))
                        accountBalance=customerBalance[k]+accountDeposit
                        customerBalance[k]=accountBalance
                        print("Your new balance: ",accountBalance)
                if n<1:
                    print("Your name and pin does not match. Please try again")                
            selectOption = input("Press enter to return to the menu or type 'exit' to quit: ")
        if selectOption.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'.
    
    #Option 3 from the menu: Withdraw money from the account
    elif selectOption=="3":
        j=0
        print("You have choosen the option to withdraw money")
        while j<1:
            k=-1
            name=input("Please enter your name: ")
            pin=input("Please enter the pin: ")
            while k<len(customerName)-1:
                k=k+1
                if name==customerName[k]:
                    if pin==customerPin[k]:
                        j=j+1
                        print("Your current balance: ")
                        print(customerBalance[k])
                        accountBalance=(customerBalance[k])
                        accountWithdrawl=eval(input("Enter the amount to withdraw: "))
                        if accountWithdrawl>accountBalance:
                            print("Insufficient Funds. Please try again")
                            accountWithdrawl=eval(input("Please enter the amount to withdraw: "))
                            accountBalance=accountBalance-accountWithdrawl
                            print("Withdrawl successful")
                            customerBalance[k]=accountBalance
                            print("Your new balance: ",accountBalance)
                        else:
                            accountBalance=accountBalance-accountWithdrawl
                            print("Withdrawl Successful")
                            customerBalance[k]=accountBalance
                            print("Your new balance: ",accountBalance)
                    if j<1:
                        print("Your name and pin does not match. Please try again")                
            selectOption = input("Press enter to return to the menu or type 'exit' to quit: ")
        if selectOption.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'.
    
    #Option 4 from the menu: Check the balance from the account
    elif selectOption=="4":
        print("You have choosen the option to check the balance")
        m=0
        while m<1:
            k=-1
            name=input("Please enter your name: ")
            pin=input("Please enter your pin: ")
            while k<len(customerName)-1:
                k=k+1
                if name==customerName[k]:
                    if pin==customerPin[k]:
                        m=m+1
                        print("Your present account balance: ")
                        print(customerBalance[k])
                    else:
                        break
        if m<1:
                print("Your name and pin does not match. Please try again")                
        selectOption = input("Press enter to return to the menu or type 'exit' to quit: ")
    if selectOption.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'.


    #Option 5 from the menu: Close the bank account
    elif selectOption == "5":
        print("You have chosen the option to close your account")
        name = input("Please enter your name: ")
        pin = input("Please enter your pin: ")
        if name in customerName:  # Check if the name exists
            index = customerName.index(name)  # Get index of the account
            if pin == customerPin[index]:  # Check if the pin matches
                confirmation = input("Are you sure you want to delete your account? (yes/no): ").lower()
                if confirmation == "yes":
                    # Delete account details from all lists
                    del customerName[index]
                    del customerPin[index]
                    del customerBalance[index]
                    print("Your account has been deleted successfully.")
                else:
                    print("Your account is not deleted")
            else:
                print("Incorrect PIN. Please try again.")
        else:
            print("Account not found. Please try again.")
        selectOption = input("Press enter to return to the menu or exit")


    #Option 6 from the menu: Display list of privilege customers
    elif selectOption=="6":
        print("You have choosen the option to see privilege customers list")
        k=0 #Initializes a counter variable k to 0. This variable will be used to loop through the customerName list.
        print("\nBank of Samuel")
        print("--------------")
        while k<=len(customerName)-1:       #Starts a while loop that runs as long as k is less than or equal to the last index in customerName.
                                            #len(customerName)-1 gives the index of the last customer in the list.
            print("Privilege customer : ")  #Prints the customer name at index k in the customerName list.
            print(customerName[k])
            k=k+1   #Increments k by 1 to move to the next customer in the list. This ensures the loop goes through all customers in the list.
        selectOption=input("Press enter to return to the menu or exit")

    #Option 7 from the menu: To Exit
    elif selectOption=="7":
        print("You have choosen the option to exit")
        print("\nThank you for banking with us")
        print("\nVisit us again soon")
        print("Have a nice day")
        break

    else:
        print("You have selected the invalid option")
        print("\nPlease try again")
        selectOption=input("Press enter to return to the menu or exit")
