from pandas import Series

s3 = Series([1.2,2.5,-2.2,3.1,-0.8,-3.2],
            index = ['Jan 1','Jan 2','Jan 3','Jan 4','Jan 5','Jan 6',])
print(s3)

#Accessing elements of a Series

print('\ns3[2] = ',s3[2])       #display third element of the Series
print('s3[\'Jan 3\'] = ',s3['Jan 3'])   #indexing element of a Series

print('\ns3[1:3] = ')      #display a slice of the Series
print(s3[1:3])
print('s3.iloc([1:3]) = ')  #display a slice of the Series
print(s3.iloc[1:3])
