# %%
"""
Удав Анатолий любит французские багеты. Длина французского
багета равна 1 метру. За один заглот Удав Анатолий заглатывает
кусок случайной длины равномерно распределенной на отрезке
[0; 1]. Для того, чтобы съесть весь багет удаву потребуется случайное
количество N заглотов.

Оцените P(N=2), P(N=3), E(N)
"""

# %%
import numpy as np
import pandas as pd
from random import uniform

# %%
uniform(a=0, b=1)
list(range(7))

# %%
def eat_baget():
    """
    Симулятор удава Анатолия.
    Возвращает число укусов, потребовавшееся на один багет.
    """
    n_ukusov = 0
    baget = 1
    while baget > 0:
        zaglot = uniform(a=0, b=1)
        baget -= zaglot
        n_ukusov += 1
    return n_ukusov

# %%
eat_baget()

# %%
n_exp = 1000
udaff_life = [eat_baget() for i in range(n_exp)]
udaff_life

EN_hat = np.mean(udaff_life)
EN_hat

PNeq2_hat = udaff_life.count(2) / n_exp
PNeq2_hat

PNeq3_hat = udaff_life.count(3) / n_exp
PNeq3_hat


# %%
"""
Гюрза Леопольдина подбрасывает кубик до первой шестёрки. 
Обозначим: величина N — число бросков. 
Событие A — при подбрасываниях выпадала только чётная грань.

Оцените P(N=2), P(N=3), E(N)

Оцените P(A), P(N=2|A), P(A|N=2), P(A OR N=2), P(A AND N=2)
"""


# %%
from random import randint

# %%
randint(a=1, b=2)

# %% 
7 // 2

# %%
7 % 2

def throw_until_six():
    """
    Подбрасываем кубик до первой шестёрки. 
    Считаем число бросков. И следим за тем, выпадали ли только четные числа.
    Возвращает: (число бросков, True/False)
    """
    n_broskov = 0
    tolko_chet = True
    brosok = -1 # вымышленный бросок, только чтобы зайти в цикл
    while brosok < 6:
        brosok = randint(1, 6)
        n_broskov += 1
        if brosok % 2 == 1:
            tolko_chet = False
    return (n_broskov, tolko_chet)

# %%
throw_until_six()

n_exp = 1000
throw_list = [throw_until_six() for i in range(n_exp)]
throw_list

# %%
throw_df = pd.DataFrame(throw_list, columns=['n_throw', 'only_even'])
throw_df.describe()

# %%
"""
Накануне войны Жестокий Тиран очень большой страны издал
указ. Отныне за каждого новорождённого мальчика семья получает
денежную премию, но если в семье рождается вторая девочка, то
всю семью убивают. Бедные жители страны запуганы и остро
нуждаются в деньгах, поэтому в каждой семье дети будут появляться
до тех пор, пока не родится первая девочка.

а) Каким будет среднее число детей в семье?
б) Какой будет доля мальчиков в стране?
в) Какой будет средняя доля мальчиков в случайной семье?
г) Сколько в среднем мальчиков в случайно выбираемой семье?
"""