print("Enter Your card name:")
print("Select a card to use:")
print("1. Master Card")
print("2. Visa Card")
print("3. Rupay Card")
n=int(input("Enter Your choice:"))
if(n==1):
    print("Master Card")
elif(n==2):
     print("Visa Card")
else:
     print("Rupay Card")


# print("Enter your amount:")
amount=0
balance=100
# if(amount>=balance):
#     print("insufficent amount")
if(amount<balance):
    print("sufficient amount")
    pin=int(input("Enter your pin:"))
    setpin=1234
    if(pin==setpin):
        print("pin is correct your balance is:",balance)
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice=int(input("Enter your choice:"))
        if(choice==1):
                print("your balance is:",balance)
        elif(choice==2):
                deposit=int(input("Enter amount to deposit:"))
                newbalance=balance+deposit
                print("Your new balance is:",newbalance)
        elif(choice==3):
                withdraw=int(input("Enter amount to withdraw:"))
                newbalance=balance-withdraw
                print("your new balance is:",newbalance)
        elif(choice==4):
                exit
        else:
                print("invalid choice")

else:
    print("insufficent amount")     
    print("deposit some amount")
    if(amount<balance):
        deposit=int(input("Enter amount to deposit:"))
        newbalance=balance+deposit
        print("Your new balance is:",newbalance)
    print("Thank you")           