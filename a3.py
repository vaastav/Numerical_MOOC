import numpy as np

def richtymer():

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
