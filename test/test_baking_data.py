import pytest

class Account:

    ALERT = "You can't withdraw money when there's no money in the account"
    INVALID_FORMAT = "Strings are not allowed"
    NO_NEGATIVE_NUMBERS = "Negative numbers are not allowed"

    def __init__(self):
        self._balance = 0
        self.activo = True

    def _validate_amount(self, amount):
        """Método privado para validar la cantidad ingresada."""
        if not isinstance(amount, (int, float)):
            raise ValueError(self.INVALID_FORMAT)
        if amount < 0:
            raise ValueError(self.NO_NEGATIVE_NUMBERS)

    def deposit(self, amount):
        self._validate_amount(amount)
        self._balance += amount

    def withdraw(self, amount):
        self._validate_amount(amount)
        if amount > self._balance:
            raise ValueError(self.ALERT)
        self._balance -= amount
    
    def print_statement(self):
        pass

    def mostrar_menu(self):
        print("\n--- Menú de opciones ---")
        print("1. depositar")
        print("2. validar monto")
        print("3. extraer dinero")
        print("4. imprimir cuenta actual")
        print("5. Salir")
        
    def ejecucion(self):
        while self.activo:
            self.mostrar_menu()
            opcion = input("Que desea realizar: ")
            if opcion == "1":
                self.deposit()
            elif opcion == "2":
                self._validate_amount()
            elif opcion == "3":
                self.withdraw()
            elif opcion == "4":
                self.print_statement()
            elif opcion == "5":
                print("ha finalizado el programa")
                self.activo = False
            else:
                print("Opción no válida, volve a ingresar.")

            

    @property
    def get_balance(self):
        return self._balance


def main():
   account = Account()
   account.ejecucion()

if __name__ == "__main__":
    main()


def test_succesful_deposit():
    #arrange
    account = Account()
    #act
    account.deposit(500)
    #assert
    balance = account._balance
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
    assert account._balance == 900

def test_error_when_withdraw_is_a_negative_number():
    account = Account()
    with pytest.raises(Exception, match=account.NO_NEGATIVE_NUMBERS):
        account.withdraw(-100)

def test_error_when_withdraw_is_a_string_number():
    account = Account()
    with pytest.raises(Exception, match=account.INVALID_FORMAT):
        account.withdraw("500")