"""Write a generalised function called ‘normalisation’ for any coloured or grey image to perform image normalisation of the following types :
a. Pixel Normalization: scale pixel values to the range 0-1.
b. Pixel Centering: scale pixel values to have a zero mean.
c. Pixel Standardization: scale pixel values to have a zero mean and unit variance."""

#importing libraries
import numpy as np
import cv2

def normalization(Input_img,pn=True,pc=False,ps=False): 
    
    if pn or pc or ps: #normalization centering or standardization
        Input_img= Input_img/255
        mean, var = np.mean(Input_img), np.var(Input_img)
        range= [np.min(Input_img),np.max(Input_img)]

    if pc or ps: #centering or standardization
        Input_img=Input_img-mean
        mean, var = np.mean(Input_img), np.var(Input_img)
        range= [np.min(Input_img),np.max(Input_img)]

    if ps: # pixel standardization
        Input_img= Input_img/np.sqrt(var)
        mean, var = np.mean(Input_img), np.var(Input_img)
        range= [np.min(Input_img),np.max(Input_img)]

    return Input_img, mean, range ,var

if __name__=='__main__':
    #reading image
    Input_img = cv2.imread('8bit gray image.jpg') 
    #calling function
    Input_img, mean, range ,var = normalization(Input_img,False,False,True)
    #showing image for 1 second 
    cv2.imshow("",Input_img)
    cv2.waitKey(1000) # waiting 1 second for output 
    print(mean, range ,var)