# import numpy as np
# import cv2

def gamma_transform(image_path,gamma):
    img= (cv2.imread(image_path))/255
    op=255*(np.power(img,gamma))
    op=op.astype(np.uint8)

    print(op,op.shape)
    cv2.imshow('original',img)
    cv2.imshow("gamma transform",op)
    cv2.waitKey(0)
    return op


# if __name__ == '__main__':
#     path="cameraman.png"
#     #uncomment following if running manually
#     gamma_transform(path,1.2)
