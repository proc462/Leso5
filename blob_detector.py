import cv2
import numpy as np

blob = cv2.imread("blob.jpg",0)

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 100

params.filterByCircularity = True
params.minCircularity = 0.8

params.filterByConvexity = True
params.minConvexity = 0.9

params.filterByInertia = True
params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(blob)
print(keypoints)

num_blob = len(keypoints)
print("Number of Blobs:", num_blob)

blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(blob, keypoints, blank, (255,112,46), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

pos = (20,550)
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1.1
color = (249,186,84)
thickness = 3

blobs = cv2.putText(blobs, "Number of Blobs:" + str(num_blob),pos,font,fontscale,color,thickness)

cv2.imshow("Result", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()
