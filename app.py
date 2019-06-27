from glob import glob
import cv2

for fn in glob(".\\sample-images\\*.jpg"):
    img = cv2.imread(fn, 0)
    resized_image = cv2.resize(img, (100, 100))
    name = fn.rsplit(".", 1)
    cv2.imwrite(name[0] + "_resized.jpg", resized_image)
