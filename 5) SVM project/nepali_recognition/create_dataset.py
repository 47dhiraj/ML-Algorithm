import cv2,os                 # opencv lai import gareko                   
from sklearn.externals import joblib
import numpy as np
import csv                    # importing the csv module
import glob			          # yedi aafno directory lai iterate garnu cha vani glob lai import garera garda sajilo parcha

label = "क"                   # run this script for each label i.e label=0 ko laig 1 choti run garney, label=1 ko lagi 1 choti .. so on until label=9


f = open('csv/dataset.csv', mode='a', newline='', encoding="utf-8")    # by default windows ma python batw csv file ma write garda each row pachi blank row aaune garcha.. so, testo blank row na aaos vanna ko lagi newline='' gareko # csv file banauda csv file lai append mode ma kholeko (i.e 'a' vannale append mode) .. append ma khole pachi .. yedi hamilai palai palo script run garda same or autai csv file mai thapdai write gardai janu cha vanni append mode use garnu parcha.. i.e auta file ma add gardai jancha
writer = csv.writer(f)              # csv.writer() method le file ma write garna ko lai object create garne kaam garcha.. i.e writer chai auta csv file writer object ho


# For adding header to the csv file only while running this script for label=0 (i.e baaki aru label like label=1, label=2, label=3, label=4, ....... label=9 lai yo header lai csv file ma lekhni code comment garni beacuase we dont want our header to be written after each label.. only top ma ek choti header vaye matra pugcha so tesko lagi label=0 execute garne bela matra tyo uncomment garera run garne, baki aru bela chai comment garni)
# header = ["label"]
# for i in range(784):              # since hamro auta row ma 784 columns huncha(i.e because of 784 pixels) so teti samma loop chalako
# 	header.append("pixel_"+str(i))
# writer.writerow(header)             # csv file ma auta row lai write garcha



dirList = glob.glob("orig_images/"+label+"/*.png")     # For getting the list of all files & folders in the directory 
# print(dirList)


## Step 1 : Iterate Recursively through all folders and files in the orig_images folder
for img_path in dirList:
	# file_name = img_path.split("/")[2]        # For Mac 
	file_name = img_path.split('\\')[1]         # For Windows         
	# print(file_name)	

	im = cv2.imread(img_path)            # Read image file using opencv      # opencv ko imread() vanni method use gareko so that it reads image of any format

	im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	im_gray = cv2.GaussianBlur(im_gray, (15, 15), 0)

	roi = cv2.resize(im_gray, (28, 28), interpolation=cv2.INTER_AREA)       # Resizing the image to that particular dimension (width * height i.e = total pixel) , so that the total pixel in the image matches with the number of features in the dataset  (eg: 28*28 = 784pixel or 784 features)
    
	# Actually image aai rako cha ki nai vanera auta sano window ma display gareko
    # cv2.imshow("window",roi)
    # cv2.waitKey()
    # break

	data=[]               # creating an empty list
	data.append(label)    # list ma value add or append gareko 
	rows,cols = roi.shape # yedi image ko size kati cha vanera check garnu cha vani.. yesari garna sakincha # for us the size of image will be 28*28
   
	# print(rows)
	# print(cols)
	
	for i in range(rows):		#each row ko lagi for loop 
	    for j in range(cols):   # auta row ko each column ko lagi for loop
	        k = roi[i,j]
	        if k>100:
	        	k=1
	        else:
	        	k=0	

	        data.append(k)          # #Add pixel one-by-one into data list or array 
			


	writer.writerow(data)           # csv file ma auta row lai write garcha
	# cv2.imwrite("proc_images/0/"+file_name, roi)





