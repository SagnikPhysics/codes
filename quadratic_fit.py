# -*- coding: utf-8 -*-
"""quadratic fit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VozTwf7XqPo4fOguioDU98t6JHcw4xum
"""

import numpy as np
import matplotlib.pyplot as pl
def matrix_inverse(matrix):
  def transposeMatrix(matrix):
    return map(list,zip(*matrix))
  def getMatrixMinor(matrix,i,j):
    c = matrix[:]
    c = np.delete(c,(i),axis=0)
    return [np.delete(row,(j),axis=0) for row in (c)]
  def deternminant(matrix):
    #base case for 2x2 matrix
    if len(matrix) == 2:
      return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    det = 0
    for c in range(len(matrix)):
      det += ((-1)**c)*matrix[0][c]*deternminant(getMatrixMinor(matrix,0,c))
    return det
  det = deternminant(matrix)
  # special case for 2x2 matrix:
  if len(matrix) == 2:
    return [[matrix[1][1]/det, -1*matrix[0][1]/det],
            [-1*matrix[1][0]/det, matrix[0][0]/det]]
  # find matrix of cofactors
  cofactors = []
  for r in range(len(matrix)):
    cofactorRow = []
    for c in range(len(matrix)):
      minor = getMatrixMinor(matrix,r,c)
      cofactorRow.append(((-1)**(r+c)) * deternminant(minor))
    cofactors.append(cofactorRow)
  cofactors = transposeMatrix(cofactors)
  cofactors = list(cofactors)
  for r in range(len(cofactors)):
    for c in range(len(cofactors)):
      cofactors[r][c] = cofactors[r][c]/det
  return cofactors
x = np.array([3, 6, 8, 9.5, 10, 11, 12])
y = np.array([-13.3, 12.2, 50.2, 88.7, 120.4, 160.0, 210.1])
n = 2 # order of the polynomial to be fitted
A = []
for j in range(n+1):
  temp = []
  for i in range(n+1):
    temp.append(sum(x**(j+i)))
  A.append(temp)
A = np.reshape(A,(n+1,n+1))
invA = matrix_inverse(A)
invA = np.reshape(invA,(n+1,n+1))
C = []
for i in range(n+1):
  C.append(sum(y*x**i))
C = np.array(C)
fit = np.dot(invA,C)
pl.plot(x,y,'ko',zorder=1,label='given datapoints')
x_plot = np.linspace(min(x),max(x),500)
pl.plot(x_plot,fit[0]+fit[1]*x_plot+fit[2]*x_plot**2,'r--',zorder=2,label='best fitted parabola')
pl.legend(loc='best')
pl.xlabel('$x$')
pl.ylabel('$y$')
pl.title('$y = $'+str(round(fit[2],3))+'$x^2 - $'+str(abs(round(fit[1],3)))+'$x - $'+str(abs(round(fit[0],3))))
pl.grid('on',alpha=0.2)
pl.show()