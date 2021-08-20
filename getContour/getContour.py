from PIL import Image, ImageOps
import numpy
import os

def getContour(IMAGE):
	if IMAGE == 'Result':return  # non technical purpose

	og_image = Image.open('./'+IMAGE) # opening image in RGB
	gray_image = ImageOps.grayscale(og_image) # opening image in Grayscale

	arr = numpy.array(gray_image) # converting gray scaled image into a numpy array
	arr2 = numpy.array(og_image) # converting RGB image into numpy array

	Thresholds = [66, 120] # thresholds specification

	for i in range(arr.shape[0]):
		if i%100 == 0 : print(".", end='') # non technical purpose

		for j in range(arr.shape[1]):

			if arr[i][j]<=Thresholds[0]:  # if pixel value in 2D gray image array is less then 66
				arr2[i][j][0]=arr2[i][j][1]=0 # turn the pixel in RGB image as Blue
				arr2[i][j][2]=255

			elif arr[i][j]<=Thresholds[1]: # else if pixel value in 2D gray image array is less then 120 
				arr2[i][j][0]=arr2[i][j][2]=0 # turn the pixel in RGB image as Green
				arr2[i][j][1]=255

			else:
				arr2[i][j][1]=arr2[i][j][2]=0 # else  
				arr2[i][j][0]=255 # turn the pixel in RGB image as Red
				
	data = Image.fromarray(arr2) # convert 3D array back to an Image
	data.save('./Result/'+IMAGE) # saveing the image
	print('')

os.chdir(os.getcwd()+"./getContour/Operation")
List = os.listdir()

for img in List:
	getContour(img)