# -*- coding: utf-8 -*-
"""linear fit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yAsWp4tkS5lTL4hs7Y727_xp10gdDgPW
"""

import numpy as np
import matplotlib.pyplot as pl

def matrix_inverse(matrix):
  def transposeMatrix(matrix):
    return map(list,zip(*matrix))
  def getMatrixMinor(matrix,i,j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

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
  for r in range(len(cofactors)):
    for c in range(len(cofactors)):
      cofactors[r][c] = cofactors[r][c]/det
  return cofactors

x = np.array([3, 6, 8, 9, 10, 11, 12])
y = np.array([5.7, 12.0, 16.5, 18.2, 20.1, 21.8, 24.8])

n = 1 # order of the polynomial to be fitted

A = []
for j in range(n+1):
  temp = []
  for i in range(n+1):
    temp.append(sum(x**(j+i)))
  A.append(temp)

A = np.reshape(A,(n+1,n+1))
invA = np.reshape(matrix_inverse(A),(n+1,n+1))

C = []
for i in range(n+1):
  C.append(sum(y*x**i))
C = np.array(C)

fit = np.dot(invA,C)

pl.plot(x,y,'ro',zorder=1,label='given datapoints')
pl.plot(x,fit[0]+fit[1]*x,'b--',zorder=2,label='best fitted straight line')
pl.legend(loc='best')
pl.xlabel('$x$')
pl.ylabel('$y$')
if(fit[0]>0.0): pl.title('$y = $'+str(round(fit[1],3))+'$x + $'+str(round(fit[0],3)))
elif(fit[0]<0.0): pl.title('$y = $'+str(round(fit[1],3))+'$x - $'+str(round(abs(fit[0]),3)))
else: pl.title('$y = $'+str(round(fit[1],3))+'$x$')
pl.grid('on',alpha=0.2)
pl.show()