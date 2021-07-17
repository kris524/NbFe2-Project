

import math,cmath
import numpy as np
import matplotlib.pyplot as plt

n=10
y=0.1705
pos  =  np.array([[0,0,0],[0,0,1/2],[y, 2*y, 1/4],[-2*y, -y, 1/4],[y,-y,1/4],[-y,-2*y,3/4],[-y,y,3/4],[2*y,y,3/4]])


moment = []
sfexp = []
values = []
q_sdw = 0 #Periodicity of magnetic order
#Q =[1, 0, 1.1] #Magnetic Bragg peaks, one magnetic bragg peaks sits at 1.1
#[1,2,0],[2,2,1],[1,0,1],[0,1,2] ])

#Equivalent to sfexp=numpy.dot(pos[p]+[0,0,i],q_2)
#First is the sum of each coordinate with the unit cell
Q = [0, 1, 2] # Rename Miller_list
Bragg_intensity = []
Bragg_position = []



[values.append(pos[p]+ [0,0,i]) for i in range(n) for p in range(len(pos))] #80 terms


# Rename them index1 index2 index3
for h in range(len(Q)):
    
    for k in range(len(Q)):
        for l in range(len(Q)):

            #rename this
            [sfexp.append( (np.dot(values[p], [ Q[h], Q[k], Q[l]  ])))  for p in range(len(values))  ] #80 terms
            #print(len(sfexp))
            #print(np.dot(values[0], [ 1, 1, 1]))
            #we create a new list with same size as sfexp that calculates the moment
            [moment.append( 1*math.cos(2 * math.pi * (pos[p][2] + i)* q_sdw )) for i in range(n) for p in range(len(pos))] #80 terms

            #A single for loop that takes each number from the moment list and the sfexp list one by one,
            # hence reaching the same result as before.
            sf_sdw = 0
            for number in range(len(sfexp)): 
    
                sf_sdw += moment[number] * cmath.exp(complex(0, -2 * cmath.pi * sfexp[number]))

            sfexp = []

            Bragg_intensity.append( round(abs(sf_sdw / n)**2, 8))
            Bragg_position.append(np.sqrt(Q[h]**2 + Q[k]**2 + Q[l]**2)) #the position has repeated numbers in it., 
            #010 has same length as 100 and 001, etc. so the dictionary will (or anything) will casue problems, so error is here
            #length,absolute of Q


print(Bragg_intensity)

#Use these as a substitute for now. 
positions = list(range(0,27))
#print(positions)

#ORIGINAL POISTIONS
 
#print(Bragg_position)
#Bragg_position = Bragg_position.sort()
#res = dict(zip(Bragg_position, Bragg_intensity))
#print(res)


#GENERAL POSITIONS

plt.bar(positions, Bragg_intensity)
plt.show()

#HISTOGRAM

#plt.hist(Bragg_intensity, bins = 50)
#plt.show()

