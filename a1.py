import numpy as np # For pi

time_step = 0.1 # Time step for Euler's method (s)
ms = 50		# Mass of the rocket shell (kg)
Cd = 0.15	# Drag coefficient
ve = 325	# Exhaust speed (m/s)
g = 9.81	# Acceleration due to gravity (m/s^2)
p = 1.091	# Average air density (kg/m^3)
A = np.pi * 0.5 * 0.5 # Maximum cross sectional area of the rocket
mpo = 100	# Initial mass of rocket propellant (kg) 
rate = 20	# Propellant burn rate (kg/s)

def remaining_mass(t):
	"""
	Calculates the mass of the remaining propellant

	@param t Time at which the mass needs to be calculated
	
	"""
	if t >= 5:
		return 0
	else :
		return mpo - rate*t

def calc_velocity(t,v):
	mp = remaining_mass(t)
	if t >= 5:
		mpdot = 0
	else:
		mpdot = 20
	dv = mpdot*ve -g*(ms + mp) -0.5*p*v*A*Cd*abs(v)
	dv = dv/(ms + mp)
	velocity = v + time_step*dv
	return velocity

def calc_flight_path():
	# Arrays to store velocity and height
	N = 600
	v = np.zeros(N)
	h = np.zeros(N)
	t = np.zeros(N)

	# Initial condition
	h[0] = 0.
	v[0] = 0.
	t[0] = 0.
	time = 0
	i = 1
	while True:
		time = time + time_step
		v[i] = calc_velocity(time,v[i-1])
		h[i] = h[i-1] + v[i-1] * time_step
		if h[i] < 0:
			break
		t[i] = time
		i += 1
	return v,h,t

