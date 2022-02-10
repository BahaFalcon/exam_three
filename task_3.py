class Rectangle:
    """
    создаем класс прямоугольник
    """
    def __init__(self, length: int, width: int) -> None:
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length > 0:
            self.__length = length
        else:
            print(f'Недопустимое значение!')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width > 0:
            self.__width = width
        else:
            print(f'Недопустимое значение!')


    def calculate_volume(self):
        return self.__length * self.__width

    def celc_perimetr(self):
        return (self.__length + self.__width) * 2

r = Rectangle(12, 15)
print(r.celc_perimetr())
r.width = 45
print(r.calculate_volume())