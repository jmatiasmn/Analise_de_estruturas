import matplotlib.pyplot as plt
import numpy as np
from math import pow
MF = []
length = []
V =[]

for l in np.arange(0, 37.27, 0.001):
    length.append(l)
    if 0 <= l < 4.03:
        MF.append(22.45*l - 7.85*pow(l,2))
        V.append(-15.70*l+22.4554)
    elif 4.03 <= l < 9.34:
        MF.append(- 7.85*pow(l,2)+106.4788*l-338.6143)
        V.append(-15.70*l+106.4788)
    elif 9.34 <= l < 13.40:
        MF.append(-7.85 * pow(l,2) + 178.8170 * l - 1014.2531)
        V.append(-15.70*l+178.8170)
    elif 13.40 <= l < 18.71:
        MF.append(-7.85 * pow(l,2) + 249.6421 * l - 1963.3094)
        V.append(-15.70*l+249.6421)
    elif 18.71 <= l < 24.01:
        MF.append(-7.85 * pow(l,2) + 336.6483 * l - 3591.1954)
        V.append(-15.70*l+336.6483)
    elif 24.01 <= l < 28.08:
        MF.append(-7.85 * pow(l,2) + 413.9265 * l - 5446.6450)
        V.append(-15.70*l+413.9265)
    elif 28.08 <= l < 31.77:
        MF.append(-7.85 * pow(l,2) + 460.8769 * l - 6765.0122)
        V.append(-15.70*l+460.8769)
    elif 31.77 <= l < 37.27:
        MF.append(-7.85 * pow(l,2) + 549.9719 * l - 9593.4244)
        V.append(-15.70*l+549.9719)

#Momento fletor
plt.subplot((121))
plt.plot(length,MF,label="Momento Fletor",color='silver')
plt.title("DMF - V01",fontsize=16)
plt.grid(linestyle='--',linewidth = 0.5)
plt.xticks([0,4.03,9.34,13.40,18.71,24.01,28.09,31.77,37.27])
plt.fill_between(length, MF,color="silver",alpha=0.5)
plt.gca().invert_yaxis()
plt.legend()



#Cortante
plt.subplot((122))

plt.plot(length,V,label="Cortante",color="royalblue")
plt.title("DEC - V01",fontsize='16')
plt.grid(linestyle='--',linewidth = 0.5)
plt.xticks([0,4.03,9.34,13.40,18.71,24.01,28.09,31.77,37.27])
plt.fill_between(length, V,color="lightsteelblue",alpha=0.5)
plt.legend()

plt.tight_layout()

plt.show()
