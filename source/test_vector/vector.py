from math import hypot


class Vector:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __abs__(self):
        return hypot(self.__x, self.__y)

    def __repr__(self):
        return 'Vector({0}, {1})'.format(self.x, self.y)
