import cv2
import os
import numpy as np

dataPath = 'D:\\LaSalle\Computer architecture\Project\Data' 
peopleList = os.listdir(dataPath)
print('List of users: ', peopleList)

labels = []
facesData = []
label = 0

for nameDir in peopleList:
	personPath = dataPath + '/' + nameDir
	print('Reading data')

	for fileName in os.listdir(personPath):
		print('User: ', nameDir + '/' + fileName)
		labels.append(label)
		facesData.append(cv2.imread(personPath+'/'+fileName,0))
		#image = cv2.imread(personPath+'/'+fileName,0)
		#cv2.imshow('image',image)
		#cv2.waitKey(10)
	label = label + 1

#print('labels= ',labels)
#print('Nmber of label 0: ',np.count_nonzero(np.array(labels)==0))
#print('Number of label 1: ',np.count_nonzero(np.array(labels)==1))

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

print("Training...")

face_recognizer.train(facesData, np.array(labels))
face_recognizer.write('modelLBPHFace.xml')

print("Model saved")