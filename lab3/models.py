class Laptop:
    """Описывает ноутбук, его память, батарею и подключение к зарядке."""

    count = 0

    def __init__(self, model, ram_gb, battery, charging):
        self.model = model
        self.ram_gb = ram_gb
        self.battery = battery
        self.charging = charging
        Laptop.count += 1

notepad lab3\main.py
from models import Laptop


print("Задание 3. Создание объектов")
laptop1 = Laptop("laptop-kovalevski", 16, 80, False)
laptop2 = Laptop("laptop-test", 8, 45, True)
print(laptop1.model, laptop1.ram_gb, laptop1.battery, laptop1.charging)
print(laptop2.model, laptop2.ram_gb, laptop2.battery, laptop2.charging)
print("Создано объектов:", Laptop.count)
