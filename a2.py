import numpy
from matplotlib import pyplot

Vmax = 80 	# (km/hr)
L = 11 		# (km)
pmax = 250 	# (cars/km)
nx = 51
dx = 2/(nx-1)	# km
dt = .0001	# hours
nt = .05/dt + 1 

# Part A
x = numpy.linspace(0,L,nx)
rho0 = numpy.ones(nx)*10
rho0[10:20] = 50

for n in range(1,int(nt)):
	rhon = rho0.copy()
	for i in range(1,nx):
		rho0[i] = rhon[i] - Vmax*(1-2*rhon[i]/pmax)*dt/dx*(rhon[i] - rhon[i-1])
		rho0[0] = 10
	if n == 1:
		max_rho = max(rho0)
		min_V = Vmax * (1 - max_rho/pmax)
		print(min_V)
		

pyplot.plot(x,rho0)
pyplot.show()


