import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('alpha_mser.png',0)
thresh={}
for i in range(7):
	ret,thresh[i] = cv2.threshold(img,255-i*15,255,cv2.THRESH_BINARY)

#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
#ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Input Image','g=255','g=240','g=225','g=210','g=195','g=180','g=165']
images = [img, thresh[0],thresh[1], thresh[2], thresh[3], thresh[4],thresh[5],thresh[6]]
for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    cv2.imwrite(titles[i]+'.png',images[i])
plt.show()
