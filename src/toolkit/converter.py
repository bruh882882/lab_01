from toolkit.errors import ConverterError

length_units = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000.0}
mass_units = {'g': 0.001, 'kg': 1.0}
temperature_units = {'c', 'f', 'k'}

def convert(val: float, unit_1: str, unit_2: str):
    unit_1 = unit_1.lower() #регистр не учитывается
    unit_2 = unit_2.lower() #регистр не учитывается

    all_units = set(length_units.keys()) | set(mass_units.keys()) | temperature_units
    if unit_1 not in all_units or unit_2 not in all_units:
        raise ConverterError("Неизвестная единица измерения")

    if unit_1 in length_units and unit_2 in length_units:
        value_in_meters = val * length_units[unit_1]
        return round(float(value_in_meters / length_units[unit_2]), 10)

    elif unit_1 in mass_units and unit_2 in mass_units:
            value_in_kilos = val * mass_units[unit_1]
            return round(float(value_in_kilos / mass_units[unit_2]), 10)

    elif unit_1 in temperature_units and unit_2 in temperature_units:
        if unit_1 == 'k':
             temp_in_kelvin = val
        elif unit_1 == 'c':
             temp_in_kelvin = val + 273.15
        elif unit_1 == 'f':
             temp_in_kelvin = (val - 32) * 5 / 9 + 273.15

        if temp_in_kelvin < 0:
             raise ConverterError("Температура ниже 0 запрещена")

        if unit_2 == 'k':
             return round(float(temp_in_kelvin), 5)
        elif unit_2 == 'c':
             return round(float(temp_in_kelvin - 273.15), 5)
        elif unit_2 == 'f':
             return round(float((temp_in_kelvin - 273.15) * 9 /5 + 32), 5)

    else: 
         raise ConverterError("Конвертация между разными группами запнрещена")