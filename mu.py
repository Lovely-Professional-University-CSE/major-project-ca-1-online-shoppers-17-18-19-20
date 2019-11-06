# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 00:22:58 2019

@author: Dell
"""
import numpy as np
import pandas as pd
data=pd.read_csv('online_shoppers_intention.csv')
#print(data.head())
data.shape
#print(data[0:3])
#print(data.loc[1:3,['index']])
x=np.array(data.loc[1:3,['index']])
t=np.array(data.loc[1:3,['target']])
w=np.array(data.loc[1:3,['weights']])

#print(data['index'])
print(x)
print(w)
#w =np.array(data.loc[1:3,['weights']])
lrate= 0.6
e=1
D=[0,0]
print('learning rate of this epoch is',lrate);
while(e<=3):
    print('Epoch is',e);
    
    for i in range(2):
        for j in range(1):
             temp=0
             for k in range(1):
                temp = temp + ((w[k,j]-x[i,k])**2)
             D[j]=temp
        
        if(D[0]<D[1]):
            J=0
            
        else:
            J=1
            
        
        print('winning unit is',J+1)
        print('weight updation ...')
        if J==t[i]:
            for m in range(0):
            
                 w[m,J]=w[m,J] + (lrate *(x[i,m]-w[m,J]))
                 print(w[m,J])
        else:
            for m in range(0):
                w[m,J]=w[m,J] - (lrate *(x[i,m]-w[m,J]))
        
       
        print('Updated weights',w)
        

    e=e+1
    lrate = 0.5*lrate;
    print(' updated learning rate after ',e,' epoch is',lrate)

