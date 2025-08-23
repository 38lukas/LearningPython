class TemperatureConverter:

    @staticmethod
    def convert_temperature(p_temperature) -> float | None:
        """
        Converts a temperature string from °C to °F or vice versa.
        :param p_temperature: str, temperature with unit, e.g., "36°C" or "100°F"
        :return: float, converted temperature
        """

        if "°C" in p_temperature:
                format_temperature = float(p_temperature.replace("°C", ""))
                return round((format_temperature * 9/5) + 32 , 2)
        elif "°F" in p_temperature:
            format_temperature = float(p_temperature.replace("°F", ""))
            return round((format_temperature - 32) * 5/9, 2)
        else:
            print("Wrong input!")
            return None

if __name__ == "__main__":
    while True:
        temperature = input("Type in the first Temperature (°F or °C):  ")
        result = TemperatureConverter.convert_temperature(temperature)

        if result != None:
            print(result)
            break
