class Atm(object):
    def __init__(self,atmNumber,pinNumber):
        self.atmNumber = atmNumber
        self.pinNumber = pinNumber

    def CashWithDrawal(self, amount):
        balance = 100000-amount
        print("You have withdrawn ", amount,". Your balance is  " ,balance  )

    def BalanceEnquiry(self):
        print("Balance is 100000 ")

    def CashDeposit(self, amount):
        total = 100000+amount
        print("You have deposited ", amount,". Your balance is  " ,total  )


def main():
    card = input("Enter the card number: ")
    pin= input("Enter the pin number: ")
    user = Atm(card,pin)
    print("1.balace enquiry     2.withdrawal    3.cash deposit")
    activity = int(input("Enter your activity number: "))
    if (activity==1):
        user.BalanceEnquiry()
    elif (activity==2):
        amount=int(input("Enter the amount: "))
        user.CashWithDrawal(amount)
    elif (activity==3):
        amount=int(input("Enter the amount: "))
        user.CashDeposit(amount)
    else:
        print("Enter a valid number")

main()
    
