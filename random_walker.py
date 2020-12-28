# Python code for 2D random walk. 
import numpy as np
import matplotlib.pyplot as plt
# number of steps 
n = 100000
  
# x and y coordinate 
x = np.zeros(n) 
y = np.zeros(n) 

# Loop
for i in range(1, n): 
    
    step = np.random.uniform(0,1)
    print(step)
    if step >= 0.5: 
        # Right
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] 
    elif step >= 0.7: 
        # Left
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] 
    elif step >= 0.9: 
        # Up
        x[i] = x[i - 1] 
        y[i] = y[i - 1] + 1
    else: 
        # Down
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - 1

    walker_x = [x[i-1],x[i]]
    walker_y = [y[i-1],y[i]]
    plt.plot(walker_x,walker_y,'b-')
    plt.pause(0.05)

plt.show()
