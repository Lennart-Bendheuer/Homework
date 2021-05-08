<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt


def euler(rhs, x_old, function_parameters, stepsize):
    x_new = x_old + stepsize * rhs(*function_parameters)
    return x_new


def heun(rhs, x_old, function_parameters_old, function_parameters_new, stepsize):
    x_new = x_old + 0.5 * stepsize * (rhs(*function_parameters_old) + rhs(*function_parameters_new))
    return x_new


def decayP1(E1, Y1, P1old, P2old):
    return P1old * E1 - Y1 * P1old * P2old


def decayP2(E2, Y2, P1old, P2old):
    return -P2old * E2 + Y2 * P2old * P1old


# Vorgabe:
E1 = 2.0
E2 = 0.8
Y1 = 0.02
Y2 = 0.002
h = 0.025
R = 100
B = 100
P1old = B
P2old = R

# Heun
X = np.arange(0, 50, h)

P_h1 = np.arange(0, 50, h)
P_h1[0] = B

P_h2 = np.arange(0, 50, h)
P_h2[0] = R

I = 1

while (I < X.size):
    P1_e_guess = euler(decayP1, P1old, [E1, Y1, P1old, P2old], h)
    P2_e_guess = euler(decayP2, P2old, [E2, Y2, P1old, P2old], h)

    P_h1[I] = heun(decayP1, P1old, [E1, Y1, P1old, P2old], [E1, Y1, P1_e_guess, P2_e_guess], h)
    P_h2[I] = heun(decayP2, P2old, [E2, Y2, P1old, P2old], [E2, Y2, P1_e_guess, P2_e_guess], h)
    P1old = P_h1[I]
    P2old = P_h2[I]
    I = I + 1

# Euler
h_e = 0.025
X_e = np.arange(0, 50, h_e)
P1 = np.arange(0, 50, h_e)
P1[0] = B

P2 = np.arange(0, 50, h_e)
P2[0] = R
P1old = B
P2old = R
I = 1

while (I < X_e.size):
    P1[I] = euler(decayP1, P1old, [E1, Y1, P1old, P2old], h_e)
    P2[I] = euler(decayP2, P2old, [E2, Y2, P1old, P2old], h_e)
    P2old = P2[I]
    P1old = P1[I]

    I = I + 1

# Diagramme

# Nur Euler
# Zeitreihe
plt.plot(X_e, P1, color="blue", label="Beute-Population")
plt.plot(X_e, P2, color="red", label="Räuber-Population")
plt.title("Euler-Verfahren")
plt.xlabel('$t$')  # axis - label
plt.ylabel('$Population$')  # for both axis
plt.legend()
plt.show()
# Phasenraumtrajektorie
plt.plot(P1, P2)
plt.title("Euler-Verfahren")
plt.xlabel('$Beute-Population$')  # axis - label
plt.ylabel('$Räuber-Population$')  # for both axis
plt.show()

# Nur Heun
# Zeitreihe
plt.plot(X, P_h1, color="blue", label="Beute-Population")
plt.plot(X, P_h2, color="red", label="Räuber-Population")
plt.title("Heun-Verfahren")
plt.xlabel('$t$')  # axis - label
plt.ylabel('$Population$')  # for both axis
plt.legend()
plt.show()
# Phasenraumtrajektorie
plt.plot(P_h1, P_h2)
plt.title("Heun-Verfahren")
plt.xlabel('$Beute-Population$')  # axis - label
plt.ylabel('$Räuber-Population$')  # for both axis
plt.show()

# Vergleich euler heun
plt.plot(P_h1, P_h2, color="green", label="Heun-Verfahren")
plt.plot(P1, P2, color="blue", label="Euler_Verfahren")
plt.title("Vergleich der Euler- und Heun-Verfahren")
plt.xlabel('$Beute-Population$')
plt.ylabel('$Räuber-Population$')
plt.legend()
plt.show()







=======
import numpy as np
import matplotlib.pyplot as plt


