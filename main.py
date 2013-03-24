from opencv.highgui import *

def main(i):
	from read import read
	from preproc import preproc
	from blob_identification import blob_identification
	from recognition import recognition
	from os import popen,mkdir,environ
	
	path = environ.get("HOME")
	popen("rm -rf blobs")
	mkdir("blobs")
	name=path+"/alpr/latest/images/"+str(i)+".jpg"	
	print name
	image=read(name)
	binary_image=preproc(image)
	blob_identification(binary_image)
	number = recognition()
	return number
