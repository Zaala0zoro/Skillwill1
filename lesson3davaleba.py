class Car:
    def __init__(self, brand, model, production_year, color, horse_power, is_sport_car=False):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car

    # Getter მეთოდები
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_production_year(self):
        return self.__production_year

    def get_color(self):
        return self.__color

    def get_horse_power(self):
        return self.__horse_power

    def get_is_sport_car(self):
        return self.__is_sport_car

    # მეთოდი ფერის ცვლილებისთვის
    def change_color(self, new_color):
        if self.__color.lower() != new_color.lower():
            self.__color = new_color
            return True
        return False

    # მეთოდი horse_power-ის გაზრდისთვის
    def increase_horse_power(self, hp):
        if hp > 0:
            self.__horse_power += hp
            return True
        return False


# კლასის ობიექტის შექმნის მაგალითი
my_car = Car("Toyota", "Corolla", 2020, "Red", 132)
print(my_car.get_brand())  # გამოსახულება იქნება "Toyota"
print(my_car.get_color())  # გამოსახულება იქნება "Red"

# ფერის ცვლილების ცდა
success = my_car.change_color("Blue")
print(success)  # გამოსახულება იქნება True
print(my_car.get_color())  # გამოსახულება იქნება "Blue"

# ფერის ცვლილების ცდა იგივე ფერზე
success = my_car.change_color("Blue")
print(success)  # გამოსახულება იქნება False

# horse_power-ის გაზრდის ცდა
success = my_car.increase_horse_power(10)
print(success)  # გამოსახულება იქნება True
print(my_car.get_horse_power())  # გამოსახულება იქნება 142

# არასწორი მნიშვნელობის horse_power-ის გაზრდის ცდა
success = my_car.increase_horse_power(-5)
print(success)  # გამოსახულება იქნება False
print(my_car.get_horse_power())  # გამოსახულება იქნება 142
