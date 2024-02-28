import cv2

img = cv2.imread("hi.png")
if img is not None:
    cv2.imshow("tital", img)
    img_re = cv2.resize(img, (250, 250))
    cv2.imwrite("new_hi.png", img_re)
    cv2.imshow("new", img_re)
    cv2.waitKey(0)
else:
    print("Warning: Could not load the image.")
