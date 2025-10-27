##########################################
# Delage, Raphaël, 2441671
##########################################
import random as rd
import numpy as np
import matplotlib.pyplot as plt
#Question 1
def temperature(jour):
    jour+=1
    while jour > 1:
        temperature_jour = round(rd.uniform(20, 35), 1)
        jour -= 1
        if temperature_jour < 24:
            resultat='Trop froid'
        elif temperature_jour > 30:
            resultat='Trop chaud'
        else:
            resultat='OK'
        print('Jour', jour, ':', temperature_jour)
        print(resultat)
print('Fin')
temperature(10)
#Question 2
population_initiale=int(input('Population bactérie initiale :'))
def population(heure):
    return population_initiale*(np.pi/1.5*heure)

tableau=np.linspace(0,population(10),11)
plt.figure(figsize=(1,1))
plt.plot(tableau)
plt.plot(160000)
plt.title('Croissance bactérienne')
plt.ylabel('Population')
plt.xlabel('Heure')
plt.show()
plt.grid()
print(tableau)










