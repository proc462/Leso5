import cv2
beach = cv2.imread("beach.jpg")

color = (0,70,125)
thickness = -15
t2 = 15
c2 = (0,0,0)
t3 = 3
t4 = 10

sp = (600,720)
ep = (900,470)

sp5 = (900,470)
ep5 = (750,320)

sp6 = (600,470)
ep6 = (750,320)

sp2 = (710,720) 
ep2 = (790,575)

sp3 = (775,645)
ep3 = (775,645)

second = cv2.rectangle(beach,sp,ep,color,thickness)
fifth = cv2.line(second,sp5,ep5,color,t2)
sixth = cv2.line(fifth,sp6,ep6,color,t2)
second = cv2.rectangle(sixth,sp2,ep2,c2,t3)
third = cv2.line(second,sp3,ep3,c2,t4)

cv2.imshow("hut", third)
cv2.waitKey(0)
cv2.destroyAllWindows()