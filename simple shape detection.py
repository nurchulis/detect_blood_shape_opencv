import cv2
import numpy as np

# Read image
im_in = cv2.imread("darah4.jpg", cv2.IMREAD_GRAYSCALE);
 
# Threshold.
# Set values equal to or above 220 to 0.
# Set values below 220 to 255.
 
th, im_th = cv2.threshold(im_in, 220, 255, cv2.THRESH_BINARY_INV);
 
# Copy the thresholded image.
im_floodfill = im_th.copy()
 
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255);
 
# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
 
# Combine the two images to get the foreground.
im_out = im_th | im_floodfill_inv



#img = cv2.imread("darah4.jpg", cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(im_floodfill_inv, 240, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
font = cv2.FONT_HERSHEY_COMPLEX



nilai_c=1
nilai_e=1
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.001*cv2.arcLength(cnt, True), True)
    cv2.drawContours(im_in, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if 6 < len(approx) < 15:
        cv2.putText(im_in, "Pupil", (x, y), font, 1, (0))
        nilai_e=nilai_e+1
    else:
        cv2.putText(im_in, "Circle", (x, y), font, 1, (0))
        nilai_c=nilai_c+1

cv2.imshow("shapes", im_in)
cv2.imshow("Threshold", im_floodfill_inv)
print "Jumlah Shell berbentuk Circle adalah =",nilai_c
print "Jumlah Shell berbentuk Pupil adalah =",nilai_e
cv2.waitKey(0)
cv2.destroyAllWindows()