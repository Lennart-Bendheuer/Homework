import numpy as np
import matplotlib.pyplot as plt
#Vorgabe:
E1 = 2.0
E2 = 0.8
Y1 = 0.02
Y2 = 0.002
h = 0.025
R = 100
B = 100

#Heun
X = np.arange(0, 50, h)


P_h1 = np.arange(0, 50, h)
P_h1[0] = B

P_h2 = np.arange(0, 50, h)
P_h2[0] = R

I = 1

while (I<X.size):
    P_h1[round(I)] = P_h1[round(I - 1)] + h * ((P_h1[round(I - 1)]*E1) - Y1 * P_h1[round(I - 1)] * P_h2[round(I - 1)])

    P_h2[round(I)] = P_h2[round(I - 1)] + h * ((P_h2[round(I - 1)] * Y2 * P_h1[round(I - 1)]) - P_h2[round(I - 1)] * E2)

    P_h1[round(I)] = P_h1[round(I - 1)] + h * 0.5 * (((P_h1[round(I - 1)]*E1) - Y1 * P_h1[round(I - 1)] * P_h2[round(I - 1)]) + ((P_h1[round(I)]*E1) - Y1 * P_h1[round(I)] * P_h2[round(I)]))

    P_h2[round(I)] = P_h2[round(I - 1)] + h * 0.5 * (((P_h2[round(I - 1)] * Y2 * P_h1[round(I - 1)]) - P_h2[round(I - 1)] * E2) + ((P_h2[round(I)] * Y2 * P_h1[round(I)]) - P_h2[round(I)] * E2))


    I = I + 1

#Euler
h_e=0.025
X_e = np.arange(0, 50, h_e)
P1 = np.arange(0, 50, h_e)
P1[0] = B

P2 = np.arange(0, 50, h_e)
P2[0] = R

I = 1

while (I<X_e.size):
    P1[round(I)] = P1[round(I - 1)] + h_e * ((P1[round(I - 1)]*E1) - Y1 * P1[round(I - 1)] * P2[round(I - 1)])


    P2[round(I)] = P2[round(I - 1)] + h_e * ((P2[round(I - 1)] * Y2 * P1[round(I - 1)]) - P2[round(I - 1)] * E2)

    I = I + 1


#Diagramme

#Nur Euler
#Zeitreihe
plt.plot(X_e, P1, color="blue", label="Beute-Population")
plt.plot(X_e, P2, color="red", label="Räuber-Population")
plt.title("Euler-Verfahren")
plt.xlabel('$t$')  # axis - label
plt.ylabel('$Population$')  # for both axis
plt.legend()
plt.show()
#Phasenraumtrajektorie
plt.plot(P1, P2)
plt.title("Euler-Verfahren")
plt.xlabel('$Beute-Population$')  # axis - label
plt.ylabel('$Räuber-Population$')  # for both axis
plt.show()

#Nur Heun
#Zeitreihe
plt.plot(X, P_h1, color="blue", label="Beute-Population")
plt.plot(X, P_h2, color="red", label="Räuber-Population")
plt.title("Heun-Verfahren")
plt.xlabel('$t$')  # axis - label
plt.ylabel('$Population$')  # for both axis
plt.legend()
plt.show()
#Phasenraumtrajektorie
plt.plot(P_h1, P_h2)
plt.title("Heun-Verfahren")
plt.xlabel('$Beute-Population$')  # axis - label
plt.ylabel('$Räuber-Population$')  # for both axis
plt.show()

#Vergleich euler heun
plt.plot(P_h1, P_h2, color="green", label="Heun-Verfahren")
plt.plot(P1, P2, color="blue", label="Euler_Verfahren")
plt.title("Vergleich der Euler- und Heun-Verfahren")
plt.xlabel('$Beute-Population$')
plt.ylabel('$Räuber-Population$')
plt.legend()
plt.show()







