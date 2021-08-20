from DE import DE
from Dependencies import printResult, plotResult, printConvergence, appendResult
import random
import numpy
import math
import time
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

'''
og_image = Image.open("./ReSized.jpg")
gray_image = ImageOps.grayscale(og_image)

ARR = numpy.array(og_image)
BRR = list(ARR.reshape([ARR.size]))

PROBABLITY = []
for x in range(256):
    print(x)
    PROBABLITY.append(BRR.count(x)) 
print(PROBABLITY)
'''

PROBABLITY=[0.00392156862745098, 0.0, 0.01568627450980392, 0.00392156862745098, 0.0, 0.01568627450980392, 0.011764705882352941, 0.03137254901960784, 0.0196078431372549, 0.027450980392156862, 0.03529411764705882, 0.0196078431372549, 0.050980392156862744, 0.058823529411764705, 0.09411764705882353, 0.0784313725490196, 0.11372549019607843, 0.13333333333333333, 0.1411764705882353, 0.1450980392156863, 0.2235294117647059, 0.3058823529411765, 0.3176470588235294, 0.3568627450980392, 0.4235294117647059, 0.6, 0.6588235294117647, 0.8352941176470589, 0.996078431372549, 0.9176470588235294, 1.1764705882352942, 1.4, 1.588235294117647, 1.9333333333333333, 2.1215686274509804, 2.4352941176470586, 2.5019607843137255, 3.196078431372549, 3.3058823529411763, 3.8901960784313725, 4.196078431372549, 4.490196078431373, 4.580392156862745, 5.184313725490196, 5.090196078431372, 5.588235294117647, 5.925490196078432, 6.298039215686274, 6.768627450980392, 7.6156862745098035, 8.235294117647058, 8.513725490196078, 8.929411764705883, 9.207843137254901, 10.047058823529412, 9.874509803921569, 10.470588235294118, 10.16470588235294, 10.313725490196079, 10.474509803921569, 10.023529411764706, 9.968627450980392, 9.384313725490196, 9.07843137254902, 8.91764705882353, 9.050980392156863, 8.176470588235293, 8.68235294117647, 7.776470588235294, 7.988235294117647, 7.768627450980392, 8.20392156862745, 7.592156862745098, 7.87843137254902, 8.133333333333333, 7.564705882352941, 7.8, 7.792156862745098, 7.647058823529412, 7.776470588235294, 7.415686274509804, 7.180392156862745, 7.152941176470589, 7.090196078431372, 6.874509803921568, 6.584313725490196, 6.898039215686275, 7.03921568627451, 6.882352941176471, 6.819607843137255, 6.886274509803922, 7.050980392156863, 6.984313725490196, 7.1647058823529415, 7.423529411764706, 7.701960784313726, 7.333333333333333, 7.372549019607843, 7.63921568627451, 7.396078431372549, 7.1568627450980395, 7.737254901960784, 7.509803921568627, 7.690196078431373, 7.298039215686274, 7.207843137254902, 6.776470588235294, 6.584313725490196, 6.572549019607843, 6.592156862745098, 6.411764705882353, 6.172549019607843, 6.070588235294117, 5.866666666666666, 5.956862745098039, 5.4941176470588236, 5.443137254901961, 5.392156862745098, 5.086274509803921, 5.050980392156863, 4.984313725490196, 5.0, 4.643137254901961, 4.474509803921569, 4.333333333333333, 4.243137254901961, 4.431372549019608, 4.184313725490196, 4.211764705882353, 3.8901960784313725, 3.6941176470588237, 3.627450980392157, 3.635294117647059, 3.4980392156862745, 3.443137254901961, 3.3019607843137253, 3.015686274509804, 2.9725490196078432, 2.768627450980392, 2.5254901960784313, 2.372549019607843, 2.3176470588235296, 2.180392156862745, 2.015686274509804, 1.8901960784313725, 2.066666666666667, 1.815686274509804, 1.8392156862745097, 1.7098039215686274, 1.7333333333333334, 1.576470588235294, 1.6313725490196078, 1.615686274509804, 1.2980392156862746, 1.3098039215686275, 1.219607843137255, 1.1058823529411765, 0.9921568627450981, 0.8627450980392157, 0.7333333333333333, 0.6862745098039216, 0.7137254901960784, 0.7490196078431373, 0.6, 0.6313725490196078, 0.4745098039215686, 0.44313725490196076, 0.3411764705882353, 0.37254901960784315, 0.2549019607843137, 0.20784313725490197, 0.12549019607843137, 0.10588235294117647, 0.058823529411764705, 0.023529411764705882, 0.01568627450980392, 0.0, 0.00784313725490196, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


OutputNormVar=(256**3)

def Entropy_Yen_5(thr):
    global OutputNormVar
    thr.sort()
    P=[]
    P.append(sum(PROBABLITY[:int(thr[0])]))
    P.append(sum(PROBABLITY[int(thr[0]):int(thr[1])]))
    P.append(sum(PROBABLITY[int(thr[1]):int(thr[2])]))
    P.append(sum(PROBABLITY[int(thr[2]):int(thr[3])]))
    P.append(sum(PROBABLITY[int(thr[3]):int(thr[4])]))
    P.append(sum(PROBABLITY[int(thr[4]):]))
    if(0 in P):
        return OutputNormVar-0
    p=[0,0,0,0,0,0]
    for i in range(int(thr[0])):
        p[0]+=(PROBABLITY[i]/P[0])**2
    for i in range(int(thr[0]),int(thr[1])):
        p[1]+=(PROBABLITY[i]/P[1])**2
    for i in range(int(thr[1]),int(thr[2])):
        p[2]+=(PROBABLITY[i]/P[2])**2
    for i in range(int(thr[2]),int(thr[3])):
        p[3]+=(PROBABLITY[i]/P[3])**2
    for i in range(int(thr[3]),int(thr[4])):
        p[4]+=(PROBABLITY[i]/P[4])**2
    for i in range(int(thr[4]),int(len(PROBABLITY))):
        p[5]+=(PROBABLITY[i]/P[5])**2
    if(0 in p):
        return OutputNormVar-0
    H=0
    for i in range(len(p)):
        H+=-1*math.log(p[i])
    return OutputNormVar-H


LoopCount = 30

# The Parameters --------------------------------------------------------------

LowerBound = 0
UpperBound = 255
Dimension  = 5
Population = 100
Generation = 100 
FitnessFunction = Entropy_Yen_5

# Multiple Execution ----------------------------------------------------------

AlgorithmLIST = [DE]

for algo in AlgorithmLIST:
    SOLUTION_LIST = []
    for i in range(LoopCount):
        print(i, end=' : ') 
        SOLUTION_LIST.append(algo(FitnessFunction, LowerBound, UpperBound, Dimension, Population, Generation))
    
    SOLUTION_LIST.sort(key=(lambda x : round(x.best,4)))
    
    printResult(SOLUTION_LIST[0])
    #printConvergence(SOLUTION_LIST[0])
    #plotResult(SOLUTION_LIST[0])  


# Obtained Thresholds : [37.29, 66.256, 92.285, 118.233, 143.379]