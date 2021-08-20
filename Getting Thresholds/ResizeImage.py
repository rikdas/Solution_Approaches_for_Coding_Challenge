import cv2
import os

def RESIZE(Image):
	if Image == 'Result':
		return
	img = cv2.imread('./'+Image, cv2.IMREAD_UNCHANGED)
	 
	scale_percent = 60 # percent of original size
	width = 250
	height = 250
	dim = (width, height)
	  
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	 
	print('Resized Dimensions : ',resized.shape)

	cv2.imwrite("./Result/"+Image, resized)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

os.chdir(os.getcwd()+'/images/')
List = os.listdir()
i = 1
for x in List:
	print(i)
	i+=1
	RESIZE(x)