import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x + b

nullmessung = 829 / 900

werte = csv_read("csv/eisen.csv")
xdata = np.zeros(11)
ydata = np.zeros(11)

y_err = np.zeros(11)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata[i] = np.log((float(values[2]) ) / float(values[1]) - nullmessung)
        y_err[i] = np.log(np.sqrt(float(values[2]) / float(values[1]) - nullmessung))

        i+=1


x_line = np.linspace(0, 5)
plt.errorbar(xdata, ydata, fmt="r.", label="Messwerte", yerr=y_err)
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

#µ = (0.431 \pm 0.005)
#N_0 = (5.02  \pm 0.01)
print(popt)
print(np.sqrt(pcov))

plt.xlabel(r"Materialdicke $D$ / cm")
plt.ylabel(r"$\ln \bigg (\frac{ N \cdot 1 \symup{s}}{t} - \Delta N \cdot 1 \symup{s} \bigg)$")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_eisen.pdf")