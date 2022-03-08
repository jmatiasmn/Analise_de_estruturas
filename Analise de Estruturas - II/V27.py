import matplotlib.pyplot as plt
import numpy as np
from math import pow
MF = []
length = []
V =[]

for l in np.arange(0, 18.37, 0.001):
    length.append(l)
    if 0 <= l < 3.99:
        MF.append(25.45*l - 7.85*pow(l,2))
        V.append(-15.70*l+25.45)
    elif 3.99 <= l < 6.25:
        MF.append(- 7.85*pow(l,2)+90.361*l-258.98)
        V.append(-15.70*l+90.361)
    elif 6.25 <= l < 9.20:
        MF.append(-7.85 * pow(l,2) + 111.928 * l - 393.773)
        V.append(-15.70*l+111.928)
    elif 9.20 <= l < 14.37:
        MF.append(-7.85 * pow(l,2) + 183.618 * l - 1053.322)
        V.append(-15.70*l+183.618)
    elif 14.37 <= l < 18.37:
        MF.append(-7.85 * pow(l,2) + 265.912 * l - 2235.895)
        V.append(-15.70*l+265.912)

#Momento fletor
plt.subplot((121))
plt.plot(length,MF,label="Momento Fletor",color='silver')
plt.title("DMF - V27",fontsize=16)
plt.grid(linestyle='--',linewidth = 0.5)
plt.xticks([0,3.99,6.25,9.20,14.37,18.37])
plt.fill_between(length, MF,color="silver",alpha=0.5)
plt.gca().invert_yaxis()
plt.legend()



#Cortante
plt.subplot((122))

plt.plot(length,V,label="Cortante",color="royalblue")
plt.title("DEC - V27",fontsize='16')
plt.grid(linestyle='--',linewidth = 0.5)
plt.xticks([0,3.99,6.25,9.20,14.37,18.37])
plt.yticks(range(-50,50,10))
plt.fill_between(length, V,color="lightsteelblue",alpha=0.5)
plt.legend()

plt.tight_layout()

plt.show()
