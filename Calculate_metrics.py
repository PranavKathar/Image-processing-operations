# #importing libraries
# import numpy as np 
# from PIL import Image
# import cv2
# import matplotlib.pyplot as plt

def calculate_metrics(ndarray_image):
	""" generalised function for any coloured or grey image and
    custom image dimensions to evaluate the mean and standard
    deviation of the pixels of an image. Also, return the histogram of the
    pixel values that will be a 3D vector for coloured images and 2D
    vector for grey images."""

    #color image
    if(ndarray_image.ndim==3):
        res = np.shape(ndarray_image)
        total_pixels=res[0]*res[1]
        #mean
        sum=np.array([0.0,0.0,0.0])
        for i in range(res[0]):
            for j in range(res[1]):
                for k in range(3):
                    sum[k]=sum[k]+ndarray_image[i,j,k] 
        mean= sum/total_pixels

        #standard_deviation
        std=np.array([0.0,0.0,0.0])
        for i in range(res[0]):
            for j in range(res[1]):
                for k in range(3):
                    std[k]=std[k]+ np.square(ndarray_image[i,j,k]-mean[k]) 
        temp=std/total_pixels
        standard_deviation= np.sqrt(temp)

        #histogram
        hist=np.zeros((1,256,3),dtype=int)
        for i in range(res[1]):
            for j in range(res[0]):
                for k in range(3):
                    hist[0][ndarray_image[j,i,k]][k]+=1 
    #grey image
    elif ndarray_image.ndim == 2:
      
        res = np.shape(ndarray_image)
        total_pixels=res[0]*res[1]
        #mean
        sum=np.array([0.0])
        for i in range(res[0]):
            for j in range(res[1]):
                sum[0]=sum[0]+ndarray_image[i,j] 
        mean= sum/total_pixels

        #standard_deviation
        std=np.array([0.0])
        for i in range(res[0]):
            for j in range(res[1]):
                std[0]=std[0]+ np.square(ndarray_image[i,j]-mean[0]) 

        standard_deviation= np.sqrt(std/total_pixels)

        #histogram
        hist=np.zeros((1,256),dtype=int)
        for i in range(res[0]):
            for j in range(res[1]):
                hist[0,(ndarray_image[i,j])]+=1

    return mean,standard_deviation,hist

# ndarray_image = np.asarray(Image.open('lena.jpg'))
# print(calculate_metrics(ndarray_image))


 
