import cv2
import numpy as np

# Read image.
img = cv2.imread('Bilder/Bild_2.png', cv2.IMREAD_COLOR)
img=img[110:110+278,192:191+291]
img2=cv2.Canny(img, 1,2)

# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = img

# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (1, 1))
#gray_blurred = gray

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 5, param1=1,param2=12, minRadius=6, maxRadius=10)

# Draw circles that are detected.
if detected_circles is not None:

    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
    i=1
    cv2.imshow("Detected Circle", img)
    cv2.waitKey(0)
