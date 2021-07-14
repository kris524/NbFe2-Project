import math,cmath
import numpy as np

n=10
y=0.1705
pos  =  np.array([[0,0,0],[0,0,1/2],[y, 2*y, 1/4],[-2*y, -y, 1/4],[y,-y,1/4],[-y,-2*y,3/4],[-y,y,3/4],[2*y,y,3/4]])
moment = []
sfexp = []
values = []
q_sdw = 0.1 #Periodicity of magnetic order
#Q =[1, 0, 1.1] #Magnetic Bragg peaks, one magnetic bragg peaks sits at 1.1
#[1,2,0],[2,2,1],[1,0,1],[0,1,2] ])

#Equivalent to sfexp=numpy.dot(pos[p]+[0,0,i],q_2)
#First is the sum of each coordinate with the unit cell
Q = [0, 1,2 ]
Bragg_intensity = []
Bragg_position = []



[values.append(pos[p]+ [0,0,i]) for i in range(n) for p in range(len(pos))] #80 terms



for h in range(len(Q)):
    
    for k in range(len(Q)):
        for l in range(len(Q)):


            [sfexp.append( np.sum(np.dot(values[p], [Q[h],Q[k],Q[l]])))  for p in range(len(values))  ] #80 terms
            #print(len(sfexp))
            #we create a new list with same size as sfexp that calculates the moment
            [moment.append( 1*math.cos(2 * math.pi * (pos[p][2] + i)* q_sdw )) for i in range(n) for p in range(len(pos))] #80 terms

            #A single for loop that takes each number from the moment list and the sfexp list one by one,
            # hence reaching the same result as before.
            sf_sdw = 0
            for number in range(len(sfexp)): 
    
                sf_sdw += moment[number] * cmath.exp(complex(0, -2 * cmath.pi * sfexp[number]))

            sfexp = []

            Bragg_intensity.append(abs(sf_sdw / n)**2)
            Bragg_position.append(np.sqrt(Q[h]**2 + Q[k]**2 + Q[l]**2))



print(Bragg_intensity)
#print(Bragg_position)

import matplotlib.pyplot as plt

plt.plot(Bragg_position, Bragg_intensity)
plt.show()
