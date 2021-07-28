import gemmi

import math,cmath
import numpy as np
import matplotlib.pyplot as plt

import crystals
from crystals import Crystal
#print(gemmi.Element('Mg').weight)
from gemmi import cif

#Read the cif file and save it in a block
doc = cif.read_file('NiF2_mp-559798_primitive.cif')
print(doc)
block = doc.sole_block()


#=======================================================================================================================================
#ACESS THE NAMES
print('----------------------------------------------------------------------------------------------')

import pandas as pd

data = []
for row in block.find_mmcif_category('_atom_site_moment.'):
    row = list(row)
    print(row)
    for value in row:
        try:
            data.append(float(value))
        except ValueError:
            data.append(value)
    

print(data)
final_data = []
i = 0
while i < len(data):
    final_data.append(data[i:i+4])
    i+=4

print(final_data) 

data = np.array(data)
#OBJECTIVE: ATTACHE THE NUMBERS TO THE DATA STRING SO WE GET ['Ni',-2.000,ETC.]

#df1 = pd.DataFrame(data, columns=['Element','m1','m2','m3'])
#df1 = df1.set_index('Element')

#print(df1)

#=======================================================================================================================================

print('----------------------------------------------------------------------------------------------')

NiF2 = Crystal.from_cif(r'C:\Users\krist\Documents\PYTHON PROJECTS ON VS CODE\NiF2_mp-559798_primitive.cif') 

#print(NiF2)

NiF2_array = np.array(NiF2)

#print(NiF2_array)
df2 = pd.DataFrame(NiF2_array,columns=['Element','x','y','z'])
df2 =df2.set_index('Element')

#print(df2)

print('----------------------------------------------------------------------------------------------')
#Multiplication


#print(df1.index)
#print(data[0][1:])
#df2.multiply(np.array(data[0][1:]), axis='columns')
#Try and use gemmi to extract that data