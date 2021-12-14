class Account:
    # Has attributes Acno, Password, Username, Balance
    def __init__(self, acno, password, username, balance):
        self.acno = acno
        self.password = password
        self.username = username
        self.bal = balance
        print(self.acno + " account is created")

    def printAccountDetails(self):
        print("Account Details are: ---------")
        print("Name: ", self.username)
        print("Account Number: ", self.acno)
        print("Balance: ", self.bal)
    
    def login(self, password):
        if(self.password == password):
            return 1
        else:
            return 0

# main

user1 = Account("AC01", "AC01Pass", "Rohith", 950.23)
user2 = Account("AC02", "AC02Pass", "Lalithej", 950.23)
user3 = Account("AC03", "AC03Pass", "Jaswanth", 950.23)

print("Weclome to the Bank Management program\n\n")

username = input("Username: ")
password = input("Password: ")

list = [user1, user2, user3]

for user in list:
    if(user.login(password) == 1):
        newUser = Account(user.acno, user.password, user.username, user.bal)
        newUser.printAccountDetails()

# for user in list:
#     user.printAccountDetails()