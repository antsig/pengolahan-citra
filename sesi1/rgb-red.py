#pip install numpy
import numpy as np
import imageio  as img
import matplotlib.pyplot as plt

image = img.imread("https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png")

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

imgRed = np.zeros_like(image)
imgRed[:,:,0] = red

imgGreen = np.zeros_like(image)
imgGreen[:,:,1] = green

imgBlue = np.zeros_like(image)
imgBlue[:,:,2] = blue

plt.figure(figsize=(10,10))
plt.subplot(4,1,1)
plt.imshow(image)

plt.subplot(4,1,2)
plt.imshow(imgRed)

plt.subplot(4,1,3)
plt.imshow(imgGreen)

plt.subplot(4,1,4)
plt.imshow(imgBlue)

plt.show()