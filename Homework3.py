import numpy as np
import matplotlib.pyplot as plt
#Vorgabe:
Phase1_Start=0.5
Phase2_Start=1
Phase3_Start=1.5
W1=0.19
W2=0.2
W3=1

Phasen=[Phase1_Start, Phase2_Start, Phase3_Start]


t_end = 15
h=0.001
time = np.arange(0, t_end, h)

Phase1 = np.arange(0, t_end, h)
Phase1[0]=Phase1_Start

Phase2 = np.arange(0, t_end, h)
Phase2[0]=Phase2_Start

Phase3 = np.arange(0, t_end, h)
Phase3[0]=Phase3_Start


#Adjacency Matrix K
K= [[0, 50, 10],
    [50, 0, 10],
    [10, 10, 0]]


for A in range(time.size-1):
    #k1 für Oszillator 1, 2 und 3
    k1=[W1, W2, W3]
    for i in range(3):
        for L in range(3):
       #     if (i!=L):
            k1[i]=k1[i]+K[i][L]*np.sin(Phasen[L]-Phasen[i])

    #k2 für Oszillator 1, 2 und 3
    k2=[W1, W2, W3]
    for i in range(3):
        for L in range(3):
       #     if (i!=L):
            k2[i]=k2[i]+K[i][L]*np.sin((Phasen[L]+(h/2)*k1[L])-(Phasen[i]+(h/2)*k1[i]))

    #k3 für Oszillator 1, 2 und 3
    k3=[W1, W2, W3]
    for i in range(3):
        for L in range(3):
      #      if (i!=L):
            k3[i]=k3[i]+K[i][L]*np.sin((Phasen[L]+(h/2)*k2[L])-(Phasen[i]+(h/2)*k2[i]))

    #k4 für Oszillator 1, 2 und 3
    k4=[W1, W2, W3]
    for i in range(3):
        for L in range(3):
      #      if (i!=L):
            k4[i]=k4[i]+K[i][L]*np.sin((Phasen[L]+h*k3[L])-(Phasen[i]+h*k3[i]))

    for i in range(3):
        Phasen[i]=Phasen[i]+((h/6)*(k1[i]+2*k2[i]+2*k3[i]+k4[i]))
    Phase1[A+1]=Phasen[0]
    Phase2[A+1]=Phasen[1]
    Phase3[A+1]=Phasen[2]





plt.plot(time, Phase1, color="blue", label="Phase 1")
plt.plot(time, Phase2, color="red", label="Phase 2")
plt.plot(time, Phase3, color="orange", label="Phase 3")
plt.title("Ein kleines Netzwerk")
plt.xlabel('$t$')
plt.ylabel('$Phase$')
plt.legend()
plt.show()













