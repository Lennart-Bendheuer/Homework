import numpy as np
import matplotlib . pyplot as plt

#Vorgabe:

Omega = 1
v0 = 1
x0 = 0

h_a = 0.05
h_b = 0.025
h_c = 0.001



L_a = 20*np.pi / h_a + 1
L_b = 20*np.pi / h_b + 1
L_c = 20*np.pi / h_c + 1

Intervall_a = np.linspace(0, 20.*np.pi, round(L_a))
Intervall_b = np.linspace(0, 20.*np.pi, round(L_b))
Intervall_c = np.linspace(0, 20.*np.pi, round(L_c))




Y_a_euler = np.linspace(0, 20.*np.pi, round(L_a)) 
Y_a_euler[0] = v0                      

x_a_euler = np . linspace (0, 20.*np.pi, round(L_a))
x_a_euler[0] = x0


Y_b_euler = np.linspace(0, 20.*np.pi, round(L_b)) 
Y_b_euler[0] = v0

x_b_euler = np . linspace (0, 20.*np.pi, round(L_b))
x_b_euler[0] = x0


Y_c_euler = np.linspace(0, 20.*np.pi, round(L_c))  
Y_c_euler[0] = v0                       

x_c_euler = np . linspace (0, 20.*np.pi, round(L_c))
x_c_euler[0] = x0




#h=0.05
I=1                                        
while I< round(L_a):
    YErgebnis = Y_a_euler[round(I-1)] + h_a* -Omega**2 * x_a_euler[round(I-1)]
    Y_a_euler[round(I)] = YErgebnis
    
    XErgebnis = x_a_euler[round(I-1)] + h_a* Y_a_euler[round(I-1)]
    x_a_euler[round(I)] = XErgebnis

    I = I + 1




plt . plot (Intervall_a , x_a_euler)
plt . xlabel ('$t$') # axis - label
plt . ylabel ('$x_a(t)$') # for both axis
plt . show ()



#h=0.025
I=1                                        
while I< round(L_b):
    YErgebnis = Y_b_euler[round(I-1)] + h_b* -Omega**2 * x_b_euler[round(I-1)]
    Y_b_euler[round(I)] = YErgebnis
    
    XErgebnis = x_b_euler[round(I-1)] + h_b* Y_b_euler[round(I-1)]
    x_b_euler[round(I)] = XErgebnis

    I = I + 1



plt . plot (Intervall_b , x_b_euler)
plt . xlabel ('$t$') # axis - label
plt . ylabel ('$x_b(t)$') # for both axis
plt . show ()



#h=0.001
I=1                                       
while I< round(L_c):
    YErgebnis = Y_c_euler[round(I-1)] + h_c* -Omega**2 * x_c_euler[round(I-1)]
    Y_c_euler[round(I)] = YErgebnis
    
    XErgebnis = x_c_euler[round(I-1)] + h_c* Y_c_euler[round(I-1)]
    x_c_euler[round(I)] = XErgebnis

    I = I + 1



plt . plot (Intervall_c , x_c_euler)
plt . xlabel ('$t$') # axis - label
plt . ylabel ('$x_c(t)$') # for both axis
plt . show ()
