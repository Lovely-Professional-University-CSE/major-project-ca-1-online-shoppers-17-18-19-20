# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:05:41 2019

@author: Hp
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
size = [10551, 1694, 85]
colors = ['green', 'yellow', 'red']
labels = "Returning Visitor", "New_Visitor", "Others"
explode = [0, 0, 0.1]

plt.pie(size, colors = colors, labels = labels, explode = explode, shadow = True, autopct = '%.2f%%')
plt.title('Different Types of customers visiting', fontsize = 30)
plt.axis('off')
plt.legend()
plt.show()


# plotting a pie chart for browsers
size = [179961, 124621, 17361, 14671,31741, 41613, 51300]
colors = ['lightgreen', 'red', 'pink', 'crimson', 'lime', 'cyan', 'pink']
labels = "2", "1","4","5","6","10","others"

plt.subplot(1, 1, 1)
plt.pie(size, colors = colors, labels = labels, shadow = True, autopct = '%.2f%%', startangle = 90)
plt.title('Different Browsers', fontsize = 30)
plt.axis('off')
plt.legend()
plt.show()

 
