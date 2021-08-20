from PIL import Image, ImageOps
import numpy
import os

mainRel = 0
mainNum = 0

def getRelation(x, y):
	global mainRel
	global mainNum

	A = Image.open('./Thresholded Contours/'+x)
	A = ImageOps.grayscale(A)

	B = Image.open('./K Means/'+y)
	B = ImageOps.grayscale(B)

	M = numpy.array(A)
	N = numpy.array(B)

	corCoeff = numpy.corrcoef(M.reshape(M.size),N.reshape(N.size))[0][1]
	mainRel += corCoeff
	mainNum += 1

DIR = os.getcwd()

os.chdir(DIR+'./getRelation/Thresholded Contours')
List1 = os.listdir()

os.chdir(DIR+'./getRelation/K Means')
List2 = os.listdir()

os.chdir(DIR+'./getRelation')

for x in range(len(List1)):
	getRelation(List1[x], List2[x])

print('Correlation Coeff :', mainRel/mainNum)