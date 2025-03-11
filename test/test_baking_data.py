import pytest

class Account ():

    BALANCE = 0
    INVALID_FORMAT = "Strings are not allowed"

    def deposit(self, amount):
        self.BALANCE+= amount
    
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
