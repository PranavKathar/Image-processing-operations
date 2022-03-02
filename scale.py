# import numpy as np 
# import cv2
# import matplotlib.pyplot as plt
# from PIL import Image


def scale_image(input_image, scaling_factor):
    a=scaling_factor
    image=Image.open(input_image)
    image=np.array(image)
    x,y=image.shape[0],image.shape[1]
    # plt.imshow(image,cmap='gray')#input image
    # plt.show()

    output_image = np.zeros((a*x,a*y))
    for i in range(a*x):
        for j in range(y*a):
            output_image[i,j]=image[i//a,j//a]
    # plt.imshow(output_image,cmap='gray')#output image
    # plt.show()
    return(output_image)

# if __name__ == '__main__':
#     input_image="cameraman.png"
#     #print(scale_image(input_image, 2))

