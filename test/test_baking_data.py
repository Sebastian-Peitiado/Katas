import pytest

class Account ():

    ALERT = "You cant withdraw money when theres no money in the account"
    BALANCE = 0
    INVALID_FORMAT = "Strings are not allowed"
    NO_NEGATIVE_NUMBERS = "Negative numbers are not allowed"

    def deposit(self, amount):
        
        if not isinstance(amount, (int, float)) :
            raise ValueError(self.INVALID_FORMAT)
        if amount < 0:
            raise ValueError(self.NO_NEGATIVE_NUMBERS)
        self.BALANCE += amount
        
    def get_balance(self):
        return self.BALANCE
  
    def withdraw(self, amount):
        if amount > self.BALANCE: 
            raise ValueError(self.ALERT)
        self.BALANCE-= amount
        

def test_succesful_deposit():
    #arrange
    account = Account()
    #act
    account.deposit(500)
    #assert
    balance = account.get_balance()
    assert balance == 500

def test_invalid_deposit():
    account = Account()
    with pytest.raises(Exception, match=account.INVALID_FORMAT):
        account.deposit("500")

def test_no_negatives_number():
    account = Account()
    with pytest.raises(Exception, match=account.NO_NEGATIVE_NUMBERS):
        account.deposit(-100)
    
def test_withdraw_money_with_no_cash():
    account = Account()
    with pytest.raises(Exception, match=account.ALERT):
        account.withdraw(100)

def test_succesful_withdraw():
    account = Account()
    account.deposit(1000)
    account.withdraw(100)
    assert account.get_balance() == 900