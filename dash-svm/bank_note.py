import pandas as pd

df = pd.read_csv('data_banknote_authentication.txt', header=None)

#X = df.loc[:,:3] #cant figure out how to use multiple input features
X = df.loc[:,0]
y = df.loc[:,4:]
