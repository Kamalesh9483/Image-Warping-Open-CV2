import cv2
import numpy as np


img = cv2.imread("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Warp Prespective/Original.jpg")

# Size of A4 sheet in Pixels
width = 595
height = 842

p1 = np.float32([[419,195],[792,250],[3,563],[601,757]])
p2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(p1,p2)
output = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Original",img)
cv2.imshow("Perspective",output)
cv2.waitKey(0)