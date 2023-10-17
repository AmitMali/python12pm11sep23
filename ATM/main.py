
pin=1234
pinAttempts=0
def loggedIn():
    userpin = int(input("Enter Your Pin"))
    global pinAttempts
    if pinAttempts<2:
        if userpin==pin:
            return True
        else:
            pinAttempts+=1
            return False
    else:
        print("Pin limit exceeded you are blocked")
        return False

def showMenu():
    print("1 - Check Balance\n2 - Withdraw\n3 - Deposite\n4 - exit")


def ATM():
    balance=1000
    choice=0

    while choice != 4:
        if loggedIn():
            showMenu()
            choice = int(input("Enter Your Choice"))
            if choice == 1:
                print(f"Your balance is {balance}")
            elif choice == 2:
                amount = int(input("Enter Amount in multiple of s100"))
                if balance > amount:
                    balance -= amount  # as same as ---> balance=balance-amount
                    print("Amount Withdrawn Successfully")
                else:
                    print("Insufficient fund")
            elif choice == 3:
                amount = int(input("Enter Amount upto 20000"))
                if amount <= 20000:
                    if amount % 100 == 0:
                        balance += amount  # as same as ---> balance=balance-amount
                        print("Amount Deposited Successfully")
                    else:
                        print("Enter amount in multiples of 100")
                else:
                    print("You exceeded the deposit limit ")
            elif choice == 4:
                print("Thank you ")



ATM()