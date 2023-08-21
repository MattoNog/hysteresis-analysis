# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:56:39 2023

@author:
"""

#%%
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from scipy.optimize import curve_fit
#from sklearn.linear_model import LinearRegression
#import scipy.stats as stats
from statistics import mean 


#%%
datos = pd.read_csv('C:/Users/Tina/Desktop/el mas capo/ruido/medicion_BHT_ruido.csv') 

h_param = datos["voltaje_H"]
b_param = datos["voltaje_B"]

#%% GRAFICO

plt.figure(figsize=(15,4))
#plt.errorbar(h_param, b_param,  c='purple',  label = "Datos", fmt='o',  ecolor='grey', capsize=2, markersize = 7, elinewidth = 2,)
plt.plot(h_param, b_param, label = 'Gráfico de ruido')
plt.ylabel(r'B [mV]', fontsize=15) 
plt.xlabel(r'H [mV]', fontsize=15)
plt.legend(fontsize = 13)
plt.grid(linestyle='--')
plt.grid(which = 'minor',linestyle=':', linewidth='0.1', color='black' )
plt.plot

#%%

"Asumo que está en mV tanto en H como en B"
"Pongo como error en 0 el promedio de ambos máximos en el supuesto cero"
"Por lo tanto queda definido un offset de toda la config"
"Esto va a tener un error relacionado a los instrumentos???? CONSULTA"

valores_h = [abs(min(h_param)), abs(max(h_param))] 
err_h = mean(valores_h)

valores_b = [abs(min(b_param)), abs(max(b_param))] 
err_b = mean(valores_b)


print("El error del H en el cero es de: ", err_h, "mV")

print("El error del B en el cero es de: ", err_b, "mV")

"Seguramente no usemos este error para H ya que no se anula en el 0"



