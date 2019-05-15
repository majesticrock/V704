import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

def sigma(epsilon):
    fac = 2 * np.pi * (2.82 * 10**(-15))**2
    term1 = (1 + epsilon)/(epsilon**2) * ( (2*(1 + epsilon))/(1+2*epsilon) - (1/epsilon)*np.log(1+2*epsilon) )
    term2 = (1/(2*epsilon)) * np.log(1 + 2*epsilon)
    term3 = -( (1 + 3 * epsilon) / (1 + 2*epsilon)**2 )

    return (fac * (term1 + term2 + term3))

zBlei = 82
zEisen = 26

avocado = 6.0221409 * 10**23

dichteBlei = 11340
dichteEisen = 7900

molMasseBlei = 207.2 * 10**(-3)
molMasseEisen = 55.845 * 10**(-3)

epsi = 1.295

print(sigma(epsi))

nBlei = (zBlei * avocado * dichteBlei) / molMasseBlei
muBlei = nBlei * sigma(epsi) * 10**(-2) #Umwandlung in cm⁻¹

nEisen = (zEisen * avocado * dichteEisen) / molMasseEisen
muEisen = nEisen * sigma(epsi) * 10**(-2) #Umwandlung in cm⁻¹


print("--------  Theoriewerte  --------")
print(muBlei)
print(muEisen)

expBlei = 1.04
expEisen = 0.431

abweichungBlei = (muBlei - expBlei) / muBlei
abweichungEisen = (muEisen - expEisen) / muEisen

print("--------  Abweichungen  --------")
print(abweichungBlei)
print(abweichungEisen)