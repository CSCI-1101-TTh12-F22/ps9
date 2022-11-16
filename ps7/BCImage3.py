# BCImage
# Get 2D list of pixels, indexed by [row][col].
# Each element is a list [red, green, blue]
# (So, it's really 3D ...)

import os
try:
    from PIL import Image
except:
    print("You will only be able to work with .ppm files.")


#This reads the 3D array into a tkinter PhotoImage object, which has to be
#created prior to  the call to setPixels
def setPixels(photo, pixels):
    """Set each pixel of the photo from the colors in the pixels 3D list"""
    data = ' '.join(['{'+' '.join(["#%02x%02x%02x" % tuple(pixels[row][col]) for col in range(len(pixels[0]))])+'}' for row in range(len(pixels))])
    photo.put(data)

##This reads a ppm image file into the 3D array.  Everything up until the last line
#consists of skipping the comments and header.
    
def getPixels(filename):
    if filename[-3:] in ['jpg','JPG']:
        im=Image.open(filename)
        filename=filename[:-3]+'ppm'
        im.save(filename)
        
 
    f = open(filename,'rb')
    f.readline()
    c = f.read(1)
    while c==b'#':
        f.readline()
        c = f.read(1)
    dim = (c+f.readline()).strip().split()
    w = int(dim[0])
    h = int(dim[1])
    f.readline()
    s = f.read()
    #print (len(s))

    pix = [[[s[i*3*w+j*3+k] for k in range(3) ] for j in range(w)] for i in range(h)]
    #Note change for Python 3, we no longer use ord because s can no longer be treated
    #as a Python string
    
    return pix
              
