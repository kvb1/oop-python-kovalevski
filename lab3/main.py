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
