###########################################################
Overview
###########################################################
These files are the python codes used to simulate the dynamics of the mathematical model in the study Predation-driven geographical isolation of broods in periodical cicadas
by Diane Carmeliza N. Cuaresma, Maica Krizna A. Gavina, Jomar F. Rabajante, Jerrold M. Tubay,
Takuya Okabe, Satoru Morita, Kazuya Kobayashi, Nobuaki Mizumoto,
Hiromu Ito, Jin Yoshimura, Satoshi Kakishima and John R. Cooley.

Our model show that predation acts an important factor for maintaining the nonoverlapping distributions.
The proposed mechanism is most effective in the vicinity of the critical strength of predation beyond which the population is doomed to extinction.
Increase in predation intensity increases resistance to settlement of a minority brood, while suppressing the main brood population.

###########################################################
Information for 'fig2.py'
###########################################################
The code was written for Python 3.8 using the Spyder editor.
The numpy, math and matplotlib libraries were used.
fig2 simulates the dynamics of a single brood and was used to generate Figure 2 in the main text.

The code describes the life cycle of a periodical cicadas under predation pressures.
The codes were specifically written for a 17-year periodical cicada.
The variable that describes this in the code is lc, lc=17.
Every 17 years, t%17=0, adult cicadas emerge and reproduce.
A year after emergence, t%17=1, during the first instar period, predation occurs, p=1.
The nymphs that were able to escape predation, due to predation satiation, burrow in the ground where no other threat exist and, hence, they were able to maintain their population.
This cycle repeats.
In the code, the total number of life cycles simulated is t\_max=41. Hence, the total simulation time is t\_end=lc\*t\_max=697.
The user change the values of lc and p to investigate 13-year cicadas and predation in other ages, respectively.

Other parameters in the code are:
F=3 	-- 	growth factor of the host
K=400 	--	carrying capacity

c=200	--	predation intensity, choose between these two values
c=350

N0=100	--	initial population of cicadas, choose between these two values
N0=50

###########################################################
Information for 'fig3.py'
###########################################################
The code was written for Python 3.8 using the Spyder editor.
The numpy, math and matplotlib libraries were used.
fig3 simulates the dynamics of two broods, one of which is the main brood and the other the straggler brood. This code was used to generatte Figure 3 in the main text.

The code describes the life cycle of a periodical cicada main brood and accelerated stragglers under predation pressures.
The codes were specifically written for a 17-year periodical cicada.
The variable that describes this in the code is lc, lc=17.
Main brood emerge and reproduce every 17 years, t%17=0. Main brood face predation a year after emergence, t%17=p, where p=1.
Nymphs that were able to escape predation maintain their population until next emergence.
This cycle repeats.
The user change the values of lc and p to investigate 13-year cicadas and predation in other ages, respectively.

At time T=lc\*t\_i=527, where t\_i=31 is the number of life cycle needed for the main brood to reach equilibrium, the stragglers are introduced.
In the code, the stragglers were introduced y=13 years after the main brood emergence.
There are jj=60 stragglers cicadas introduced, leaving the main brood with N0=N[T+y]-jj cicadas left.
Starting at T+y+1, the code simulates the life cycle of two broods simultaneously.
Stragglers emerge and reproduce every t%17=y%17.
Stragglers face predation every t%17=(y+1)%17.
Stragglers that escape predation maintain their population until next emergence.
This cycle repeats.
The total simulation time is t\_end=1037.

Other parameters in the code are:
F=3 	-- 	growth factor of the host
K=400 	--	carrying capacity
cL=350	--	predation intensity
NL=100	--	initial population of cicadas