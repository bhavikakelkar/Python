
# Bank Management Program

class Bank:

    def __init__(self):
        self.accountno = -1
        self.name = ''
        self.deposit = -1
        self.__di = {}                             # hidden dictionary and set
        self.__se = set()

    def checkaccount(self):
        if self.accountno in self.__se:
            return True
        else:
            return False


    def newaccount(self):
        self.accountno = int(input("Enter Account Number "))
        ch = self.checkaccount()

        while(ch == True):
            print("Account Number is already present ")
            self.name = str(input("Enter your name "))
            if((self.__di[self.accountno])[0]== self.name):
                print("Your Account is already present ")
                return None
            else:
                self.accountno = int(input("Try with different account number "))
                ch = self.checkaccount()

        self.name = str(input("Enter your name "))
        self.deposit = int(input("Enter initial amount >=500 "))
        self.__di[self.accountno]=[self.name,self.deposit]
        self.__se.add(self.accountno)
        print("Your Account is Created ")

    def depositamount(self):
        self.accountno = int(input("Enter account number "))
        ch = self.checkaccount()
        if(ch==True):
            self.deposit = int(input("Enter amount to be deposited "))
            (self.__di[self.accountno])[1] += self.deposit
            print("Amount is deposited ")
        else:
            print("Account is not present")

    def withdrawamount(self):
        self.accountno = int(input("Enter account number "))
        ch = self.checkaccount()
        if(ch==True):
            print("Amount present in your account : ",(self.__di[self.accountno])[1])
            self.deposit = int(input("Enter amount to withdraw "))

            while(self.deposit>(self.__di[self.accountno])[1]):
                print("Not Possible. Enter again ")
                self.deposit = int(input("Enter amount to withdraw "))

            (self.__di[self.accountno])[1] -= self.deposit
            print(" Process is done ")
        else:
            print("Account is not present")


    def accountdetails(self):
        self.accountno = int(input("Enter account number "))
        ch = self.checkaccount()
        if (ch == True):
            print("Account no.:",self.accountno,end=" ** ")
            print("Name:",(self.__di[self.accountno])[0],end=" ** ")
            print("Amount:",(self.__di[self.accountno])[1])
        else:
            print("Account is not present")


    def modifyaccount(self):
        self.accountno = int(input("Enter account number "))
        ch = self.checkaccount()
        if (ch == True):
            if(input("Do you want to change account name (y/n)")=='y'):
                self.name = str(input("Enter modified name "))
                (self.__di[self.accountno])[0]=self.name
            if(input("Do you want to deposit amount (y/n)")=='y'):
                self.depositamount()
            elif(input("Do you want to withdraw amount (y/n)") == 'y'):
                self.withdrawamount()
            print("Modification is done ")
            self.accountdetails()
        else:
            print("Account is not present")


    def accountholderlist(self):
        print("Account holder names :")
        for i in self.__se:
            print((self.__di[i])[0])

    def deletee(self):
        self.accountno = int(input("Enter account number "))
        ch = self.checkaccount()
        if (ch == True):
            del self.__di[self.accountno]
            self.__se.remove(self.accountno)
            print("Deletion is done")
        else:
            print("Account is not present")


def mainmenu():
    b = Bank()
    print("{0:^50}".format("BANK ACCOUNT"))
    print("MAINMENU")
    print("1. New Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Show Account Details")
    print("5. Modify Account Details")
    print("6. Show Account Holder List")
    print("7. Delete an Account")

    status = int(input("Enter your choice : (enter 0-quit)  "))

    while(status != 0):
        if status == 1:
            b.newaccount()
        elif status == 2:
            b.depositamount()
        elif status == 3:
            b.withdrawamount()
        elif status == 4:
            b.accountdetails()
        elif status == 5:
            b.modifyaccount()
        elif status  == 6:
            b.accountholderlist()
        elif status == 7:
            b.deletee()
        else:
            print("Invalid Input")
        status = int(input("Enter your choice : (enter 0 - quit)  "))



def main():
    mainmenu()


if __name__ == '__main__':
    main()