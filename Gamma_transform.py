# import numpy as np
# import cv2

def contrast_streching(image_path,r1,r2,s1,s2):
    #calculating slopes
    m1=s1/r1
    m2=(s2-s1)/(r2-r1)
    m3=(255-s2)/(255-r2)
    #reading image
    img=cv2.imread(image_path)#use opencv for reading image
    #shape of the image
    shape=np.shape(img)
    h,w=shape[0],shape[1]

    #func for different conditions according to the values given
    def update(val):
        if val<r1:
            return m1*val
        if val<r2:
            return m2*(val-r1)+s1
        return m3*(val-r2)+s2
    op=np.zeros(shape)
    for i in range(h):
        for j in range(w):
            for k in range(3):
                op[i,j,k]=update(img[i,j,k])

    op=op.astype(np.uint8)
    print(op,op.shape)
    cv2.imshow('original',img)
    cv2.imshow('image_after_contrast_streching',op)
    cv2.waitKey(0)
    return op



# if __name__ == '__main__':
#     path="cameraman.png"
#     #uncomment following if running manually
#     # contrast_streching(path,50,100,80,200)


