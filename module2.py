import numpy
from matplotlib import pyplot

nx = 41
dx = 2/(nx-1)
nt = 10
dt = .02

x = numpy.linspace(0,2,nx)
u = numpy.ones(nx)
lbound = numpy.where(x >=0.5)
ubound = numpy.where( x <=1 )
u[numpy.intersect1d(lbound, ubound)] = 2

for n in range(1,nt):
	un = u.copy()
	for i in range(1,nx):
		u[i] = un[i] - un[i]*dt/dx*(un[i]-un[i-1])

pyplot.plot(x,u, color = '#003366', ls='--',lw=3)
pyplot.ylim(0,2.5)
pyplot.show()