def euler(rhs, x_old, function_parameters, stepsize):
    x_new = x_old + stepsize * rhs(*function_parameters)
    return x_new


def heun(rhs, x_old, function_parameters_old, function_parameters_new, stepsize):
    x_new = x_old + 0.5 * stepsize * (rhs(*function_parameters_old) + rhs(*function_parameters_new))
    return x_new


def decayP1(E1, Y1, P1old, P2old):
    return P1old * E1 - Y1 * P1old * P2old


def decayP2(E2, Y2, P1old, P2old):
    return -P2old * E2 + Y2 * P2old * P1old


# Vorgabe:
E1 = 2.0
E2 = 0.8
Y1 = 0.02
Y2 = 0.002
h = 0.025
R = 100
B = 100
P1old = B
P2old = R

# Heun
X = np.arange(0, 50, h)

P_h1 = np.arange(0, 50, h)
P_h1[0] = B

P_h2 = np.arange(0, 50, h)
P_h2[0] = R

I = 1

while (I < X.size):
    P1_e_guess = euler(decayP1, P1old, [E1, Y1, P1old, P2old], h)
    P2_e_guess = euler(decayP2, P2old, [E2, Y2, P1old, P2old], h)

    P_h1[I] = heun(decayP1, P1old, [E1, Y1, P1old, P2old], [E1, Y1, P1_e_guess, P2_e_guess], h)
    P_h2[I] = heun(decayP2, P2old, [E2, Y2, P1old, P2old], [E2, Y2, P1_e_guess, P2_e_guess], h)
    P1old = P_h1[I]
    P2old = P_h2[I]
    I = I + 1

# Euler
h_e = 0.025
X_e = np.arange(0, 50, h_e)
P1 = np.arange(0, 50, h_e)
P1[0] = B

P2 = np.arange(0, 50, h_e)
P2[0] = R
P1old = B
P2old = R
I = 1

while (I < X_e.size):
    P1[I] = euler(decayP1, P1old, [E1, Y1, P1old, P2old], h_e)
    P2[I] = euler(decayP2, P2old, [E2, Y2, P1old, P2old], h_e)
    P2old = P2[I]
    P1old = P1[I]

    I = I + 1

# Diagramme

# Nur Euler
# Zeitreihe
plt.plot(X_e, P1, color="blue", label="Beute-Population")
plt.plot(X_e, P2, color="red", label="Räuber-Population")
plt.title("Euler-Verfahren")
plt.xlabel('$t$')  # axis - label
plt.ylabel('$Population$')  # for both axis
plt.legend()
plt.show()
# Phasenraumtrajektorie
plt.plot(P1, P2)
plt.title("Euler-Verfahren")
plt.xlabel('$Beute-Population$')  # axis - label
plt.ylabel('$Räuber-Population$')  # for both axis
plt.show()

# Nur Heun
# Zeitreihe
plt.plot(X, P_h1, color="blue", label="Beute-Population")
plt.plot(X, P_h2, color="red", label="Räuber-Population")
plt.title("Heun-Verfahren")
plt.xlabel('$t$')  # axis - label
plt.ylabel('$Population$')  # for both axis
plt.legend()
plt.show()
# Phasenraumtrajektorie
plt.plot(P_h1, P_h2)
plt.title("Heun-Verfahren")
plt.xlabel('$Beute-Population$')  # axis - label
plt.ylabel('$Räuber-Population$')  # for both axis
plt.show()

# Vergleich euler heun
plt.plot(P_h1, P_h2, color="green", label="Heun-Verfahren")
plt.plot(P1, P2, color="blue", label="Euler_Verfahren")
plt.title("Vergleich der Euler- und Heun-Verfahren")
plt.xlabel('$Beute-Population$')
plt.ylabel('$Räuber-Population$')
plt.legend()
plt.show()







>>>>>>> af046017b6b2bdebf3e50811abf82e4a73740f5f
