
balance=0
#account creating
def account_creating():
    global balance
    balance=int(input("Enter your initial amount:"))
    print("Your account is now created!!")   

def deposit_amount():
    global balance
    deposit=int(input("Enter deposit amount:"))
    if deposit>0:
        balance+=deposit
        print("Your deposit is successful,total amount is:",balance)
    else:
        print("deposit unsuccessful")

def withdraw_amount():
    global balance
    withdraw=int(input("Enter withdraw amount:"))
    if withdraw<=balance:
        balance-=withdraw
        print("Successfull withdrawl and you balance is:",balance)
    elif withdraw>balance and withdraw==0:
        print("Invalid withdrawl") 

def check_balance():
    print("Your current balance is:",balance)
  

print("Welcome to our bank")
while True:
    print("Welcome to our bank...manu-->")
    print("1. Create acoount")
    print("2. Deposit amount")
    print("3. Withdraw amount")
    print("4. Check balance")
    print("5. Exit manu")

    Choice=int(input("Enter your choice:"))

    if Choice==1:
        account_creating()
    elif Choice==2:
        deposit_amount()
    elif Choice==3:
        withdraw_amount()
    elif Choice==4:
        check_balance()
    elif Choice==5:
        print("Thanks for choosing our bank>>>Good day")
        break
    else:
        print("Invalid input")                

            
