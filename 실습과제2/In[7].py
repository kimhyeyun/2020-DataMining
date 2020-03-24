import numpy as np

my2dlist = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  # a 2-dim list
print(my2dlist)
print(my2dlist[2])  #access the third sublist
print(my2dlist[:][2])   #can't access third element of each sublist
#print(my2dlist[:,2])  #this will cause syntax error

my2darr = np.array(my2dlist)
print(my2darr)
print(my2darr[2][:])    #access the third row
print(my2darr[2,:])     #access the third row
print(my2darr[:][2])    #access the third row (similar to 2d list)
print(my2darr[:,2])     #access the third column
print(my2darr[:2,2:])   #access the first two rows & last two columns
