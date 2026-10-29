class Laptop:
    """Описывает ноутбук, его память, батарею и подключение к зарядке."""

    count = 0

    def __init__(self, model, ram_gb, battery, charging):
        if type(model) != str or model == "":
            raise ValueError(f"model = {model!r}: нужна непустая строка")
        if type(ram_gb) != int or not 4 <= ram_gb <= 128:
            raise ValueError(f"ram_gb = {ram_gb}: нужно целое от 4 до 128")
        if type(battery) != int or not 0 <= battery <= 100:
            raise ValueError(f"battery = {battery}: нужно целое от 0 до 100")
        if type(charging) != bool:
            raise ValueError(f"charging = {charging}: нужно True или False")
        self.model = model
        self.ram_gb = ram_gb
        self.battery = battery
        self.charging = charging
        Laptop.count += 1
