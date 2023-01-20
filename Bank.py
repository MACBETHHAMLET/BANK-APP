from Account import Account
from Customer import Customer


class Bank(object):

    def __init__(self, customersList=[], loginCustomer=None):
        # Load from the text file
        lines = []
        self.customersList = []
        with open('testfile.txt', 'r') as f:
            lines = f.readlines()
        for Line in lines:
            LineParts = Line.split(sep="#")
            # Extract Customer Info
            CustomerInfo = LineParts[0]
            CustomerInfoParts = CustomerInfo.split("/")
            # Create AccountList
            AccountList = []
            if len(LineParts) > 1:
                AccountsInfo = LineParts[1]
                AccountsInfoSeparated = AccountsInfo.split("@")

                for item in AccountsInfoSeparated:
                    accountInfo = item.split('/')
                    temp = Account(accountInfo[0], int(accountInfo[1]))
                    AccountList.append(temp)
            ResultedCustomer = Customer(
                CustomerInfoParts[0], CustomerInfoParts[1], AccountList)
            self.customersList.append(ResultedCustomer)

        # Add input customer list to the created one by the text file.
        if customersList != []:
            self.customersList += customersList
        # Set logged in customer
        self.loginCustomer = loginCustomer

    def get_customers(self):
        return self.customersList

    def get_customer(self, username):
        temp = None
        for customer in self.customersList:
            if customer.username == username:
                temp = customer
                break
        return (temp)

    def add_customer(self, username, password):
        temp = self.get_customer(username)
        if temp == None:
            self.customersList.append(Customer(username, password))
            return True
        else:
            print("This username is already existed")
            return False

    def change_customer_password(self, username, new_password):
        temp = self.get_customer(username)
        if (temp != None):
            if new_password == temp.password:
                print("you need to write a new password")
                return False
            else:
                temp.password = new_password
                return True
        else:
            print(f"there is no customer with the name of {username}")
            return False

    def remove_customer(self, username):
        temp = self.get_customer(username)
        if temp != None:
            self.customersList.remove(temp)
            return True
        else:
            print(f"there is no customer with {username}")
            return False

    def login(self, username, password):
        temp = self.get_customer(username)
        if temp != None:
            if temp.check_password(password):
                self.loginCustomer = temp
                return True
            else:
                print("your password is wrong")
                return False
        else:
            print(f"there is no customer with {username}")
            return False

    # Applied on the logged in customer
    def logout(self):
        if self.loginCustomer != None:
            self.loginCustomer = None
            return True
        else:
            print("There is no logged in customer")
            return False

    # Applied on the logged in customer ###check wether there is loggedin customer or not ### self.loginCustomers == None
    def get_account(self):
        if self.loginCustomer != None:
            return self.loginCustomer.customerAccountsList
        else:
            print("There is no logged in customer")
            return False

    # Applied on the logged in customer ###check wether there is loggedin customer or not ### self.loginCustomers == None
    def deposit(self, account_number, amount):
        if self.loginCustomer != None:
            if self.loginCustomer.deposit(account_number, amount):
                return True
            else:
                return False
        else:
            print("There is no logged in customer")
            return False

    # Applied on the logged in customer
    def withdraw(self, account_number, amount):
        if self.loginCustomer != None:
            if self.loginCustomer.withdraw(account_number, amount):
                return True
            else:
                return False
        else:
            print("There is no logged in customer")
            return False

    def __del__(self):
        # Write the customer data to file
        with open("testfile.txt", "w") as f:
            lines = []
            for customer in self.customersList:
                # Create customer info part
                ResultedString = f"{customer.username}/{customer.password}#"
                # Create the account info part
                for account in customer.customerAccountsList:
                    temp = f"{account.account_number}/{account.balance}@"
                    ResultedString += temp
                ResultedString = ResultedString[:-1]
                lines.append(ResultedString)
            f.write('\n'.join(lines))
