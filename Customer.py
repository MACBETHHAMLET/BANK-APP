from Account import Account


class Customer(object):
    def __init__(self, username, password, customerAccountsList=[]):
        # put some constraint on password and username
        self.username = username
        self.password = password
        self.customerAccountsList = customerAccountsList

    def check_password(self, password):
        if self.password == password:
            return True
        else:
            return False

    def add_account(self, newaccount):
        if type(newaccount) == Account:
            self.customerAccountsList.append(newaccount)
            return True
        return False

    def get_account(self, account_number):
        temp = None
        for account in self.customerAccountsList:
            if account.account_number == account_number:
                temp = account
                break
        return temp

    def deposit(self, account_number, amount):
        temp = None
        for account in self.customerAccountsList:
            if account.account_number == account_number:
                temp = account.change_balance(amount)
                break
        if temp != None:
            return True
        else:
            return False

    def withdraw(self, account_number, amount):
        temp = None
        for account in self.customerAccountsList:
            if account.account_number == account_number:
                temp = account.change_balance(-amount)
                break
        if temp != None:
            return True
        else:
            return False

    def print_customerAccounts_list(self):
        for account in self.customerAccountsList:
            print(
                f"Account number:{account.no} Account balance:{account.balance}")
