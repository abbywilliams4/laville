import pandas as pd
# for plots and figs
from matplotlib import pyplot as plt
#for using arrays
import numpy as np

df = pd.read_csv(R"C:\Users\valle\Downloads\coda1.csv")
fig, (ax1) = plt.subplots(1)
#fig.suptitle("X2")
ax1.plot(df['Time'],df['X2'])
#fig.suptitle("Y2")
ax1.plot(df['Time'],df['Y2'])
#fig.suptitle("Z2")
ax1.plot(df['Time'],df['Z2'])

ax1.legend(('X2','Y2','Z2'))
ax1.set_ylabel('Magnitude (mm)')
ax1.set_xlabel('Time (s)')
ax1.set_title('Magnitude of Vector Components vs Time')
plt.show()

#plt.plot(df['Time'], df['X2'])
#plt.plot(df['Time'], df['Y2'])
#plt.plot(df['Time'], df['Z2'])
#plt.ylabel('Magnitude')
#plt.xlabel('Time (s)')
#plt.show()

#convert values to numeric instead of object because cannot graph without numerical data
#need to graph all coordinates for each marker (ex: X2, Y2, Z2) over Time, and create a legend 