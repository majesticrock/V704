import matplotlib.pyplot as plt

import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
import sympy
from scipy import optimize

a0 = 495 / 900
A1 = np.array([0.69, 0.66, 0.64, 0.66, 0.75, 0.78, 1.76, 4.49, 6.94, 6.37, 27.92]) - a0 #zählrate / zeit
M = np.array([1.30, 1.20, 1.08, 0.91, 0.82, 0.68, 0.54, 0.43, 0.41, 0.34, 0.27]) * 10**(-1)#massenbelegung
A = np.log(A1)

#erste Gerade
A1g1 = np.array([0.78, 1.76, 4.49, 6.94, 6.37, 27.92]) - a0 #A1 zu erstw gerade
Mg1 = np.array([0.68, 0.54, 0.43, 0.41, 0.34, 0.27])  * 10**(-1)
Ag1 = np.log(A1g1)

def test_func(Mg1, a1, b1):
    return a1 * Mg1 + b1

params, params_covariance = curve_fit(test_func, Mg1, Ag1)
errors = np.sqrt(np.diag(params_covariance)) #Sigma Formel 
print(params)
print('a1:', params[0], '+-', errors[0])
print('b1:', params[1], '+-', errors[1])  

#zweite Gerade
A1g2 = np.array([0.69, 0.66, 0.64, 0.66, 0.75]) - a0
Mg2 = np.array([1.30, 1.20, 1.08, 0.91, 0.82]) * 10**(-1)
Ag2 = np.log(A1g2)

def test_func2(Mg2, a2, b2):
    return a2 * Mg2 + b2

params2, params2_covariance = curve_fit(test_func2, Mg2, Ag2)
errors2 = np.sqrt(np.diag(params2_covariance)) #Sigma Formel 
print(params)
print('a2:', params2[0], '+-', errors2[0])
print('b2:', params2[1], '+-', errors2[1])

#Fehlerbalken
xfehler = np.array([0.003, 0.005, 0.003, 0.014, 0.003, 0.003, 0.003, 0.003, 0.001, 0.000, 0.000]) * 10**(-1)

yfehler1 = np.sqrt(A1)
yfehler = np.log(yfehler1)
plt.errorbar(M, A, xerr=xfehler, yerr=yfehler, fmt='.', label="Messwerte")

xline1 = np.linspace(0.4, 1.3) * 10**(-1)
xline2 = np.linspace(0.27, 0.9) * 10**(-1)
#Graphen
#plt.plot(M, A, 'rx', label=r'Messwerte') #Wichtig mit 28
plt.plot(xline2, test_func(xline2, *params),'-', label=r'Fit 1')
plt.plot(xline1, test_func2(xline1, *params2),'-', label=r'Fit 2')
plt.xlabel(r'Massenbelegung $R$  /  $\frac{\symup{g}}{\symup{cm}^2}$')
plt.ylabel(r'$\ln ((A - A_0 ) \cdot 1 \symup{s})$')
plt.legend()
plt.tight_layout()
#plt.xlim(0, 0.005)
#plt.ylim(0,0.0002)

plt.savefig("build/plot_beta.pdf")