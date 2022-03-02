import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image
import cv2

def convolution2d(image,ker,stride,padding):
    print(ker)
    def invertkernel(k):
        hk,wk=np.shape(k)
        new=np.zeros([hk,wk])
        new2=np.zeros([hk,wk])
        for i in range(hk):
            new[i,:]=ker[hk-i-1,:]
    
        for j in range(wk):
            new2[:,j]=new[:,wk-j-1]
        #print (new2)
        return new2

    kernel=invertkernel(ker)
    k1,k2=np.shape(kernel)#kernel size
    h=np.shape(image)[0]
    w=np.shape(image)[1]
    x_pad,y_pad=padding[0,0],padding[1,0]#padding size
    H,W=h+2*x_pad,w+2*y_pad#size of padded img
    
    if(image.ndim==2):
        new=np.zeros((H,W))#zero matrix (+padded ) 
        c_img=np.zeros((H-k1,W-k2))#output img zero matrix
        for i in range(H):
            for j in range(W):
                if i<x_pad or j<y_pad or i>=(h+x_pad) or j>=(w+y_pad):
                   new[i,j]=0
                else:
                    new[i,j]=image[i-x_pad,j-y_pad]
        s1,s2=stride[0,0],stride[1,0]
        for i in range(k1//2,H-k1//2,s1):
            for j in range(k2//2,W-k2//2,s2):
                temp=0
                for p in range(k1):
                    for q in range(k2):
                        temp+=kernel[p,q]*new[i+p-k1//2][j+q-k2//2]  
                if temp>255:
                    temp=255
                if temp<0:
                    temp=0
                c_img[i-k1//2-1,j-k2//2-1]=temp       
    else:
        new=np.zeros((H,W,3))#zero matrix (+padded ) 
        c_img=np.zeros((H-k1,W-k2,3))#output img zero matrix
        for k in range(3):
            for i in range(H):
                for j in range(W):
                        if i<x_pad or j<y_pad or i>=(h+x_pad) or j>=(w+y_pad):
                            new[i,j,k]=0
                        else:
                            new[i,j,k]=image[i-x_pad,j-y_pad,k]
        s1,s2=stride[0,0],stride[1,0]
        for k in range(3):
            for i in range(k1//2,H-k1//2,s1):
                for j in range(k2//2,W-k2//2,s2):
                        temp=0
                        for p in range(k1):
                            for q in range(k2):
                                temp+=kernel[p,q]*new[i+p-k1//2,j+q-k2//2,k]  
                        if temp>255:
                            temp=255
                        if temp<0:
                            temp=0
                        c_img[i-k1//2-1,j-k2//2-1,k]=temp     

    c_img=c_img.astype(np.uint8)
    # cv2.imshow("Input_image", image)
    # cv2.imshow("convolution",c_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return c_img.astype(np.uint8)

# if __name__ == '__main__':
#     #K= np.array([[1,0,-1],[0,0,0],[-1,0,1]])
#     #K= np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
#     #K = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
#     #K= np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
#     #K= np.array([[1,1,1],[1,1,1],[1,1,1]])/9
#     #K = np.array([[1,2,1], [2,4,2], [1,2,1]])/16
#     #K = np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])/256

#     stride=np.array([[1],[1]])
#     padding=np.array([[1],[1]])
#     # stride= np.array([[2], [3]])
#     # padding= np.array([[1], [1]])
#     #image = cv2.imread("cameraman.png",0)
#     #img= cv2.imread("Lena.png")
#     #image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

#     img=Image.open("Lena.jpg")
#     #img=Image.open("cameraman.png")
#     image=np.asarray(img)
#     convolution2d(image,K,stride,padding)
#     #print(convolution2d(image,K,stride,padding))








