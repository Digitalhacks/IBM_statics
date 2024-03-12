import pandas as pd
import numpy as np
s= pd.Series(['cat', 'dog', np.nan, 'rabbit'])             #creaet a list
print(s,"\n___________________________")
s_mapped=s.map({'cat':'kitty', 'dog':'puppy'})           # mapping cat to kitty and dog to puppy
print(s_mapped,"\n_______________________")         
print(s.map('I Love {}'.format),"\n______________________") #mapping i is also work in sentences
print(s.map('I Love  {}'.format, na_action='ignore'),"\n_____________________") # na ignored

print(s,"\n___________________________")   #mapping mathod does not effect to the main value, only return ....