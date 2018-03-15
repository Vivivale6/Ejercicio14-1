import numpy as np
import matplotlib.pyplot as plt

sol=np.loadtxt("monthrg.dat")
years=sol[:,0]
month=sol[:,1]
dia=sol[:,2]
manchas=sol[:,3]
time=years+(month-1)/12.0


ii = (time>1900)

datos=np.array([time[ii],manchas[ii]])
final=np.savetxt("fecha_manchas.dat",datos.T)
