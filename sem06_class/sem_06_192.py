
class dual:
    """
    Класс прикольных дуальных чисел
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        if isinstance(other, dual):
            return dual(self.a + other.a, self.b + other.b)
        return dual(self.a + other, self.b)
    def __radd__(self, other):
        if isinstance(other, dual):
            return dual(self.a + other.a, self.b + other.b)
        return dual(self.a + other, self.b)
    def __repr__(self):
        text = 'дуальное число ' + str(self.a) + \
            '+' +  str(self.b) + 'e'
        return text
    def __mul__(self, other):
        if isinstance(other, dual):
            a = self.a * other.a
            b = self.a * other.b + self.b * other.a
            return dual(a, b)
        return dual(self.a * other, self.b * other)
    def __rmul__(self, other):
        if isinstance(other, dual):
            a = self.a * other.a
            b = self.a * other.b + self.b * other.a
            return dual(a, b)
        return dual(self.a * other, self.b * other)

dual(6, 5) * dual(3, 4)
dual(6, 5) * 5
5 * dual(6, 5)
dual(3, 4) + dual(5, 6)
dual(3, 4) + 9
9 + dual(3, 4)
dual(1, 3) * dual(2, -1)


isinstance(dual(7, 0), dual)
isinstance(7, dual)

x = dual(7, 3)
x
x.a
y = dual(7, 3) + dual(-2, 5)

y.b

'dsf' + str(7)

dual(7, 3).__add__(dual(8, 2))

import math

def exp(x):
    """
    Обобщаем exp на случай дуальных чисел
    """
    if isinstance(x, dual):
        return dual(math.exp(x.a), math.exp(x.a) * x.b)
    return math.exp(x)

exp(7)

exp(dual(7, 3))
dual(6, 5) + dual(3, 4)
dual(6, 5) + 9


def f(x):
    return x * x * x

def f2(x):
    return exp(exp(x) + 2 * x) + exp(x * x + 6 * x)


def derivator(fun, point):
    """
    автоматическое дифференцирование функции в точке
    """
    dual_res = fun(dual(point, 1))
    return dual_res.b


derivator(f, 1)
derivator(f2, 0)
exp(5)


f2(dual(2, 1))


def cos(x):
    """
    Обобщаем cos на случай дуальных чисел
    """
    if isinstance(x, dual):
        return dual(math.cos(x.a), -math.sin(x.a) * x.b)
    return math.cos(x)


cos(dual(3, 2))

cos(dual(0, 1))

def f3(x):
    return cos(exp(cos(x * x)))

f3(2)

f3(dual(2, 1))

derivator(cos, math.pi / 2)