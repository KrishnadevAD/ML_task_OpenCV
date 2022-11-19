import numpy as np 
import cv2
from math import  sqrt
#import cv2


image= cv2.imread('img.png')
original_image= image

gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges= cv2.Canny(gray, 50,200)

img_gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh2 = cv2.threshold(img_gray2, 150, 255, cv2.THRESH_BINARY)


contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

def get_contour_areas(contours):

    all_areas= []

    for cnt in contours:
        area= cv2.contourArea(cnt)
        all_areas.append(area)

    return all_areas


sorted_contours= sorted(contours, key=cv2.contourArea, reverse= False)

font = cv2.FONT_HERSHEY_SIMPLEX
for i in range(0,4):
  smallest_item= sorted_contours[i]
  x=smallest_item[-1][0][0]
  y=smallest_item[-1][0][1]+78
  cv2.putText(original_image, str(i+1), (x,y),font, 1, (0, 255, 0), 2, cv2.LINE_AA)

# print(smallest_item[1][0])
# print(smallest_item)

if smallest_item[0][0][1] < smallest_item[1][0][1] and smallest_item[0][0][0] < smallest_item[1][0][0] :
    large = smallest_item[0][0][0]
    large1 = smallest_item[0][0][1]
    for i in range(0,len(smallest_item)):
        if large < smallest_item[i][0][0]:
            large=smallest_item[i][0][0]
        if large1 < smallest_item[i][0][1]:
            large1 = smallest_item[i][0][1]
    x1=smallest_item[0][0][0]
    y1=smallest_item[0][0][1]

    # x2=smallest_item[-1][0][0]
    x2 = large

    y2=large1

    d=sqrt((pow((x1-x2),2))+(pow((y1-y2),2)))
else:
    large = smallest_item[0][0][0]
    min_y = smallest_item[0][0][1]
    for i in range(0, len(smallest_item)):
        if large < smallest_item[i][0][0]:
            large = smallest_item[i][0][0]
        if min_y > smallest_item[i][0][1]:
            min_y = smallest_item[i][0][1]
    x1 = smallest_item[0][0][0]
    y1 = smallest_item[0][0][1]

    # x2=smallest_item[-1][0][0]
    x2 = large

    y2 = min_y

    d = sqrt((pow((x1 - x2), 2)) + (pow((y1 - y2), 2)))



print(d)
cv2.waitKey(0)
cv2.imshow("og",original_image)
# cv2.imshow("og",edges)


cv2.waitKey(0)
cv2.destroyAllWindows()
# print(sorted_contours[0])
print(x1,y1,x2,y2)
print(smallest_item)