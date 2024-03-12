import pandas as pd
import numpy as np
#Creating Series from Array

arr1= np.array(['r','a','h','u','l']) #to create a 1d array 
arr1_series= pd.Series(arr1)           # array1 to series
print(arr1_series)
print("______________________")

list1= ["Rahul","Rakesh"] #create a list
list_df= pd.DataFrame(list1) # list to dtaframe or 2D array
print( list_df,"\n_____________________________________") 



