import random
print('(random.random()',random.random())

import pandas
cons = pandas.read_csv('cons.csv')
print(cons)
print(cons.head(2))
print(cons.describe())