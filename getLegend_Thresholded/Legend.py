import matplotlib.pyplot as plt
import matplotlib.image as imp
import os

def getLegend(Image):
	if Image[-3:] != "jpg": return
	test_image=imp.imread("./"+Image)
	plt.axis('off')
	plt.plot([0], color="green")
	plt.plot([0], color="red")
	plt.plot([0], color="blue")

	plt.legend(["No Elevation (0-66)", "Moderate Elevation (67-120)", "High Elevation (121-255)"], loc ="upper right")

	plt.imshow(test_image)
	plt.savefig('./Result/'+Image)

os.chdir(os.getcwd()+'/getLegend_Thresholded/IMAGES')
L = os.listdir()

for x in L:
	getLegend(x)
