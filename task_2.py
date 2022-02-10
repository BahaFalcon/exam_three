class Lemonade:
    def __init__(self, ingredient: str):

        self.__ingredient = ingredient

    @property
    def ingredient(self):
        return self.__ingredient

    @ingredient.setter
    def ingredient(self, ingredient):
        if isinstance(ingredient, str):
            self.__ingredient = ingredient
        else:
            self.__ingredient = None


    def show_my_drink(self):
        if self.ingredient:
            print(f'Лемонад и {self.__ingredient}')
        else:
            print('Обычная газировка')

soda = Lemonade('apple')

soda.show_my_drink()