# Imports Blob libraries,identifies blobs and Resizes into 20X20

def blob_identification(binary_image):
	from opencv.highgui import cvSaveImage,cvLoadImageM
	from opencv.cv import cvCreateImage,cvGetSize,cvCreateMat,cvSet,CV_RGB,cvResize
	from Blob import CBlob
	from BlobResult import CBlobResult
	from classification import classification
        from os import chdir,environ
	path = environ.get("HOME")
	frame_size = cvGetSize (binary_image) 
	blo = cvCreateImage(frame_size, 8, 1)
	resblo=cvCreateMat(240,320,binary_image.type)	
	mask = cvCreateImage (frame_size, 8, 1)
	cvSet(mask, 255)
	myblobs = CBlobResult(binary_image, mask, 0, True)
	myblobs.filter_blobs(325,2000)
	blob_count = myblobs.GetNumBlobs()
	count=0
	pixr=[]
	pixrm=[]
	for i in range(blob_count):
		value=[]
		rowval=[]
		colval=[]
		cvSet(blo,0)
		my_enum_blob = myblobs.GetBlob(i)
		my_enum_blob.FillBlob(blo,CV_RGB(255,0,255),0,0)
		cvSet(resblo,0)
		cvResize(blo,resblo,1)
		for rowitem in range(resblo.rows):
		    for colitem in range(resblo.cols):
		       if resblo[rowitem,colitem]!=0:
		          rowval.append(rowitem)
		    	  colval.append(colitem)
		    	  value.append(resblo[rowitem,colitem])                      
		pixr.append(rowval[0])
		pixrm.append(rowval[-1])
		rowmin=min(rowval)
		rowedit=[]
		for item in rowval:
		    rowedit.append(item-rowmin)
	
		coledit=[]
		colmin=min(colval)
		for item in colval:
		    coledit.append(int(item)-colmin)
	
		rowmax=max(rowedit)
		colmax=max(colval)-colmin
		moved=cvCreateMat(rowmax+10,colmax+10,blo.type)
		cvSet(moved,0)
		
		for i in range(len(rowval)):
		    moved[int(rowedit[i])+5,int(coledit[i])+5]=int(value[i])
		chdir(path+"/alpr/latest/blobs")
		cvSaveImage("pic"+ str(count)+".png",moved)
                count+=1
	avoid=classification(pixr,pixrm)
	blob_image = cvCreateImage(frame_size, 8, 1)
	cvSet(blob_image,0)
	for i in range(blob_count):
		if i not in avoid:
			my_enum_blob = myblobs.GetBlob(i)
			my_enum_blob.FillBlob(blob_image,CV_RGB(255,0,255),0,0)
			cvSaveImage("blob.jpg",blob_image)
	return
        
	
