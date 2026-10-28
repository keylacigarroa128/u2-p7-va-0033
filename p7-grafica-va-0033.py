# Keyla Paola NC = 0033 | Fecha 28/octubre/2026
import numpy as np
import matplotlib.pyplot as plt 

no_lista = [1,2,3,17,48]
calificacion_ml = [20,30,80,100,90]
calificacion_va= [70,90,60,90,80]

plt.plot(no_lista,calificacion_ml,label="Calificaciones Machine Learning 0033",color="red",marker="d")
plt.plot(no_lista,calificacion_va,label="Calificaciones Vision Artificial 0033",color="blue",marker="*")

plt.title("Calificaciones materias --- 0033")
plt.xlabel("Numero de lista --- 0033")
plt.ylabel("calificaciones ML / VA  --- 0033")

plt.legend()
plt.show()

print("# Keyla Paola NC = 0033 | Fecha 28/octubre/2026")