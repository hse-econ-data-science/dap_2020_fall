import numpy as np # математика + массивы
from scipy import special # спец функции (редкие)
import pandas as pd # таблички
import seaborn as sns # графики

np.cos(0)

special.factorial(10)

special.binom(10, 2)

# сравнения

4 < 5

3 + 1 == 4

0.3 + 0.1 == 0.4
0.4 - 0.1 == 0.3

1 < 5 < 7

a = [4, 5, 7, 8, -1, 17, 32, 9]
a[2:5]


b = [i ** 2 for i in a if i > 0]

def my_square(x=0):
    """
    Эта функция возводит в квадрат!

    Аргументы:
    x - что хотим возвести

    Результат:
    квадрат исходного числа
    """
    y = x ** 2

    return y

my_square(7)

# data = pd.read_csv('имя файла')

diam = sns.load_dataset('diamonds')

diam.head()
diam.tail()
diam.info()
diam.describe()
diam.shape
diam.columns

# действия с табличками

diam['price']

np.mean(diam['price'])
np.mean(diam['carat'])



berem = diam.query('price < 3900 & carat > 0.8')
berem.describe()

berem2 = diam.filter(['carat', 'price'])
berem2.head()


# популярный подход
berem['ln_price'] = np.log(berem['price'])
berem['ln_carat'] = np.log(berem['carat'])

berem.head()

berem3 = berem.assign(
    ln_price = np.log(berem['price']), 
    ln_carat = np.log(berem['carat']))
# поправьте ошибку :)
berem3.head()


berem3.to_csv('~/Downloads/sem_01/berem.csv', 
    index=False)
# найдите опцию, которая не сохраняет номера строк
data = pd.read_csv('~/Downloads/sem_01/berem.csv')
data.describe()

import this



