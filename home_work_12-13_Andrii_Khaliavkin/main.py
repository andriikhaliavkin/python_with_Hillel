# Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати тільки обʼєкти класу int або float
# Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point). Реалізуйте перевірку даних, аналогічно до класу Line.
# Визначет атрибут, що містить площу трикутника (за допомогою property). Для обчислень можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self._x = value
        else:
            raise TypeError('x must be int or float')

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self._y = value
        else:
            raise TypeError('y must be int or float')


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @property
    def p1(self):
        return self._p1

    @p1.setter
    def p1(self, value):
        if isinstance(value, Point):
            self._p1 = value
        else:
            raise TypeError('p1 must be Point')

    @property
    def p2(self):
        return self._p2

    @p2.setter
    def p2(self, value):
        if isinstance(value, Point):
            self._p2 = value
        else:
            raise TypeError('p2 must be Point')

    @property
    def length(self):
        return ((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    @property
    def p1(self):
        return self._p1

    @p1.setter
    def p1(self, value):
        if isinstance(value, Point):
            self._p1 = value
        else:
            raise TypeError('p1 must be Point')

    @property
    def p2(self):
        return self._p2

    @p2.setter
    def p2(self, value):
        if isinstance(value, Point):
            self._p2 = value
        else:
            raise TypeError('p2 must be Point')

    @property
    def p3(self):
        return self._p3

    @p3.setter
    def p3(self, value):
        if isinstance(value, Point):
            self._p3 = value
        else:
            raise TypeError('p3 must be Point')

    @property
    def area(self):
        a = Line(self.p1, self.p2).length
        b = Line(self.p2, self.p3).length
        c = Line(self.p3, self.p1).length
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.area > other.area

    def __ge__(self, other):
        return self.area >= other.area

    def __lt__(self, other):
        return self.area < other.area

    def __le__(self, other):
        return self.area <= other.area

    def __str__(self):
        return f'{self.p1.x}, {self.p1.y} -- {self.p2.x}, {self.p2.y} -- {self.p3.x}, {self.p3.y}'

# Доопрацюйте класс Triangle наступним чином:
# обʼєкти классу Triangle можна порівнювати між собою (==, !=, >, >=, <, <=) за площею.
# перетворення обʼєкту классу Triangle на стрінг показує координати його вершин у форматі x1, y1 -- x2, y2 -- x3, y3

print(Triangle(Point(0, 0), Point(0, 1), Point(1, 0)).area)
print(Triangle(Point(0, 0), Point(0, 1), Point(1, 0)) == Triangle(Point(0, 0), Point(0, 1), Point(1, 0)))
print(Triangle(Point(0, 0), Point(0, 1), Point(1, 0)) != Triangle(Point(0, 0), Point(0, 1), Point(1, 0)))
print(Triangle(Point(0, 0), Point(0, 1), Point(1, 0)) > Triangle(Point(0, 0), Point(0, 1), Point(1, 0)))
print(Triangle(Point(0, 0), Point(0, 1), Point(1, 0)) >= Triangle(Point(0, 0), Point(0, 1), Point(1, 0)))
print(Triangle(Point(0, 0), Point(0, 1), Point(1, 0)) < Triangle(Point(0, 0), Point(0, 1), Point(1, 0)))
print(Triangle(Point(0, 0), Point(0, 1), Point(1, 0)) <= Triangle(Point(0, 0), Point(0, 1), Point(1, 0)))
print(Triangle(Point(0, 0), Point(0, 1), Point(1, 0)))



