"""
Background Remover
==================
Function to remove white backgrounds from silhouette pictures

- Saves files as .png
- Can be modified to remove black or white backgrounds
- Can also be modified to remove picture and leave white background
- Created by tlee753
- Last Modified 2/10/16
- Version 8.0
"""

from PIL import Image
from numpy import array
# import required methods from libraries

def backRem ():
    inputFile = raw_input("Please type file name string without quotations. \n")
    # asks user to input file name
    
    try:
        image = Image.open(inputFile)
        image = image.convert('RGBA')
        # opens image and converts to Red, Green, Blue, Alpha interpretation
        
        data = array(image)
        # converts the image into four interconnected arrays of RGBA values ranging from 0 to 255
        
        [red, green, blue, alpha] = data.T
        # splits the four layers of the array into separate single layered arrays
        
        try:
            redValue = raw_input
        
        
        
        whiteMask = (red >= 240) & (green >= 240) & (blue >= 240) & (alpha >= 240)
        data[whiteMask.T] = (0, 0, 0, 0)
        # creates a mask for white pixels and alters the pixel to be transparent if it is white
        
        image = Image.fromarray(data)
        # converts four interconnected arrays back into image interpretation
        
        outputFile = inputFile[0:len(inputFile)-4] + "_edited.png"
        image.save(outputFile)
        # creates a new file name based on the input and saves the edited image under that name
        
        print ("Conversion Complete")
        # prints confirmation of successful conversion for user
        
    except:
        print ("Unable to load file. Please check to make sure file exists and is spelled correctly.")

    
backRem()
# function call