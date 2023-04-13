# Solve a dynamic programming problem about cookies

#%%
import numpy as np

beta = 0.9
p = 0.8
q = 0.05
runs = 100

V = np.zeros((runs,11))
G = np.zeros((runs,11))


#%%
for n in range(runs-1):
    for i in range(11):
        # calculate value from choosing each strategy
        W = np.zeros(11)
        for j in range (11):
            if j>i:
                W[j] = -1
            elif j==i: 
                W[j] = np.sqrt(j)+beta * (q*(1-p)*V[n,10] + q*p*V[n,9] +(1-q)*V[n,0])
            else:
                W[j] = np.sqrt(j)+beta * (q*(1-p)*V[n,10] + q*p*V[n,9] + (1-q)*(1-p)*V[n,i-j] + (1-q)*p*V[n,i-j-1])

        V[n+1,i] = W.max()
        G[n+1,i] = np.argmax(W)

#%%
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
 'value' : V[-1,:],
 'policy' : G[-1,:]})

df

#%%
df['policy'].plot(kind='bar')
df['value'].plot(secondary_y=True)
ax = plt.gca()

plt.show()

#%%

