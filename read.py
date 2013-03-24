# Imports OpenCV libraries and Reads the Image
def read(name):
    from opencv.highgui import cvLoadImageM
    #Location of the image
    location = name
    image = cvLoadImageM(location,0)
    return image

