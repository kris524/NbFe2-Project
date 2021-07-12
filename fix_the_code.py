import math,cmath
import numpy as np

n=10
y=0.1705
pos  =  np.array([[0,0,0],[0,0,1/2],[y, 2*y, 1/4],[-2*y, -y, 1/4],[y,-y,1/4],[-y,-2*y,3/4],[-y,y,3/4],[2*y,y,3/4]])
moment = []
sfexp = []
values = []
q_sdw = 0.1
Q = [1,0, 1.1]

#Equivalent to sfexp=numpy.dot(pos[p]+[0,0,i],q_2)
#First is the sum of each coordinate with the unit cell
[values.append(pos[p]+ [0,0,i]) for i in range(n) for p in range(len(pos))]

#next is the dot product with the Miller index iterating over the values on the previous line
[sfexp.append( np.sum(np.dot(values[k], Q)))  for k in range(len(values))]

#we create a new list with same size as sfexp that calculates the moment
[moment.append( 1*math.cos(2 * math.pi * (pos[p][2] + i)* q_sdw )) for i in range(n) for p in range(len(pos))]

#A single for loop that takes each number from the moment list and the sfexp list one by one, hence reaching the same result as before.
sf_sdw = 0
for number in range(len(sfexp)): 
    sf_sdw += moment[number] * cmath.exp(complex(0, -2 * cmath.pi * sfexp[number]))

print(abs(sf_sdw / n)**2)