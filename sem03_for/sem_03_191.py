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
import pandas as pd
import numpy as np

from random import uniform
from random import randint

# %% 
uniform(a=0, b=1)

# %%
randint(a=1, b=10)


# %%
def esh_baget():
    """
    Симулятор жизни удава Анатолия. 
    Возвращает число укусов, потребовавшееся, чтобы съесть один батон.
    """
    baget = 1
    n_ukusov = 0
    while baget > 0:
        ukus = uniform(a=0, b=1)
        baget -= ukus
        n_ukusov += 1
    return n_ukusov

# %%
esh_baget()

# %%
n_exper = 100000
# list(range(10))
exper = [esh_baget() for i in range(n_exper)]
exper

# %%
# estimate P(N=2), P(N=3), E(N)
PNeq2_hat = exper.count(2) / n_exper
PNeq2_hat

# %%
PNeq3_hat = exper.count(3) / n_exper
PNeq3_hat

# %%
np.mean(exper)

# Удав Анатолий благодарит за обед!


# %%
"""
Гюрза Леопольдина подбрасывает кубик до первой шестёрки. 
Обозначим: величина N — число бросков. 
Событие A — при подбрасываниях выпадала только чётная грань.

Оцените P(N=2), P(N=3), E(N)

Оцените P(A), P(N=2|A), P(A|N=2), P(A OR N=2), P(A AND N=2)
"""


# %%
def bros_kubiki():
    """
    Симулятор жизни гюрзы Клавдии. Подбрасываем кубик до первой шестёрки.
    Считаем число бросков и следим, выпадала ли только чётная грань. 
    Функция возвращает (число бросков, True/False)
    """
    n_broskov = 0
    tolko_chet = True
    brosok = -1 # вымышленный бросок, чтобы зайти внутрь цикла
    while brosok < 6:
        brosok = randint(a=1, b=6)
        n_broskov += 1
        if brosok % 2 == 1:
            tolko_chet = False
    return (n_broskov, tolko_chet)

# %%
bros_kubiki()


# %%
n_exper = 10000
exper = [bros_kubiki() for i in range(n_exper)]

# %%
exper[0:10]

# %%
exper_df = pd.DataFrame(exper, columns=['chislo_broskov', 'tolko_chet'])

exper_df

# %%
exper_df['chislo_broskov'].mean()

# %%
exper_A_happened = exper_df.query('tolko_chet == True')
exper_A_happened

# %%
exper_A_happened['chislo_broskov'].mean()


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