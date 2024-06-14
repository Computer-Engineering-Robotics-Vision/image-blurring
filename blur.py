import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an image
image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for displaying with matplotlib

# Apply different blurring techniques

# 1. Averaging
kernel_size = (5, 5)
blurred_average = cv2.blur(image, kernel_size)

# 2. Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# 3. Median Blur
median_blur = cv2.medianBlur(image, 5)

# 4. Bilateral Filter
bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75)

# Display the results using matplotlib
plt.figure(figsize=(12, 8))

plt.subplot(231), plt.imshow(image), plt.title('Original Image')
plt.subplot(232), plt.imshow(blurred_average), plt.title('Average Blurring')
plt.subplot(233), plt.imshow(gaussian_blur), plt.title('Gaussian Blurring')
plt.subplot(234), plt.imshow(median_blur), plt.title('Median Blurring')
plt.subplot(235), plt.imshow(bilateral_blur), plt.title('Bilateral Blurring')

plt.tight_layout()
plt.show()
