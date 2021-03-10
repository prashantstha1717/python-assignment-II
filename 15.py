# 15. Imagine you are designing a banking application. What would a customer look like? What attributes would she have?
# What methods would she have?

class Customer():
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def customer_detail(self):
        print('Perosnal details')
        print('Firstname: ', self.firstname)
        print('Lastname: ', self.lastname)
        print('Age: ', self.age)
        print('Gender: ',self.gender)


customer1 = Customer('Prashant', 'Shrestha', 19, 'Male')
customer2 = Customer('Sita', 'Pokhrel', 15, 'Female')
customer1.customer_detail()
customer2.customer_detail()


class Bank(Customer):
    def __init__(self, firstname, lastname, age, gender):
        super().__init__(firstname,lastname,age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f'Account balance has been deposited by : {self.balance}')


customer1 = Bank('Prashant', 'Shrestha', 19, 'Male')
customer2 = Bank('Sita', 'Pokhrel', 15, 'Female')
customer1.deposit(500)
print(f'{customer1.firstname} has amount of Rs.{customer1.balance}.')
print(f'{customer2.firstname} has amount of Rs.{customer2.balance}.')




