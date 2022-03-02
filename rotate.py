# import numpy as np 
# import cv2
# import matplotlib.pyplot as plt
# from PIL import Image
# from numpy import cos,sin

def rotate_image(input_image, angle):
    theta=np.radians(angle)
    image=Image.open(input_image)
    image=np.array(image)
    x,y=image.shape[0],image.shape[1]
    c1,c2=x//2,y//2
    # plt.imshow(image,cmap='gray')#input image
    # plt.show()

    X=x*cos(theta)+y*sin(theta)
    Y=x*sin(theta)+y*cos(theta)
    X,Y=abs(int((X+1))),abs(int((Y+1)))
    C1,C2=X//2,Y//2
    output_image=np.zeros((X,Y))
    
    for i in range(x):
        for j in range(y):
            var1,var2=i-c1,j-c2
            var3,var4=var1*cos(theta)-var2*(sin(theta)),(var1)*sin(theta)+var2*(cos(theta))
            var3,var4=var3+C1,var4+C2
            var3,var4=int(var3),int(var4)
            output_image[var3,var4]=image[i,j]
    # plt.imshow(output_image,cmap='gray') # output image before interpolation
    # plt.show()

    for i in range(X):
        for j in range(Y):
            if output_image[i,j]==0:
                try:
                    output_image[i,j]=output_image[i,j+1]
                except:
                    output_image[i,j]=output_image[i,j-1]
    
    output_image=output_image.astype(np.uint8)
    # plt.imshow(output_image,cmap='gray') #output_image after interpolation
    # plt.show()
    return(output_image)

# if __name__ == '__main__':
#     input_image="cameraman.png"
#     print(rotate_image(input_image, 45))