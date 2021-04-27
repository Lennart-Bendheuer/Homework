import numpy as np
import matplotlib . pyplot as plt


x_analyt = np . linspace (0 , 7 , 100) #X Achse für analytische Lösung

#Vorgabe:
Alpha_a = 1
Alpha_b = 1
Alpha_c = 1
Alpha_d = 3

h_a = 0.5
h_b = 0.1
h_c = 0.01
h_d = 0.5

x0_a = 0.5
x0_b = 0.5
x0_c = 0.5
x0_d = 3

#L für X-und Y-Achse und die X Achse für Euler's Method
L_a = 7/h_a + 1
L_b = 7/h_b + 1
L_c = 7/h_c + 1
L_d = 7/h_d + 1

x_a_euler = np . linspace (0, 7, round(L_a))
x_b_euler = np . linspace (0, 7, round(L_b))
x_c_euler = np . linspace (0, 7, round(L_c))
x_d_euler = np . linspace (0, 7, round(L_d))


#3a
     #analytisch
y_a = x0_a* np.exp(-Alpha_a*x_analyt)  #Y_achse

plt . plot (x_analyt , y_a)
plt . xlabel ('$t$') # axis - label
plt . ylabel ('$x_a(t)$') # for both axis



     #euler
Y_a_euler = np.linspace(0, 7, round(L_a)) #Reihe für Y-achse, in der nachher die passenden Werte eingetragen werden
Y_a_euler[0] = x0_a                       #1. Wert der Y-achse

I=1                                       #restliche Werte für Y-Achse   
while I< round(L_a):
    YErgebnis = Y_a_euler[round(I-1)] + h_a* -Alpha_a * Y_a_euler[round(I-1)]
    Y_a_euler[round(I)] = YErgebnis
    I = I + 1


plt . plot (x_a_euler , Y_a_euler)
plt . xlabel ('$t$') # axis - label
plt . ylabel ('$x_a(t)$') # for both axis
plt . show ()





#3b
     #analytisch
y_b = x0_a* np.exp(-Alpha_b*x_analyt)  #Y_achse

plt . plot (x_analyt , y_b)
plt . xlabel ('$t$') # axis - label
plt . ylabel ('$x_b(t)$') # for both axis



     #euler
Y_b_euler = np.linspace(0, 7, round(L_b)) #Reihe für Y-achse, in der nachher die passenden Werte eingetragen werden
Y_b_euler[0] = x0_b                       #1. Wert der Y-achse

I=1
while I< round(L_b):
    YErgebnis = Y_b_euler[round(I-1)] + h_b* -Alpha_b * Y_b_euler[round(I-1)]
    Y_b_euler[round(I)] = YErgebnis
    I = I + 1


plt . plot (x_b_euler , Y_b_euler)
plt . xlabel ('$t$') # axis - label
plt . ylabel ('$x_b(t)$') # for both axis
plt . show ()



#3c
     #analytisch
y_c = x0_c* np.exp(-Alpha_c*x_analyt)  #Y_achse

plt . plot (x_analyt , y_c)
plt . xlabel ('$t$') # axis - label
plt . ylabel ('$x_b(t)$') # for both axis



     #euler
Y_c_euler = np.linspace(0, 7, round(L_c)) #Reihe für Y-achse, in der nachher die passenden Werte eingetragen werden
Y_c_euler[0] = x0_c                       #1. Wert der Y-achse

I=1
while I< round(L_c):
    YErgebnis = Y_c_euler[round(I-1)] + h_c* -Alpha_c * Y_c_euler[round(I-1)]
    Y_c_euler[round(I)] = YErgebnis
    I = I + 1


plt . plot (x_c_euler , Y_c_euler)
plt . xlabel ('$t$') # axis - label
plt . ylabel ('$x_c(t)$') # for both axis
plt . show ()




#3d
     #analytisch
y_d = x0_d* np.exp(-Alpha_d*x_analyt)  #Y_achse

plt . plot (x_analyt , y_d)
plt . xlabel ('$t$') # axis - label
plt . ylabel ('$x_d(t)$') # for both axis



     #euler
Y_d_euler = np.linspace(0, 7, round(L_d)) #Reihe für Y-achse, in der nachher die passenden Werte eingetragen werden
Y_d_euler[0] = x0_d                       #1. Wert der Y-achse

I=1
while I< round(L_d):
    YErgebnis = Y_d_euler[round(I-1)] + h_d* -Alpha_d * Y_d_euler[round(I-1)]
    Y_d_euler[round(I)] = YErgebnis
    I = I + 1


plt . plot (x_d_euler , Y_d_euler)
plt . xlabel ('$t$') # axis - label
plt . ylabel ('$x_d(t)$') # for both axis
plt . show ()




