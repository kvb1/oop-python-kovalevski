class Laptop:
    """Описывает ноутбук, его память, батарею и подключение к зарядке."""

    count = 0

    def __init__(self, model, ram_gb, battery, charging):
        if type(model) != str or model == "":
            raise ValueError(f"model = {model!r}: нужна непустая строка")
        if type(ram_gb) != int or not 4 <= ram_gb <= 128:
            raise ValueError(f"ram_gb = {ram_gb}: нужно целое от 4 до 128")
        if type(charging) != bool:
            raise ValueError(f"charging = {charging}: нужно True или False")
        self.model = model
        self.ram_gb = ram_gb
        self.battery = battery
        self.charging = charging
        Laptop.count += 1

    def work(self, hours):
        if type(hours) not in (int, float) or not hours > 0:
            raise ValueError(f"hours = {hours}: нужно положительное число")
        expense = 15 * hours
        if expense > self.battery:
            raise ValueError(
                f"hours = {hours}: заряда {self.battery}% не хватит"
            )
        self.battery = self.battery - expense

    def hours_left(self):
        return round(self.battery / 15, 1)

    def __str__(self):
        if self.charging:
            state = "заряжается"
        else:
            state = "не заряжается"
        return (
            f"Ноутбук {self.model}: ОЗУ {self.ram_gb} ГБ, "
            f"заряд {self.battery} %, {state}"
        )

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        if type(value) not in (int, float) or not 0 <= value <= 100:
            raise ValueError(f"battery = {value}: допустимо от 0 до 100")
        self._battery = value
