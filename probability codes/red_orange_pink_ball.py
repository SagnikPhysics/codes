# -*- coding: utf-8 -*-
"""red orange pink ball.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tIcSANRHvX9lPyi7UyBsl2aJ4BAz5N_w
"""

# Q1(a)

red = 12
orange = 8
pink = 15
total = red + orange + pink

inf = 5000000
cnt = 0
from random import randint
for i in range(inf):
  n1 = randint(1,total)
  n2 = randint(1,total)
  if((13<=n1<=20 and 21<=n2<=35) or (13<=n2<=20 and 21<=n1<=35)):
    cnt = cnt+1

print("Probability that one ball is orange and one ball is pink will be,",round(float(cnt)/float(inf),3))