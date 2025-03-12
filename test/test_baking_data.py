import pytest

class Account ():

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