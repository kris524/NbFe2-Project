import math,cmath
import numpy as np
import matplotlib.pyplot as plt
import crystals
from crystals import Crystal
#This is the primitive cell file generated from our cif file
diamond = Crystal.from_cif(r'C:\Users\krist\AppData\Local\Programs\Python\Python39\Lib\site-packages\crystals\cifs\diamond.cif') 
#=======================================================================================================================================
#THIS PART IS TAKING THE LOCATIONS OF THE DIAMOND

import numpy as np
atomic_position = []
for atm in diamond:
 
    
    #print(atm)
    txt = np.array(atm)
    #print(txt)
    #b = [int(s) for s in txt.split() if s.isdigit()]
    #atomic_position.append(repr(numpy.array(atm)))
    #print(b)
    for i in range(len(txt)):
        #print(txt[i])
        if txt[i] < 1:
            atomic_position.append(txt[i])

#print(atomic_position)
print('------------------------------------------------------')
#for x in atomic_position:
matrix = []
i=0
while i < (len(atomic_position)):
   
    matrix.append(atomic_position[i:i+3])
    i+=3


print(matrix)

print('------------------------------------------------------')


#=======================================================================================================================================

n=10 
y=0.1705
#NOW USE THE POSITIONS OF THE DIAMOND GENERATED FROM THE CIF FILE
matrix = np.array(matrix)

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



[values.append(matrix[p]+ [0,0,i]) for i in range(n) for p in range(len(matrix))] #80 terms


# Rename them index1 index2 index3
for h in range(len(Q)):
    
    for k in range(len(Q)):
        for l in range(len(Q)):

            #rename this
            [sfexp.append( (np.dot(values[p], [ Q[h], Q[k], Q[l]  ])))  for p in range(len(values))  ] #80 terms
            #print(len(sfexp))
            #print(np.dot(values[0], [ 1, 1, 1]))
            #we create a new list with same size as sfexp that calculates the moment
            [moment.append( 1*math.cos(2 * math.pi * (matrix[p][2] + i)* q_sdw )) for i in range(n) for p in range(len(matrix))] #80 terms
            
            #A single for loop that takes each number from the moment list and the sfexp list one by one,
            # hence reaching the same result as before.
            sf_sdw = 0
            for number in range(len(sfexp)): 
    
                sf_sdw += moment[number]* cmath.exp(complex(0, -2 * cmath.pi * sfexp[number]))

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
plt.xlabel('Miller index')
plt.ylabel('Bragg intensity')
plt.show()

#HISTOGRAM

#plt.hist(Bragg_intensity, bins = 50)
#plt.show()