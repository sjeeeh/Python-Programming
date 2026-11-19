class BankAccount:
    def __init__(self, name, acc_no, acc_type,balance=0.0):
        self.name=name
        self.acc_no=acc_no
        self.acc_type=acc_type
        self.balance=balance
    def deposit(self,amount):
        if amount<=0:
            print("Invalid amount. Deposit must be greater than 0.")
            return
        self.balance+=amount
        print(f"Deposited {amount:.2f}. New Balance:{self.balance:.2f}")
    def withdraw(self,amount):
        if amount<=0:
            print("Invalid amount. Withdraw must be greater than 0.")
        elif amount>self.balance:
            print(f"Insufficient Balance. Available amount: {self.balance:.2f}")
        else:
            self.balance-=amount
            print(f"Withdraw {amount:.2f}. New Balance:{self.balance:.2f}")
    def display(self):
        print("\n----Account Details----")
        print(f"Depositor name : {self.name}")
        print(f"Account number : {self.acc_no}")
        print(f"Account type   : {self.acc_type}")
        print(f"Balance        : {self.balance}")
        print("-------------------------\n")
        
name=input("Enter depositor name: ")
acc_no=input("Enter Account no: ")
acc_type=input("Enter Account type(Saving/Current): ")
initial=float(input("Enter initial balance: "))

account=BankAccount(name,acc_no,acc_type,initial)

account.deposit(float(input("Enter amount to deposit: ")))
account.withdraw(float(input("Enter amount to withdraw: ")))
account.display()
