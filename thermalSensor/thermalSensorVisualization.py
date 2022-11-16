# serial lib to read teensy input
import serial
import time
# matplotlib for vizualization
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.widgets import RectangleSelector

# function used to select the area of the heatmap, captures the selected pixels and trims down the array accordingly
def onselect_function(eclick, erelease):
    global newpixels
    global extent
    # Obtain (xmin, xmax, ymin, ymax) values
    # for rectangle selector box using extent attribute.
    extent = rect_selector.extents
    #print("Extents: ", extent)

    # Zoom the selected part
    # Set xlim range for plot as xmin to xmax
    # of rectangle selector box.
    plt.xlim(extent[0], extent[1])

    # Set ylim range for plot as ymin to ymax
    # of rectangle selector box.
    plt.ylim(extent[2], extent[3])

    # plot the pixels which are selected
    newpixels = [d[int(extent[0]):int(extent[1])][int(extent[2]):int(extent[3])] for d in data]

# function to animate heatmap with h
def animateheatmap(i):
    global newpixels
    global extent
    line = ser.readline()  # read a byte string
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        arr = string.split(',')[:-1]
        numarray = [float(p) for p in arr]
        numarray = np.reshape(numarray, (16,12))
        print(numarray.shape)

        if len(newpixels)==0:
            data.append(numarray)
            a = data[i]
        else:
            newpixels.append(numarray[int(extent[0]):int(extent[1])][int(extent[2]):int(extent[3])])
            a = newpixels[i]

        ax1.imshow(a, cmap='hot', interpolation='none')


def animateline(i):
    global newpixels
    if len(newpixels) > 0:
        meanvalues = [np.mean(d) for d in newpixels[-50:]]
    else:
        meanvalues = [np.mean(d) for d in data[-50:]]
    x = np.arange(1, len(meanvalues)+1)
    y = meanvalues
    #control line
    upper_limit = np.mean(meanvalues)*1.01
    lower_limit = np.mean(meanvalues)*.99
    ax2.clear()
    ax2.set_xlim(0,len(meanvalues))
    ax2.set_ylim(min(meanvalues)-1,max(meanvalues)+1)
    ax2.set_xlabel('Data point')
    ax2.set_ylabel('Mean temparature')
    ax2.axhline(y=lower_limit, color='Red', label='Control Line')
    ax2.axhline(y=upper_limit, color='Red')
    tmean.set_text("Mean value of the last 50 readings : %.4f Celcius"%np.mean(meanvalues))
    tstd.set_text("Standard Deviation of the last 50 readings : %.4f Celcius"%np.std(meanvalues))
    ax2.axhline(y=np.mean(meanvalues), color='Green', label="Mean of last 50 values")
    ax2.axhline(y=np.mean(meanvalues) + np.std(meanvalues), color='Orange', label="Standard Deviation of last 50 values")
    ax2.axhline(y=np.mean(meanvalues) - np.std(meanvalues), color='Orange')
    ax2.legend(loc="lower left")
    ax2.plot(x,y, color="Black", label="Average Temprature of one capture")


#######################################################
# Main Script flow starts here ########################
#######################################################

# global data variables
newpixels = []
data = []
extent =[]

# initial empty array of the image size
a = np.zeros((16,12))

# defining the serial port to read the data stream
# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM4', 115200, timeout=1)
time.sleep(1)

# initialize a figure
fig=plt.figure()

# 4 columns and 2 rows
# The first plot is on line 1, and is spread all along the 4 columns
ax2 = plt.subplot2grid((2, 4), (0, 0), colspan=4)

# The second one is on column2, spread on 3 columns
ax1 = plt.subplot2grid((2, 4), (1, 0), colspan=3)

# define the metrics to be diaplayed alongside the plots
tmean = ax1.text(15, 5, "Mean value of the last 50 readings :", fontsize=15)
tstd = ax1.text(15, 10, "Standard Deviation of the last 50 readings :", fontsize=15)

# define the plots axis's labels
# ax1.title.set_text('Heatmap of the temprature readings')
# ax2.title.set_text('Mean of the selected pixels')
ax1.set_xlabel('Width')
ax1.set_ylabel('Height')

# animation for the heatmap
ani = FuncAnimation(plt.gcf(), animateheatmap, interval=200)
# animation for the line graph
ani2 = FuncAnimation(fig, animateline, interval=200)

# calling the onselect function in the event when a rectangular portion is selected on the heatmap
rect_selector = RectangleSelector(ax1, onselect_function, drawtype='box', button=[1])

# show the plots
plt.show()

# close the serial port 
ser.close()


