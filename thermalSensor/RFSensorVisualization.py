# serial lib to read teensy input
import serial
import time
# import matplotlib for plotting the output
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Function to animate the line sync with input
def animateline(i):
    line = ser.readline()  # read a byte string
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        data.append(int(string))
    # clear the axis and plot the new input data
    ax.clear()
    ax.axhline(y=np.mean(data[-20:]), color='Green', label='Mean')
    ax.axhline(y=np.mean(data[-20:])*1.01, color='Red', label='Control Line')
    ax.axhline(y=np.mean(data[-20:])*0.99, color='Red')
    ax.legend(loc="upper left")
    ax.plot(data[-20:], color="Blue")

#######################################################
# Main Script flow starts here ########################
#######################################################

# datas array for the inputs stream
data = []

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM5', 9600, timeout=2)
time.sleep(2)

# define the plot
fig, ax = plt.subplots()

# plot's axes and label
ax.title.set_text("Magnetic sensor reading")
ax.set_xlabel('# of reading')
ax.set_ylabel('Analog output')

# calling the defined function to make the plot dynamic
ani = FuncAnimation(fig, animateline, interval=500)

# show the plot
plt.show()

# close the serializer
ser.close()