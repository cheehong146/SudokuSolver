import cv2
import os


class ImageParser:
    @staticmethod
    def isJpgExtension(fileName):
        if fileName[-4:] == ".jpg":
            return True
        else:
            return False
    
imageFolder = "v2_train"

rootDir = os.getcwd()
imageFolderDir = os.listdir(imageFolder + "/")
datasetImage = []

with os.scandir(imageFolder + "/") as entries:
    for entry in entries:
        fileName = entry.name
        if ImageParser.isJpgExtension(fileName):
            imgDir = imageFolder + "/" + fileName
            imgData = cv2.imread(imgDir, 0)
            datasetImage.append(imgData)

print(datasetImage)            
            
