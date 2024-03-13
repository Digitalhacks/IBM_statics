import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s1= pd.Series(["Rahul","Srestha","Mithi","rushtha"])
print(s1,"\n__________________")

print(s1.to_frame(name="Name"),"\n_________________")      #list to D.frame

s2= pd.Series([18,18,18,18])
print(pd.DataFrame({"NAME":s1, "AGE":s2}))

