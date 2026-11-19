class Bank:
    def __init__(self, accno, name, acctype, balance=0):
        self.accno=accno
        self.name=name
        self.acctype=acctype
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposit successfull new balance:{self.balance}")
        else:
            print("invalid deposit amount.enter a positive value.")
    def withdraw(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance -=amount
                print(f"new balance:{self.balance}")
            else:
                print("insufficient balance.")
        else:
            print("invalid withdrawal amount.enter a positive value.")
    def display(self):
        print("\naccount number:",self.accno)
        print("account holder name:",self.name)
        print("account type:",self.acctype)
        print("balance:",self.balance)
b1=Bank(1002,"Nidhi","Savings",0)
b1.display()
while True:
    print("\n***MENU***")
    print("1.deposit")
    print("2.withdraw")
    print("3.display")
    print("4.exit")
    choice=int(input("\nenter your choice(1-4):"))
    if choice == 1:
        d=float(input("enter amount to be deposited:"))
        b1.deposit(d)
    elif choice == 2:
        w=float(input("enter amount to be withdraw:"))
        b1.withdraw(w)
    elif choice == 3:
        b1.display()
    elif choice == 4:
        print("exit")
        break
    else:
        print("enter a valid choice")
        

        
