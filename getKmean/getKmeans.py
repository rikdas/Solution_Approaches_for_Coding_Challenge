from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
 
def kMeans(ImageA):
	if ImageA[-3:] != "jpg": return

	image = cv2.imread(ImageA)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	pixel_vals = image.reshape((-1,3))
	pixel_vals = np.float32(pixel_vals)
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
	k = 3
	retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
	centers = np.uint8(centers)
	segmented_data = centers[labels.flatten()]
	segmented_image = segmented_data.reshape((image.shape))
	plt.imshow(segmented_image)
	#plt.show()
	x = np.array(segmented_image)
	im = Image.fromarray(x)
	im.save('./Result/'+ImageA)


os.chdir(os.getcwd()+'./getKmean/IMAGE')
L = os.listdir()
for x in L:
	kMeans(x)
