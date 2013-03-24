def classification(pixr,pixrm):
	from os import walk,remove,environ
	from opencv.highgui import cvLoadImageM
	path = environ.get("HOME")
	lrow=[]
	lcol=[]
	avoided=[]
	file_count = len(walk(path+"/alpr/latest/blobs").next()[2])
	for i in range(0,file_count):
		filename="pic"+str(i)+".png"
		img=cvLoadImageM(filename)
		lrow.append(img.rows)
		lcol.append(img.cols)
	lenr=(len(lrow)/2)
		
	mean_row=lrow[lenr]
	mean_col=lcol[lenr]
	for item in range(0,len(lrow)):
		if abs(lrow[item]-mean_row)>7:
			remove("pic"+str(item)+".png")
			lcol[item]='x'			
			avoided.append(item)
	for item in range(0,len(lcol)):
		if lcol[item]=='x':
			break
		else:
			if abs(lcol[item]-mean_col)>7:
				remove("pic"+str(item)+".png")
				avoided.append(item)

	val=(len(pixr)/2)-1
	mpixr=pixr[val]
	mpixrm=pixrm[val]
	amin=[]
	for i in range(0,len(pixr)):
		if abs(mpixr-pixr[i])>32:
			avoided.append(i)
			
	amax=[]
	for i in range(0,len(pixr)):
		if abs(mpixrm-pixrm[i])>50:
			avoided.append(i)	
	return(avoided)			

				
			
		
	
