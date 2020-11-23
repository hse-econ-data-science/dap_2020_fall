import numpy as np
import pandas as pd
import seaborn as sns


x_list = [5, 6, 0, -3, 8, 0, 2, 0]
x = np.array(x_list)

x_list + 5
x + 5

x_list == 0
x == 0


x.reshape((2, 4))

x.reshape((4, 2))

x.reshape((2, 2, 2))


x.reshape((2, -1))

np.max(x)


def zad1(x):
    """
    Функция выбирает все элементы, идущие за нулём.
    Если таких нет, возвращает None.
    Если такие есть, то возвращает их максимум.
    """
    zeros = (x[:-1] == 0)  
    if np.sum(zeros):
        elements_to_compare = x[1:][zeros]
        return np.max(elements_to_compare)
    return None

def max_element_before_zero(x):
    shift_by_one = np.hstack((1, x))
    bool_array = (shift_by_one == 0)[:np.size(shift_by_one) - 1]
    if np.size(x[bool_array]) == 0:
        return None
    else:
        return np.max(x[bool_array])




x_list = [5, 6, 0, -3, 8, 0, 2, 0]
x = np.array(x_list)
zad1(x)

merzkiy = np.array([5])
y = np.array([5, 6, 7, 0, 8])
z = np.array([5, 6, 7, 0, 8, 0, 10, 0, -3, 0, 0])
w = np.array([3, 4, 5])

zad1(merzkiy)
zad1(y)
zad1(w)
zad1(z)

np.sum([True, False, True])


w[1]

w[[True, False, True]]

np.insert(w, 0, 42) # добавить элемент
x
x_bez_pervogo = x[1:]
x_bez_pervogo
zeros = [False, True, False, True, True, True, False]
x_bez_pervogo[zeros]

x[1:][zeros]