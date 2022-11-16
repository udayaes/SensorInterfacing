# importing python wrapper for the basler camera
from pypylon import pylon
# imageio to export images to files
import imageio
# to store the calibration matrix
import pickle
# opencv
import cv2
# time library
from datetime import datetime

# define the camera module to be used
camera = pylon.InstantCamera(
    pylon.TlFactory.GetInstance().CreateFirstDevice())

# open/start the camera
camera.Open()
# define the camera input params
camera.PixelFormat = "BayerBG8"
camera.ExposureTimeAbs = 250000

#list for images
img_list = []

# loop listening for events to take picture
while True:
    # user input to capture or exit
    i = input("Type 'c' and press Enter to capture and any other key if done ..\n")

    # if user initiated capture
    if i == 'c':
        # grap the camera output
        result = camera.GrabOne(1000)

        # create and configure ImageFormatConverter
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_RGB8packed

        # convert image to RGB, create NumPy array
        # and save RGB image as color BMP
        converted = converter.Convert(result)
        image_rgb = converted.GetArray()
        print("RGB", image_rgb.shape)

        #file name
        #increasing the count
        timestamp = datetime.now().strftime("%m_%d_%y__%H_%M_%S")
        file_name = 'capture{}.jpg'.format(timestamp)
        # save the original image
        imageio.imsave('images/{}'.format(file_name), image_rgb, plugin='DICOM')
        print("Captured")

        # Getting calibration matrix from the pickle file
        file_to_read = open("images/wide_dist_pickle.p", "rb")
        calibration_matrix = pickle.load(file_to_read)
        mtx = calibration_matrix['mtx']
        dist = calibration_matrix['dist']

        # reading the original image and undistorting it
        img = cv2.imread('images/{}'.format(file_name))
        dst = cv2.undistort(img, mtx, dist, None, mtx)

        # saving the undistorted image
        cv2.imwrite("images/calibrated/{}".format(file_name),dst)
        img_list.append(file_name)
    
    # if user input is not for capture, exit the loop
    else:
        print("Capturing complete")
        break
