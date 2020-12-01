# Import packages
import matplotlib.pyplot as plt
import numpy as np

def h_of_t(t):
    # Return height of pool given time
    
    C_d = 180
    A_pool = 5 * 10
    h_0 = 3
    
    return (np.sqrt(h_0) - C_d/(2 * A_pool) * t)**2

# Generate time values on which to evaulate h 
t = np.arange(0,1,0.01)

# Use the map function to evaluate h at all t provided
# convert to list for plotting
h = list(map(h_of_t,t))

# Make a pretty plot.
plt.figure(figsize=(8,6))
plt.plot(t,h,color='grey',linestyle='--')
plt.xlabel('Time [hr]')
plt.ylabel('Height of Water in Pool [m]')
plt.title('Water Height vs. Time')
plt.xticks([0,0.5,1])
plt.yticks([0,1.5,3])

# Show the plot.
plt.show()