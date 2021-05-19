import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mat


K=50
N=50
h=0.001
Nt=1500

thetas = np.random.uniform(0, 2.*np.pi, size=N)
Omegas= np.random.standard_cauchy(size=N)

def order_parameters(theta):
    real = np.mean(np.cos(theta))
    imag = np.mean(np.sin(theta))
    r = np.sqrt(real**2 + imag**2)
    psi = np.angle(real + 1j*imag)
    return r, psi

def rk4_step(omega, theta, K, h):
    k1 = rhs(K, omega, theta)
    k2 = rhs(K, omega, theta + k1 * (h / 2 ))
    k3 = rhs(K, omega, theta + k2 * (h / 2 ))
    k4 = rhs(K, omega, theta + k3 * h)
    theta = theta + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    return theta

def rhs(K, omega, theta):
    N = len(theta)
    Ergebnis_Thetas = []
    r, psi = order_parameters(thetas)
    for i in range(N):
        Ergebnis_Thetas.append(omega[i] + K * r * np.sin(psi - theta[i]))
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

    #             dieser Part hier funktioniert bei mir nicht; wo ist mein Fehler?
    fileName = "video-phases_" + str(i) + ".png"
    plt.savefig(fileName)
    #             also der Part bis hier :( Es wird mir nur eine Fehlermeldung angezeigt: FileNotFoundError: [Errno 2] No such file or directory: 'video/phases_0.png'


    plt.pause(0.01)

    plt.clf()

    thetas = rk4_step(Omegas, thetas, K, h)




