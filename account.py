
class Account:
    def __init__(self, name: str) -> None:  # TODO: give the ability to accept a different account balance then 0
        """
        This function 'sets up' the account setting its name(an argument) and its amount(0)
        :param name: This is what the account name will be set to
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        This function increases the account balance by the specified amount as long as it is greater than 0
        :param amount: This is the amount the balance will increase by (amount > 0)
        :return: result of the deposit attempt returns false if amount is <= 0 (bool)
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        This function decreases the account balance by the specified amount as long as it is greater than 0 and the
         decrease doesn't leave the balance < 0
        :param amount: This is the amount the balance will increase by (amount > 0)
        :return: Determines weather the withdrawal was successful (bool)
        """
        if self.__account_balance - amount < 0 or amount <= 0:
            return True
        else:
            self.__account_balance += -1*amount
            return True

    def get_name(self) -> str:
        """
        This function returns the name of the account
        :return: returns the name(str)
        """
        return self.__account_name

    def get_balance(self) -> float:
        """
        This function returns the name of the account
        :return: returns the account balance(float)
        """
        return self.__account_balance
