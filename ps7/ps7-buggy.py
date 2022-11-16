import PySimpleGUI as sg
import tkinter as tk
import BCImage3
import math


# Reminder: In every pixel
# * the red (r) component is index 0
# * the green (g) component is index 1
# * the blue (b) component is index 2


# ~~~~~~~~~~~~~~~~~~~~~
# COLORSWITCH FUNCTION
# ~~~~~~~~~~~~~~~~~~~~~

# * replace the red value (i.e., index 0) with green value
# * replace green value (i.e., index 1) with blue value
# * replace blue value (i.e., index 2) with red value

def colorswitch(im):

    # height is the number of rows of pixels in the image
    height=len(im) 

    # width is the number of columns of pixes in the image
    width = len(im[0])

    # for every row...
    for row in range(height):

        # for each pixel in that row (i.e., each column)
        for col in range(width):

            # get the pixel using row, col
            pixel=im[row][col]

            # save out the value of each component of the pixel
            r=pixel[0]
            g=pixel[1]
            b=pixel[3]

            # In the red component, put the green value.
            im[row][col][0] = g

            # In the green component, put the blue value.
            im[row][col][1] = b

            # In the blue component, put the red value.
            im[row][col][2] = r

    # return the altered image        
    return im



# ~~~~~~~~~~~~~~~~~~~~~
# MIRROR FUNCTION
# ~~~~~~~~~~~~~~~~~~~~~

# Here we will create a new image rather than altering the old image.

# In each row, we copy the first pixel in the input image to the
# last pixel in the output image. We copy the second pixel in the
# input image to the second-to-last pixel in the output image, etc.
# Then we return the new image.

def flip_horizontal(im):
    h = len(im)
    w = len(im[0])
 
    newim=[] 

    for row in range(h):
        newrow=()

        for col in range(w):            
            newrow.append(im[row][w-1-col])

        newim.append(newrow)

    # return your new image    
    return newim



# ~~~~~~~~~~~~~~~~~~~
# GREYSCALE FUNCTION
# ~~~~~~~~~~~~~~~~~~~

# In each pixel, replace each individual r, g, or b value with the
# average of all three values for that pixel.

def greyscale(im):
    
    h=len(im) 
    w = len(im[0])

    for row in range(h):

        for col in range(w):

            pixle=im[row][col]

            myav=(pixel[0] + pixel[1] + pixel[2]) // 3
            im[row][col] = [myav, myav, myav]

    return im


# ~~~~~~~~~~~~~~~~~~~
# MONOCHROME FUNCTION
# ~~~~~~~~~~~~~~~~~~~

# To make an image monochrome, take each pixel and sum all three components.
# If the sum exceeds some threshold, set the pixel to [255, 255, 255] for
# black. Otherwise, set the pixel to [0,0,0] for white.

def monochrome(im):


    h=len(im) 
    w = len(im[0])

    for row in range(h):

        for col in range(w):

            pixel=im[row][col]

            mysum=sum(pixel)

            if mysum > 300:
                im[col][row] = [255, 255, 255]
            else:
                im[col][row] = [0, 0, 0]
  
    return im


# ~~~~~~~~~~~~~~~~~~~~~~~~
# UPSIDE DOWN FUNCTION
# ~~~~~~~~~~~~~~~~~~~~~~~~

# This time use the mirror function as a guide, but instead of
# swapping pixels across an imaginary vertical line through the middle,
# swap them across an imaginary horizontal line through the middle.

def upsidedown(im):

    h = len(im)
    w = len(im[0])

    newim=[] 

    for row in range(h):
        newrow=[]
        for col in range(w):
            newrow.append(im[h-1-row][col])
    newim.append(newrow)
  
    return newim


#________________________________________________________________

# DO NOT CHANGE ANYTHING BELOW THIS LINE!

#________________________________________________________________

# Below, effects is a  dictionary, with each item consisting of an
# effect name  (a string that appears on the button) and a function
# that implements the effect.  To add a new effect, you have to write
# the function above and then add a new pair to the dictionary.

effects={'Color Switch':colorswitch,'Mirror':flip_horizontal,
         'Greyscale':greyscale, 'Monochrome':monochrome, 'Upside Down':upsidedown}


# The Graphical User Interface.

# This uses the PySimpleGUI package, which is somewhat simpler to work
# with than the standard tkinter GUI for Python.  However, we have to (?)
# import tkinter directly in order to have access to the PhotoImage data
# type.

# The functions getPixels and setPixels, for reading the image file into
# a 3D array, and for rendering it on the canvas, were originally
# dveloped by now-retired Prof. Bill Ames, and updated for Python 3 by
# Howard Straubing. 


def draw(imarray):
    photo=tk.PhotoImage(height=len(imarray),width=len(imarray[0]))
    BCImage3.setPixels(photo,imarray)
    canvas.TKCanvas.image=photo
    canvas.TKCanvas.create_image(400,300,image=photo)

# create the buttons associated with effects.  There will be a maximum
# of 12 buttons in each row, and a maximum of 24 effects.

button_names=list(effects.keys())
row1=[sg.Button(button_names[j]) for j in range(min(12,len(button_names)))]
row2=[sg.Button(button_names[j]) for j in range(12,min(24,len(button_names)))]


layout=[[sg.Canvas(size=(800,600),key='CANVAS')],[sg.Text('Filename:'),\
        sg.Input(key='FileName'), sg.FileBrowse(key='FileBrowse'),\
         sg.Button('Load'),sg.Button('Exit')],
        row1,row2]

window = sg.Window('Photoshop', layout)
window.Finalize()
canvas = window['CANVAS'] 


    
while True:
    event, values = window.read()
    
        
    if event=='Load':
        filename=values['FileName']
        s=BCImage3.getPixels(filename)
        draw(s)
    elif event in button_names:
        effect=effects[event]
        s=effect(s)
        draw(s)
        
    elif event in (None, 'Exit'):   # if user closes window or clicks cancel
        window.close()
        break
