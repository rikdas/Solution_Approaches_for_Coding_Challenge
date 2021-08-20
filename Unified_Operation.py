import os
import shutil

D = os.getcwd()

os.chdir(D+'/Raw Images/')

L = os.listdir()

for x in L:
	shutil.copy(os.getcwd()+'/'+x, D+'/getContour/Operation/'+x)

os.chdir(D)
print('Running Conturing')
os.system('python ./getContour/getContour.py') # getting thresholded contours

os.chdir(D+'/getContour/Operation/Result')

L = os.listdir()

for x in L:
	shutil.copy(os.getcwd()+'/'+x, D+'/getRelation/Thresholded Contours/'+x) # placing conturs in getRelation/Thresholded Contours
	shutil.copy(os.getcwd()+'/'+x, D+'/getKmean/IMAGE/'+x)
	shutil.copy(os.getcwd()+'/'+x, D+'/getLegend_Thresholded/IMAGES/'+x)


os.chdir(D)
print('Running K Means')
os.system('python ./getKmean/getKmeans.py') # getting K menas of the contours

os.chdir(D+'/getKmean/IMAGE/Result')

L = os.listdir()

for x in L:
	shutil.copy(os.getcwd()+'/'+x, D+'/getRelation/K Means/'+x) # placing K-means in getRelation/K Means
	shutil.copy(os.getcwd()+'/'+x, D+'/getLegend_KMeans/IMAGES/'+x)

os.chdir(D)
print("Running Correlation")
os.system('python ./getRelation/getRelation.py') # getting Correlation Coeff


print('Adding Legends')
os.chdir(D)
os.system('python ./getLegend_Thresholded/Legend.py') # adding Legends
os.chdir(D)
os.system('python ./getLegend_KMeans/Legend.py') # adding Legends


os.chdir(D) # placing output at OUTPUT folder
print('Creating Output')
os.chdir(D+'/getLegend_Thresholded/IMAGES/Result')
L = os.listdir()
for x in L:
	shutil.copy(os.getcwd()+'/'+x, D+'/OUTPUT/Thresholded/'+x) 
os.chdir(D)
os.chdir(D+'/getLegend_KMeans/IMAGES/Result')
L = os.listdir()
for x in L:
	shutil.copy(os.getcwd()+'/'+x, D+'/OUTPUT/K Means/'+x)
os.chdir(D)
# find the result at OUTPUT folder
