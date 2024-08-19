#-----------------------------------------------------------------------------
# This python code is used to generate Figure 2.
# Figure 2 shows the different possible dynamics of the model.
#-----------------------------------------------------------------------------

# Importing libraries
import math as m
import matplotlib.pyplot as plt

# Input constants 
F = 3             #growth factor of host
K = 400           #cicada carrying capacity
c1 = 50          #predation intensity, panel (a,c)
c2 = 50          #predation intensity, panel (b,d)
N1 = 100          #initial population, panel (a,b)
N2 = 50           #initial population, panel (c,d)

N = []            #cicada population

# Time count
lc = 17           #life cycle of host (periodical cicadas have life cycle of 17, 13)
p = 1             #age when predation occurs
t_max = 41        #number of cycles
t_end = lc*t_max  #total simulation time

N.clear()
N.append(N1)
for t in range(0,t_end+1) :
    if t%lc==0 :                    #emergence
        #if N[t] >= 1  : N.append(F*(1-N[t]/K)*N[t]*(1-m.exp(-N[t]/c2)))             #if p=0
        if N[t] >= 1  : N.append(F*(1-N[t]/K)*N[t])
        else: N.append(0)
    elif t%lc==p :                  #predation, comment out if p=0
        if (1-m.exp(-N[t]/c1))*N[t] >= 0 : N.append((1-m.exp(-N[t]/c1))*N[t])
        else : N.append(0)
    else :
        N.append(N[t])
plt.subplot(2,2,1)
plt.plot(N, linestyle="-")
plt.xlabel("Time, $t$ (in years)")
plt.ylabel("Population, $N(t)$")
plt.ylim(0,350)
plt.xticks(range(lc,t_end+lc,lc*round(t_end/150)))

plt.show()