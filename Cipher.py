# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:11:26 2024

@author: sreekar
"""

import string
data=""
dict={}
file=open("op_file.txt",'w')
for i in range (len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open('open_file.txt') as f:
    while True:
        c=f.read(1)
        if not c:
            print("end of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print(data)
file.close()
#output came ,successfully
