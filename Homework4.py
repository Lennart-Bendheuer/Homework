import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mat


K=50
N=50
h=0.001
Nt=1500

thetas = np.random.normal(0, 2.*np.pi, size=N)
Omegas = np.random.random_sample(size=N)

def order_parameters(theta):
    real = np.mean(np.cos(theta))
    imag = np.mean(np.sin(theta))
    r = np.sqrt(real**2 + imag**2)
    psi = np.angle(real + 1j*imag)
    return r, psi

def rk4_step(omega, theta, K, h):
    k1 = rhs(omega, theta, K)
    k2 = rhs(omega, theta + k1 * (h / 2 ), K)
    k3 = rhs(omega, theta + k2 * (h / 2 ), K)
    k4 = rhs(omega, theta + k3 * h, K)
    theta = theta + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    return theta

def rhs(omega, theta, K):
    N = len(theta)
    Ergebnis_Thetas = []
    r, psi = order_parameters(thetas)
    for i in range(N):
        Ergebnis_Thetas.append(omega[i] + K * np.sin(psi - theta[i]))
    return np.array(Ergebnis_Thetas)



plt.figure("phases")
for i in range(Nt):
    r, psi = order_parameters(thetas)
    rx = r * np.cos(psi)
    ry = r * np.sin(psi)
    xp = np.cos(thetas)
    yp = np.sin(thetas)

    circle = np.linspace(0, 2 * np.pi, 100)
    plt.plot(np.sin(circle), np.cos(circle))

    plt.title(str(round(h * i, 3)) + " s")  #Wie verhindere ich es hier, dass sich die Anzahl der Nachkommastellen verändert?

    plt.plot(xp, yp, "o")

    plt.arrow(0, 0, rx, ry, head_width=0.05)

    plt.draw()
    plt.show(block=False)


   # fileName = "video-phases_" + str(i) + ".png"
   # plt.savefig(fileName)

#diese f Strings funktionieren bei mir nicht, daher nutze ich ImageJ

    plt.pause(0.01)

    plt.clf()

    thetas = rk4_step(Omegas, thetas, K, h)




