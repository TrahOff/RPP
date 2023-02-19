class Vegetable:
    _shelf_life = "9 дней"

    def __init__(self, color, shape):
        self._shape = shape
        self._color = color

    def self_features(self):
        print(f"имеет {self._shape} форму и {self._color} цвет")

    @staticmethod
    def can_be_eaten():
        print("можно добавить в различные блюда!")

    def can_be_stored(self):
        print(f"может храниться {self._shelf_life}")


class Carrot(Vegetable):
    @staticmethod
    def feature():
        print("вытянутая и твёрдая. Растёт в земле.")

    @staticmethod
    def name():
        print("Морковь")
        

class Tomato(Vegetable):
    @staticmethod
    def feature():
        print("круглая и сочная. Растёт на кустах.")

    @staticmethod
    def name():
        print("Помидор")


def main():
    car = Carrot("оранжевый", "вытянутый конус")
    tom = Tomato("красный", "шар")
    for veg in (car, tom):
        veg.name()
        veg.feature()
        veg.self_features()
        veg.can_be_eaten()
        veg.can_be_stored()


if __name__ == "__main__":
    main()
