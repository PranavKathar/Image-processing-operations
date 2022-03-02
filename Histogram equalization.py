# import numpy as np 
# import cv2
# import matplotlib.pyplot as plt
# from PIL import Image

def histogram_equalization(input_image):
    image=Image.open(input_image)
    image=np.array(image)
    x,y=image.shape[0],image.shape[1]
    # cv2.imshow("ip",image)
    # cv2.waitKey(0)
    output_image = np.zeros_like(image)

    if (image.ndim==2):
        h,bins= np.histogram(image,bins=256)
        pdf=h/(x*y)
        cdf=(255*(np.cumsum(pdf))).astype(np.uint8)
        for i in range(x):
            for j in range(y):
                output_image[i,j]=cdf[image[i,j]]

    else:
        for k in range(3):
            h,bins= np.histogram(image[:,:,k],bins=256)
            
            pdf=h/(x*y)
            cdf=(255*(np.cumsum(pdf))).astype(np.uint8)
            for i in range(x):
                for j in range(y):
                    output_image[i,j,k]=cdf[image[i,j,k]]
    
    # plt.imshow(output_image)
    # plt.show()
    return(output_image) 

# if __name__ == '__main__':
#     #input_image="cameraman.png"
#     input_image="Lena.jpg"
#     print(histogram_equalization(input_image))