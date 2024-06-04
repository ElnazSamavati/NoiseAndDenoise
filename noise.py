import cv2
import numpy as np
from skimage import img_as_ubyte

#orginal image
img = cv2.imread("C:\\Users\\yukiy\\Downloads\\Dandelion.jpg", 0)
img = img/255

cv2.imshow('original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#blank image
x,y = img.shape
g = np.zeros((x,y), dtype=np.float32)

#salt and pepper amount
#نویز 50 درصد میباشد... برای 10 درصد فقط کافی است پپر را 0.05 و برای 25 درصد 0.125 بنویسیم
pepper = 0.25
salt = 1 - pepper

#create salt and pepper noise image
for i in range(x):
    for j in range(y):
        rnd=np.random.random()
        if rnd < pepper:
            g[i][j] = 0
        elif rnd > salt:
            g[i][j] = 1
        else:
            g[i][j] = img[i][j]

cv2.imshow('image with noise', g)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_noise = g
## denoise image
# mean filter (average)
m = 5
n = 5
denoise_mean = cv2.blur(img_noise, (m,n))

# median filter
img_noise_median = np.clip(img_noise, -1, 1) #pixel value range
img_noise_median = img_as_ubyte(img_noise_median) #convert to uint8
denoise_median = cv2.medianBlur(img_noise_median, 5)


cv2.imshow('Denoise Mean', denoise_mean)
cv2.imshow('Denoise Median', denoise_median)

cv2.waitKey(0)
cv2.destroyAllWindows()
