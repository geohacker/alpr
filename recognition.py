def recognition():
	from os import chdir,environ
	from tesseract import image_to_string
	from Image import open
	path = environ.get("HOME")
	im = open("blob.jpg")	
	text = image_to_string(im)
	chdir(path+"/alpr/latest/")
	return text
