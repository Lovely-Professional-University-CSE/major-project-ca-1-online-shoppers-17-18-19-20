from sklearn  import datasets

import pandas as pd

import numpy as np

dataset = pd.read_csv ('online_shoppers_intention.csv')

dataset.head()

dataset.columns

x = dataset.iloc[:,:].values

weights = np.random.uniform(size = (2,1))

weights

weights[1,0]

first_weights = weights[0,0]

second_weights = weights[1,0]

len(x)

l = x[0]

l[1]

leanring_rate = np.random.rand()

learning_rate = leanring_rate

for i in range(5):
    first = (l[i]-first_weights)
    first_square = first**2
    second = (l[i]-second_weights)
    second_square = second**2
    answer = min(first_square,second_square)
    print(answer)
    first_weights = first_weights+(learning_rate*(l[i]-first_weights))
    second_weights = second_weights + (learning_rate*(l[i]-second_weights))
    
    learning_rate = learning_rate*0.5

%matplotlib inline
import matplotlib.pyplot as plt

plt.show()