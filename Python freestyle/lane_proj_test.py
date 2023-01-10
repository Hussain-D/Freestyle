import cv2
import matplotlib.pyplot as plt
import numpy as np


# CONVERT INTO GREY SCALE IMAGE
def grey(image):
    image = np.asarray(image)
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


# GAUSSIAN BLUR TO REDUCE NOISE AND SMOOTHEN THE IMAGE
def gauss(image):
    return cv2.GaussianBlur(image, (5, 5), 0)


# CANNY EDGE DETECTION
def canny(image):
    edges = cv2.Canny(image, 100, 200)
    return edges


# IMPORTING IMAGE
img = cv2.imread("C:/Users/D P Balaiah/Documents/Sem 7/Major Project/Hu/sample lane image.jpg")

# GREYSCALING
grey_img = grey(img)
plt.imshow(grey_img)

# GAUSSIAN BLUR
gaussian_img = gauss(grey_img)
plt.imshow(gaussian_img, cmap="gray")
plt.title('Gaussian Blur'), plt.xticks([]), plt.yticks([])

# CANNY EDGE
canny_img = canny(gaussian_img)
plt.imshow(canny_img, cmap="gray")
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()