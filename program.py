import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import math

image=cv2.imread("d42teMo.jpeg")
print(image.size)
im_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
im_gray=cv2.GaussianBlur(im_gray,(7,7),1.5)
im_canny=cv2.Canny(im_gray, 0, 50)
lines = cv2.HoughLinesP(im_canny,1,np.pi/180,120, np.array([]), minLineLength = 280, maxLineGap = 150)
x0=[]
y0=[]
x1=[]
y1=[]
filt_x=80
filt_y=10
a,b,c = lines.shape
for i in range(a):
    cv2.line(image, (lines[i][0][0], lines[i][0][1]),(lines[i][0][2], lines[i][0][3]), (0, 255, 255),3, cv2.LINE_AA)
print(a,b,c)
for i in range(a):
    print(i,lines[i][0][0], lines[i][0][1],lines[i][0][2], lines[i][0][3])
for i in range(a):
    #print(lines[i][0][0], lines[i][0][1],lines[i][0][2], lines[i][0][3])
    k=0
    for j in range(a):
        if i!=j:
            #Proverka na nalozhenie liniy
            if abs(lines[i][0][0]-lines[j][0][0])<filt_x and abs(lines[i][0][1]-lines[j][0][1])<filt_y\
               and abs(lines[i][0][2]-lines[j][0][2])<filt_x and abs(lines[i][0][3]-lines[j][0][3])<filt_y:
                len_l1=math.sqrt((lines[i][0][0]-lines[i][0][2])**2+(lines[i][0][1]-lines[i][0][3])**2)
                len_l2=math.sqrt((lines[j][0][0]-lines[j][0][2])**2+(lines[j][0][1]-lines[j][0][3])**2)
                if len_l1>len_l2: #Ostavlyaem bolee dlinnuyu liniyu
                    lines[j][0][0]=0
                    lines[j][0][1]=0
                    lines[j][0][2]=0
                    lines[j][0][3]=0
                if len_l2>len_l1:
                    lines[i][0][0]=0
                    lines[i][0][1]=0
                    lines[i][0][2]=0
                    lines[i][0][3]=0
                #print("________false",i,j)
            if abs(lines[i][0][0]-lines[j][0][0])<filt_y and abs(lines[i][0][1]-lines[j][0][1])<filt_x\
               and abs(lines[i][0][2]-lines[j][0][2])<filt_y and abs(lines[i][0][3]-lines[j][0][3])<filt_x:
                len_l1=math.sqrt((lines[i][0][0]-lines[i][0][2])**2+(lines[i][0][1]-lines[i][0][3])**2)
                len_l2=math.sqrt((lines[j][0][0]-lines[j][0][2])**2+(lines[j][0][1]-lines[j][0][3])**2)
                if len_l1>len_l2:
                    lines[j][0][0]=0
                    lines[j][0][1]=0
                    lines[j][0][2]=0
                    lines[j][0][3]=0
                if len_l2>len_l1:
                    lines[i][0][0]=0
                    lines[i][0][1]=0
                    lines[i][0][2]=0
                    lines[i][0][3]=0
    
    if lines[i][0][0]==0 and lines[i][0][1]==0 and lines[i][0][2]==0 and lines[i][0][3]==0:
        print (i)
        continue
    x0.append(lines[i][0][0])
    y0.append(lines[i][0][1])
    x1.append(lines[i][0][2])
    y1.append(lines[i][0][3])
for i in range(len(x0)):
    cv2.line(image, (x0[i],y0[i]),(x1[i],y1[i]), (0, 0, 255),3, cv2.LINE_AA)
    print(i,(x0[i],y0[i]),(x1[i],y1[i]))
cv2.imshow("detected lines", image)


