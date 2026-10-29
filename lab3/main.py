print("\nЗадание 4. Проверка данных")
try:
    Laptop("", 16, 80, False)
except ValueError as error:
    print("Ошибка:", error)

try:
    Laptop("test", 2, 80, False)
except ValueError as error:
    print("Ошибка:", error)

try:
    Laptop("test", 16, 120, False)
except ValueError as error:
    print("Ошибка:", error)

print("Счётчик после ошибочных попыток:", Laptop.count)

python lab3\main.py
print("\nЗадание 5. Методы")
print("До работы:")
print(laptop1)
laptop1.work(2)
print("После двух часов работы:")
print(laptop1)
print("Осталось часов:", laptop1.hours_left())
try:
    laptop1.work(10)
except ValueError as error:
    print("Ошибка:", error)
print("\nЗадание 6. Свойство battery")
print("Текущий заряд:", laptop1.battery)
laptop1.battery = 90
print("После присваивания:", laptop1.battery)
try:
    laptop1.battery = 150
except ValueError as error:
    print("Ошибка:", error)
print("\nЗадание 7. Итог")
laptop3 = Laptop("laptop-final", 32, 100, True)
print(laptop3)
print("Итоговое количество объектов:", Laptop.count)
