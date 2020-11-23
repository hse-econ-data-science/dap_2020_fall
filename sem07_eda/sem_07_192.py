import numpy as np
import pandas as pd
import seaborn as sns


v = [4, 5, 6, 8]

va = np.array(v)
va

zoo = [4, 'Привет', np.cos]

zoo_a = np.array(zoo)
zoo_a

va[2]

va.reshape((2, 2))



va.reshape((-1, 2))

?np.random

va[:-1]

np.max(va[:-1] == 5)


def zad1(x):
    zeros = (x[:-1] == 0)
    if np.max(zeros):
        zeros_shifted = np.insert(zeros, 0, False)
        elements_to_compare = x[zeros_shifted]
        return np.max(elements_to_compare)
    return None



def zad1b(x):
    """
    Возвращает максимальный элемент из тех, что идут за нулём.
    Если такой есть. Иначе None.
    """
    if len(x) == 1:
        return None
    zeros = (x[:-1] == 0)
    if np.max(zeros):
        elements_to_compare = x[1:][zeros]
        return np.max(elements_to_compare)
    return None


np.array([7]))

len(x)
print(zad1b(np.array([6, 7, 8, 7, 6])))


x = np.array([4, 5, 6, 7, 0])
print(zad1(x))


x = np.array([4, 5, 6, 7, 0, 8, 0, 9, 3])
zeros = (x[:-1] == 0)
zeros


flag = np.array([True, False, True, False])


v = [4, 5, 6, 8]

va = np.array(v)
va


va[flag]
va[[0, 3]]

np.array(5) + va
np.array([5, va])

5 + va
np.array(5, va)


np.insert(va, 0, 42)

np.concatenate(([False], va))