import numpy as np # математика + векторы
import pandas as pd # таблички
import seaborn as sns # графички

from scipy import special # спец функции

np.cos(7)

special.factorial(10)

True + True + True + False

True * True * False

'Привет, Орлы и Орлицы!' * 3

# сравнения

3 > 5
2 < 7 < 9
0.4 == 0.4
0.3 + 0.1 == 0.4
0.4 - 0.1 == 0.3

a = [3, 5, -3, -7, 1, 8, 9]

a[1:4]

b = [i ** 3 for i in a if i > 0]
b


b2 = [i ** 3 for i in a]
b2

special.binom(30, 3)

diam = sns.load_dataset('diamonds')

diam.head()
diam.tail()
diam.info()
diam.describe()

diam.shape
diam.columns

# добываю столбик
diam['carat']

# идея Алексея
berem_prime = diam[(diam['carat'] > 0.8) * (diam['price'] < 2000)]
# отбор строк (более читабельный)
berem = diam.query('carat > 0.8 & price < 2000')

berem.shape

# отбор столбцов
berem2 = berem.filter(['carat', 'price'])
berem2

# создать столбец
berem2['ln_price'] = np.log(berem2['price'])
berem2.head()
# через assign
berem3 = berem2.assign(
    ln_price = np.log(berem2['price']),
    carat2 = berem2['carat'] ** 2
)


diam.to_csv('diamonds_data.csv')

new = pd.read_csv('diamonds_data.csv')
new.head()

import this







