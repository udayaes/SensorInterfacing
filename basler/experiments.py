from pypylon import pylon
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
import imageio
import time

def wait(i):
    print("Waiting for "+str(i)+" secs")
    for j in range(i):
        time.sleep(1)
        print(str(j), end = "... ")

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

camera.Open()
camera.PixelFormat = "BayerBG8"
camera.ExposureTimeAbs = 250000

# demonstrate some feature access
new_width = camera.Width.GetValue() - camera.Width.GetInc()
if new_width >= camera.Width.GetMin():
    camera.Width.SetValue(new_width)

img = [] # some array of images
frames = [] # for storing the generated images
fig = plt.figure()

numberOfImagesToGrab = 1
camera.StartGrabbingMax(numberOfImagesToGrab)
while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(1000, pylon.TimeoutHandling_ThrowException)
    if grabResult.GrabSucceeded():
        # Access the image data.
        #print("SizeX: ", grabResult.Width)
        #print("SizeY: ", grabResult.Height)
        # img = grabResult.Array
        #print("image array", grabResult)
        # imageio.imsave('image_bayer.bmp', img)

        # create and configure ImageFormatConverter
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_RGB8packed

        # convert image to RGB, create NumPy array
        # and save RGB image as color BMP
        converted = converter.Convert(grabResult)
        image_rgb = converted.GetArray()
        print("RGB", image_rgb.shape)
        imageio.imsave('images/disimages/distorted_8.jpg', image_rgb)
        print("Captured")
        

        # plotting
        frames.append([plt.imshow(image_rgb, cmap=cm.Greys_r,animated=True)])

    grabResult.Release()
ani = animation.ArtistAnimation(fig, frames, interval=1000, blit=True,
                                repeat_delay=1000)
camera.Close()
plt.show()