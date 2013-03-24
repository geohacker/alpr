#Module 2: Image preprocessing

def preproc(image):
    from opencv.cv import cvCreateMat,cvThreshold,CV_THRESH_OTSU
    rows = image.rows
    cols = image.cols
    typ = image.type
    binary_image = cvCreateMat(rows,cols,typ)
    cvThreshold(image, binary_image,128,255, CV_THRESH_OTSU)
    return binary_image

