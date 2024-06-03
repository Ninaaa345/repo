import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


% Wärmeübertrager
# Constants
U = 100.0  # Overall heat transfer coefficient (W/m^2-K)
A = 1.0  # Heat transfer area (m^2)
m_dot_c = 0.1  # Mass flow rate of cold fluid (kg/s)
m_dot_h = 0.1  # Mass flow rate of hot fluid (kg/s)
Cp_c = 4186.0  # Specific heat capacity of cold fluid (J/kg-K)
Cp_h = 4186.0  # Specific heat capacity of hot fluid (J/kg-K)
T_c_in = 20.0  # Inlet temperature of cold fluid (C)
T_h_in = 80.0  # Inlet temperature of hot fluid (C)

# ODEs
def heat_exchanger_ode(T, t):
    T_c, T_h = T
    dT_c_dt = (U*A*(T_h - T_c))/(m_dot_c*Cp_c)
    dT_h_dt = -(U*A*(T_h - T_c))/(m_dot_h*Cp_h)
    return [dT_c_dt, dT_h_dt]

# Time array
t = np.linspace(0, 500, 500)

# Solve ODEs
T = odeint(heat_exchanger_ode, [T_c_in, T_h_in], t)

# Plot results
plt.plot(t, T[:, 0], 'b-', label='T_c')
plt.plot(t, T[:, 1], 'r-', label='T_h')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (C)')
plt.legend(loc='best')
plt.grid()
plt.show()