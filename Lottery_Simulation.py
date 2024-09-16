# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:55:35 2024

@author: sreekar
"""

import random
import matplotlib.pyplot as plt
account=0
x=[]
y=[]
for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    bet_value=random.randint(1,10)
    if (bet==bet_value):
        account=account+900-100
    else:
        account=account-100
    y.append(account)
print("Final amount is:",account)
plt.plot(x,y)
plt.show()

#OUTPUT
#Final amount is: -1400
