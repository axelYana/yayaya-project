import cv2
import numpy as np



def load_and_display(file):
   img=cv2.imread(file,0)
   cv2.imshow('image', img)
   cv2.waitKey(100000)
   cv2.destroyAllWindows()



def process_image(filename): #rotation#
    img = cv2.imread(filename,0)
    rows,cols = img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    cv2.imshow('image',dst)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
process_image(r'/Users/ayoub/yayaya-project/data/tetris_blocks.png')


