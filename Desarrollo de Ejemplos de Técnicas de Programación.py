class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # Método abstracto

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Uso de la abstracción
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f"{dog.name} hace: {dog.make_sound()}")
print(f"{cat.name} hace: {cat.make_sound()}")

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Variable protegida

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Fondos insuficientes")

    def get_balance(self):
        return self._balance

# Uso de la encapsulación
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)

print(f"Saldo actual: {account.get_balance()}")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def drive(self):
        return "Car is moving"

class Motorcycle(Vehicle):
    def wheelie(self):
        return "Motorcycle is doing a wheelie"

# Uso de la herencia
car = Car("Toyota")
motorcycle = Motorcycle("Harley Davidson")

print(f"{car.brand}: {car.start_engine()}. {car.drive()}")
print(f"{motorcycle.brand}: {motorcycle.start_engine()}. {motorcycle.wheelie()}")

class Shape:
    def area(self):
        pass  # Método abstracto

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Uso del polimorfismo
square = Square(5)
circle = Circle(3)

print(f"Área del cuadrado: {square.area()}")
print(f"Área del círculo: {circle.area()}")
#