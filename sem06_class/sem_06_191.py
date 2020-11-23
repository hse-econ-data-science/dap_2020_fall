class dual:
    """
    Расчудесный класс дуальных чисел 
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        text = 'дуальное число ' + str(self.a) + \
            ' + ' + str(self.b) + 'e'
        return text
    def __add__(self, other):
        if isinstance(other, dual):
            return dual(self.a + other.a, self.b + other.b)
        return dual(self.a + other, self.b)
    def __radd__(self, other):
        if isinstance(other, dual):
            return dual(self.a + other.a, self.b + other.b)
        return dual(self.a + other, self.b)
    def __mul__(self, other):
        if isinstance(other, dual):
            new_a = self.a * other.a
            new_b = self.a * other.b + self.b * other.a
            return dual(new_a, new_b)
        return dual(self.a * other, self.b * other)
    def __rmul__(self, other):
        if isinstance(other, dual):
            new_a = self.a * other.a
            new_b = self.a * other.b + self.b * other.a
            return dual(new_a, new_b)
        return dual(self.a * other, self.b * other)
    def conj(self):
        return dual(self.a, -self.b)
    def __div__(self, other):
        if isinstance(other, dual):
            denom = other.a * other.a
            ...
            ...
        return dual(self.a / other, self.b / other)


5 + dual(3, 4)

dual(4, 5).conj()

dual(6, -3) * dual(3, 4)


x = dual(4, 5)
x
x.a
x.b
dual(4, 5) + dual(5, 6)
dual(4, 5) + 9
7 + dual(4, 5)

isinstance(x, dual)
isinstance(y, dual)
isinstance(7.5, dual)

y = dual(6, 7)
y.a
y.b

x + y


def f(x):
    return exp(6 * x * x * x) + exp(3 * x * x) + 5 * x

f(dual(0, 1))

import math

def exp(x):
    """
    Обобщение экспоненты на дуальные числа
    """
    if isinstance(x, dual):
        return dual(math.exp(x.a), x.b * math.exp(x.a))
    return math.exp(x)



def cos(x):
    """
    Обобщение косинуса на дуальные числа
    """
    if isinstance(x, dual):
        return dual(math.cos(x.a), -x.b * math.sin(x.a))
    return math.cos(x)

pi = math.pi
pi
cos(pi)
cos(dual(pi, pi))
derivator(cos, pi/2)


def h(x):
    return cos(exp(x * x + cos(3 * x)))

derivator(h, pi)


exp(dual(3, 4))
exp(3)


def derivator(fun, point):
    res_dual = fun(dual(point, 1))
    return res_dual.b

derivator(exp, 5)

exp(5)

def g(x):
    return x * x * x * x

g(1)

derivator(g, 1)


