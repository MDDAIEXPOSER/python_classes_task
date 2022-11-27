class Account:
    def __init__(self, name, id, passwD, accountBalance):
        self._name = name
        self.__accountBalance = accountBalance
        self.__id = id
        self.__passwD = passwD

    def get_accbalance(self):
        return self.__accountBalance

    def set_accbalance(self, new_accountBalance):
        self.__accountBalance = new_balance

    def get_accpassword(self):
        return self.__passwD

    def get_id(self):
        return self.__id

    def set_id(self, new_id, passwD):
        if passwD == self.get_accpassword():
            self.__id = new_id
            print('успешно изменен')
        else:
            print('Не тот пароль')

    def del_id(self, passwD):
        if id == self.get_accpassword():
            del self.__id
            print('паспорт удален')
        else:
            print('Не тот пароль')

    def change_accbalance(self, new):
        if self.__accountBalance + new >= 0:
            self.__accountBalance += new
            print(f'balance: {self.get_accbalance()}')
        else:
            print('Balance < 0 !!!')
