import cv2
import numpy as np

guy = cv2.imread("suprised_man.png")

gray = cv2.cvtColor(guy,cv2.COLOR_BGR2GRAY)

gray_blurred = cv2.blur(gray, (3,3))

detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT,1,20,param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)
print(detected_circles)

if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    print(detected_circles)
    for i in detected_circles[0,:]:
        x,y,r=i[0],i[1],i[2]

        cv2.circle(guy, (x,y), r, (200,255,0),2)

    cv2.imshow("detection", guy)
    cv2.waitKey(0)


cv2.destroyAllWindows()