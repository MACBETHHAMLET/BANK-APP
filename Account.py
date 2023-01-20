class Account(object):
    def __init__(self, account_number, initial_amount=0):

        self.account_number = account_number
        self.balance = initial_amount

    def change_balance(self, change_value):
        temp = self.balance + change_value
        if temp >= 0:
            self.balance = temp
            return True
        else:
            return False

    def get_balance(self,):
        return self.balance
