import pandas as pd # таблички
import numpy as np # численные операции
import seaborn as sns # графички готовые
import matplotlib.pyplot as plt # графички из кирпичиков

diam = sns.load_dataset('diamonds')

# посмотреть
diam.shape
diam.head(3)
diam.tail(4)
diam.describe()
diam.info()
diam.describe(include='object')

# создание переменной, отбор строк, отбор столбцов
diam2 = (diam.filter(['x', 'y', 'z'])
    .query('x > 0.2')
    .assign(ln_x = np.log(diam['x']))
    .sort_values(by='x', ascending=False)
    .head(5)
    .rename(columns={'y': 'yyy'}))
diam2

diam3 = diam.rename(columns={'y': 'razmer_y'})
diam3

x = np.cos(56)
x

diam.filter(['x', 'y', 'z']).query('x > 0.2').assign(ln_x = np.log(diam['x'])).sort_values(by='x')

# как выстрелить себе в ногу!
diam.iloc[3:5, 1:3]

# действия со столбцом
diam['cut'].unique()
diam['cut'].nunique()
diam['cut'].value_counts()
diam['cut'].mode()
diam['price'].size


diam['x'].mode()
diam.head(10)
diam['x'].median()
diam['x'].mean()

diam4 = (diam.assign(
    price_cat = pd.cut(diam['price'], bins=3, 
        labels=['cheap', 'med', 'pricy']))
        .query('price_cat == "med"')
        .head(10))
diam4

# создать столбец на базе столбца
diam['price_cat'] = pd.cut(diam['price'], bins=3, 
        labels=['cheap', 'med', 'pricy'])
diam['cut2'] = diam['cut'].str.replace('Good', 'Bad')
diam.head(10)


diam4.head()

# https://xkcd.com/208/
diam.filter(regex='^c')
diam.filter(regex='ty$')
diam.filter(regex='^[cx]')
diam.filter(regex='^[a-t]a')


diam5 = (diam.groupby('cut')
    .agg(av_price = ('price', np.mean),
        min_price = ('price', np.min),
        max_price = ('price', np.max),
        n_obs = ('price', 'size'))
    .reset_index())
diam5


diam.groupby('cut').agg(av_price = ('price', np.mean))