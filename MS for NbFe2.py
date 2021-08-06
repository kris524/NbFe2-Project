import gemmi
#Work with two pakages, gemmi reads the magnetic coordsm while crystals reads the real coords
import math,cmath
import numpy as np
import matplotlib.pyplot as plt 
import crystals
from crystals import Crystal

from gemmi import cif
from numpy.lib.function_base import append
#Read the cif file and save it in a block, standard procedure when working with this package
doc = cif.read_file('NbFe2_mp-568901_primitive.cif') #NbFe2_ferromagnetic, NbFe2_ferrimagnetic
block = doc.sole_block()


#=======================================================================================================================================
#ACESS THE NAMES
print('----------------------------------------------------------------------------------------------')

import pandas as pd
#create an empty list that will store all the data in this form: ['Ni', m1, m2, m3, 'F', m1, m2 m3]
data = []
for row in block.find_mmcif_category('_atom_site_moment.'):
    row = list(row)
    #print(row)
    for value in row:
        try:
            data.append(float(value))
        except ValueError:
            data.append(value)
    


print(data)
#now data = ['Ni', -2.0, 0.03, 0.0, 'F', 0.0, 0.0, 0.0], however, we need to divide it into grops,
# Thats what the next line of code does, it splits them accordingly
#OBJECTIVE: ATTACHE THE NUMBERS TO THE DATA STRING SO WE GET ['Ni',-2.000,ETC.]

final_data = []
i = 0
while i < len(data):
    final_data.append(data[i:i+4])
    i+=4

print(final_data)  #[['Ni', -2.0, 0.03, 0.0], ['F', 0.0, 0.0, 0.0]]

#Here we just create a pandas dataframe, the code is standard and makes everything easy to acces later on
#name the corresponding columns and also, make element to be the index
df1 = pd.DataFrame(final_data, columns=['Element','m1','m2','m3'])
df1 = df1.set_index('Element')
print(df1)
# Part 1 done
#=======================================================================================================================================

print('----------------------------------------------------------------------------------------------')
#Here we now use the crystals package to import the real coords of the crystal
NiF2 = Crystal.from_cif(r'C:\Users\krist\Documents\PYTHON PROJECTS ON VS CODE\NbFe2_mp-568901_primitive.cif') 

#We convert all the data into an editable array, however, here we get the atomic numbers, not the element names so we will change that
NiF2_array = np.array(NiF2)

#make it into and array that will make access and edits easier
df2 = pd.DataFrame(NiF2_array,columns=['Element','x','y','z'])
df2 =df2.set_index('Element')
print(df2)

print('----------------------------------------------------------------------------------------------')
#Multiplication

#=======================================================================================================================================
#HERE I WILL TAKE THE CORRESPONDING ATOMIC NUMBERS WITH THEIR ELEMENTS:
#mainly work with crystals package here to take the coordinates with their atomic number and just change 9 -> 'F', 28 -> 'Ni', etc
#here we work with atomic data and df2

atomic_data = pd.read_csv(r'C:\Users\krist\Documents\PYTHON PROJECTS ON VS CODE\Physics Project\atomic data.csv')
atomic_data =atomic_data.set_index('Element')

#print(atomic_data)

#atomic_data.sort_index().sort_index(axis=1)
#df2.sort_index().sort_index(axis=1)
#Now we want to take df2 and compare its index to atomic data

#Create this empty list that will contain all the symbols and later we will set this as an index for df2
symbols_for_df2 = []
for index, row in atomic_data.iterrows():
    #print(index)
    for index2, rows in df2.iterrows():
        #print(j[0])
        if index == index2:
            
            #create a new column that contains the symbol
            symbols_for_df2.append(row['symbol'])
            
#Print to see all the coresponding symbols and finally atach them to the dataframe and make them an index, exacly as planned!      
print(symbols_for_df2)
df2['symbols'] = symbols_for_df2 
df2 = df2.set_index('symbols')

print(df2)

#=======================================================================================================================================
#Create an empty list where all the dot products will be stored there
dot_product_list = []

#iterate over the index and the rows, you have individual access to each of them
for index2, row2 in df2.iterrows():

    corrds_df2 = [row2['x'], row2['y'],row2['z']]

    for index, row1 in df1.iterrows():

        corrds_df1 = [row1['m1'], row1['m2'],row1['m3']]

        if index2 == index:
            dot_product = np.dot(corrds_df2, corrds_df1)
            dot_product_list.append(dot_product)

    
    #name a corrds variable that keeps each coordinate as a list
    

    
print('----------------------------------------------------------------------------------------------')

#print('The dot products are: ',dot_product_list)

#What I have doen below is focus on making the right labels of the index. 
#My idea to change 2a and 6h is to write specific code here that has access to the x,y and z.
#something like this

#Create an emty list where the new names will be stored
new_index = []
for ind, j in df2.iterrows():  #Itarate over indecies and coordinates called j, ind = index

    coordinates = [j['x'], j['y'], j['z']]

    print(coordinates)
    user_input = input()
    new_index.append(user_input)
    #Save the coords in a list 
   

#print(df2)
#print(new_index)
print('----------------------------------------------------------------------------------------------')

new_df2 = df2.copy() #Make a copy of the dataframe 

new_df2['new_index'] = new_index   #create a new column called new_index

#print(new_df2)

new_df2 = new_df2.set_index('new_index') #Now change its index to new_index

print(new_df2)  #I have created new dataframce with the corresponding names that I can use 
#All that need to be done is add Fe2a and Fe6h to the magnetic data and you can combine them