# import numpy as np 
# import cv2
# import matplotlib.pyplot as plt
# from PIL import Image

def gray_slicing(input_image, thr1, thr2):
    image=Image.open(input_image)
    image=np.array(image)
    x,y=image.shape[0],image.shape[1]
    # plt.imshow(image,cmap='gray') #innput image
    # plt.show()
    if (image.ndim==2):
        z1=np.zeros((x,y))
        z2=np.zeros((x,y))
        for i in range(x):
            for j in range(y):
                if(image[i,j]>thr1 and image[i,j]<thr2):
                    z1[i,j]=255
                    z2[i,j]=255
                else:
                    z1[i,j]=image[i,j]
                    z2[i,j]=0
    
    else:
        z1=np.zeros((x,y,3))
        z2=np.zeros((x,y,3))
        for i in range(x):
            for j in range(y):
                for k in range(3):
                    if(image[i,j,k]>thr1 and image[i,j,k]<thr2):
                        z1[i,j,k]=255
                        z2[i,j,k]=255
                    else:
                        z1[i,j,k]=image[i,j,k]
                        z2[i,j,k]=0

        z1=z1.astype(np.uint8)
        z2=z2.astype(np.uint8)
    output_image_with_background=z1
    output_image_without_background=z2
    # plt.imshow(z1)#output_image_with_background
    # plt.show()
    # plt.imshow(z2)#output_image_with_background
    # plt.show()

    return(output_image_with_background, output_image_without_background)

# if __name__ == '__main__':
#     #input_image="cameraman.png"
#     input_image="Lena.jpg"
#     #print(gray_slicing(input_image, 50, 150))
