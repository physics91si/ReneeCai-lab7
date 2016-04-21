import scipy as sci
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
velocity = np.loadtxt('droptower_vdata.txt', unpack = True)
justvel = np.array([velocity[(1,0)],velocity[(1,1)],velocity[(1,2)],velocity[(1,3)],velocity[(1,4)],velocity[(1,5)],velocity[(1,6)],
                    velocity[(1,7)],velocity[(1,8)],velocity[(1,9)],velocity[(1,10)]])
position = sci.integrate.cumtrapz(justvel, initial = 0)

time = np.arange(0,11,1)

graph1 = plt.plot(time,position,'r:',lw=3,label='Position')
plt.xlabel('Time')
plt.ylabel('Position') 
plt.title('Position v. Time')
plt.show()
    
    
plt.plot(time,justvel,'b--',lw=5)
plt.xlabel('Time')
plt.ylabel('Velocity') 
plt.title('Velocity v. Time')
plt.show()

accel = np.diff(justvel)/time[1:11]
plt.plot(time[1:11],accel,'m-.',lw=5)
plt.xlabel('Time')
plt.ylabel('Acceleration') 
plt.title('Acceleration v. Time')

plt.plot(time,position,'c--',time,justvel,'r:',time[1:11],accel,'g-',lw=4)
plt.xlabel('Time')


plt.title('Change in Position, Velocity, and Acceleration over Time',fontsize=15)
