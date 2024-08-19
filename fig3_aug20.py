#-----------------------------------------------------------------------------
# This python code is used to generate Figure 3.
# Figure 3 shows the different possible dynamics of the model when stragglers are introduced.
#-----------------------------------------------------------------------------
  
# Importing libraries
import math as m
import matplotlib.pyplot as plt

# Input parameters
K = 400           #cicada carrying capacity
F = 3             #growth factor for cicada
cL = 350          #predation intensity, 17-year
NL = 100          #main brood, initial population, 17-year
#cL = 200            #predation intensity, 13-year 
#NL = 50             #main brood, initial population, 13-year
y = 13            #age of main brood at straggler introduction

# Array for population of hosts
N = []            #main, population density
J = []            #straggler, population density

# Time count
lc = 17           #life cycle of host, can be 13 or 17
p = 1             #age at predation
t_i = 31          #cycles to equi
T = lc*t_i        #intro time
t_end = 17*61     #total sim time

jj=60            #straggler, initial population 
N.clear(); J.clear(); N.append(NL); J.append(0)

# During the first T years (t_i cycles), stragglers are inexistent, i.e., J[t]=0 for t<T.
for t in range(0,t_end+1) :
    if t < T+y :                                     #accelerated emergence
    #if t < T :                                       #delayed emergence  
        if t%lc==0 :
            if N[t] >= 1 : N.append(F*(1-N[t]/K)*N[t])
            else : N.append(0)
            J.append(0)
        elif t%lc==p :
            if (1-m.exp(-N[t]/cL))*N[t] >= 0 : N.append((1-m.exp(-N[t]/cL))*N[t])
            else : N.append(0)
            J.append(0)
        else :
            N.append(N[t])
            J.append(0)

# After T, stragglers are introduced. 
# Choose when straggler brood emerge.
# Accelerated emergence, for y>=9.  
    if t == T+y :                               
        N.append(N[t]-jj)                            #population of main brood is reduced by how many emerged eariler
        J.append(F*(1-jj/K)*jj)                      #jj adult cicadas emerged early, they reproduce

# Delayed emergence, for y<9.
#    if t == T :
#        n0 = N[t]-jj
#        if n0 >= 1 : N.append(F*(1-n0/K)*n0)
#        else : N.append(0)
#        J.append(0)
#    if t > T and t < T+y :
#        if t%lc==p :
#            if (1-m.exp(-N[t]/cL))*N[t] >= 0 : N.append((1-m.exp(-N[t]/cL))*N[t])
#            else : N.append(0)
#            J.append(0)
#        else :
#            N.append(N[t])
#            J.append(0)
#    if t == T+y :
#        if t%lc==p :
#            if (1-m.exp(-N[t]/cL))*N[t] >= 0 : N.append((1-m.exp(-N[t]/cL))*N[t])
#            else : N.append(0)
#            J.append(F*(1-jj/K)*jj)
#        else :
#            N.append(N[t])
#            J.append(F*(1-jj/K)*jj)
       
# Dynamics of two broods, main and straggler                    
    if t > T+y :
        if t%lc==0 : #reproduction main brood
            if t%lc==y%lc: #reproduction straggler brood
                if N[t] >= 1 : N.append(F*(1-N[t]/K)*N[t])
                else : N.append(0)
                if J[t] >= 1 : J.append(F*(1-J[t]/K)*J[t])
                else : J.append(0)
            elif t%lc==(y+p)%lc:  #predation straggler brood  
                if N[t] >= 1 : N.append(F*(1-N[t]/K)*N[t])
                else : N.append(0)
                if (1-m.exp(-J[t]/cL))*J[t] >= 0 : J.append((1-m.exp(-J[t]/cL))*J[t])
                else : J.append(0)
            else:
                if N[t] >= 1 : N.append(F*(1-N[t]/K)*N[t])
                else : N.append(0)
                J.append(J[t])
        elif t%lc==p : #predation main brood
            if t%lc==y%lc: #reproduction straggler brood
                if (1-m.exp(-N[t]/cL))*N[t] >= 0 : N.append((1-m.exp(-N[t]/cL))*N[t])
                else : N.append(0)
                if J[t] >= 1 : J.append(F*(1-J[t]/K)*J[t])
                else : J.append(0)
            elif t%lc==(y+p)%lc:  #predation straggler brood  
                if (1-m.exp(-N[t]/cL))*N[t] >= 0 : N.append((1-m.exp(-N[t]/cL))*N[t])
                else : N.append(0)
                if (1-m.exp(-J[t]/cL))*J[t] >= 0 : J.append((1-m.exp(-J[t]/cL))*J[t])
                else : J.append(0)
            else:
                if (1-m.exp(-N[t]/cL))*N[t] >= 0 : N.append((1-m.exp(-N[t]/cL))*N[t])
                else : N.append(0)
                J.append(J[t])
        elif t%lc==y%lc : #reproduction straggler brood
            N.append(N[t])
            if J[t] >= 1 : J.append(F*(1-J[t]/K)*J[t])
            else : J.append(0)
        elif t%lc==(y+p)%lc : #predation straggler brood
            N.append(N[t])
            if (1-m.exp(-J[t]/cL))*J[t] >= 0 : J.append((1-m.exp(-J[t]/cL))*J[t])
            else : J.append(0)
        else :
            N.append(N[t])
            J.append(J[t])

plt.plot(N, linestyle="-", color="blue", linewidth=2.0, label="Main brood")
plt.plot(J, linestyle="-", color="green", linewidth=2.0, label="Straggler brood")
plt.xlabel("Time, $t$ (in years)")#, fontsize=22)
plt.ylabel("Population, $N(t)$, $J(t)$")#, fontsize=22)
plt.ylim(0,350)
plt.xlim(T,t_end)
#plt.yticks(fontsize=18)

plt.show()

