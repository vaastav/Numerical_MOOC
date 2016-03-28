import numpy as np

def compute_internal_energy( u, e_T, gamma ):
	internal_energy = e_T + u*u/2
	return internal_energy

def compute_pressure( rho, e, gamma ):
	pressure = ( gamma - 1 ) * rho * e
	return pressure

def compute_flux( u, rho, e_T, gamma ):
	flux = []
	flux += [ rho * u ]
	internal_energy = compute_internal_energy( u, e_T, gamma )
	pressure = ( rho, internal_energy, gamma )
	flux += [ rho*u*u + pressure ] 
	flux += [ ( rho*e_T + pressure ) * u ]
	return flux

nx = 81
dx = .25
dt = .0002
nt = .05/dt + 1
gamma = 1.4

# Initial conditions on the left side

rho_L = 1     # kg/m^3
mu_L = 0      # m/s
p_L = 100     # kN/m^2

# Initial conditions on the right side

rho_R = 0.125 # kg/m^3
mu_R = 0      # m/s
p_R = 10      # kN/m^2

