import pandas as pd # таблички
import numpy as np # числа
import seaborn as sns # графики прет-а-порте
import matplotlib.pyplot as plt # графики сделай сам


diam = sns.load_dataset('diamonds')

# простые действия
diam.head()
diam.describe()
diam.info()
diam['cut']

diam.describe(include='object')

# отбирали столбцы .filter
# отбирали строки .query
# создавали столбец .assign

new = (diam.assign(ln_price = np.log(diam['price']))
    .query('x > 0.7')
    .filter(['x', 'ln_price'])
    .sort_values(by='x', ascending=False)
    .head(7)
    .rename(columns={'x': 'iks'})
)


# та же комбо-серия но по шагам:
new2 = diam.assign(ln_price = np.log(diam['price'])) 
new3 = new2.query('x > 0.7')
new4 = new3.filter(['x', 'ln_price'])

# как выстрелить себе в ногу?
diam.iloc[2:3, 3:5]


# регулярные выражения! regular expressions regex
diam.filter(regex='ty$')
diam.filter(regex='^c')
diam.filter(regex='^[a-t]a')
https://xkcd.com/208/

# что сделать с отдельной колонкой?
diam['x'].mean()
diam['x'].mode()
diam['cut'].mode()
diam['cut'].value_counts()
diam['cut'].unique()
diam['cut'].nunique()

# преобразования столбца
diam5 = (diam.assign(price_cat=pd.cut(diam['price'], bins=3, 
    labels=['cheap', 'medium', 'pricy']))
    .query('price_cat == "medium"')
    .head(7))
diam5
?pd.cut

# работа с текстовыми переменными
diam5['cut2'] = diam['cut'].str.replace('Good', 'Bad')
diam5['cut3'] = diam['cut'].str.contains('Good')
diam5.head(10)

# split apply combine strategy
diam6 = (diam.groupby('cut')
    .agg(av_price=('price', np.mean),
        min_price=('price', np.min),
        max_weight=('carat', np.max))
    .reset_index())
diam6
diam.head()


