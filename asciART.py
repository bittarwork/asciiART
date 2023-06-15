# Imports PIL module 
from PIL import Image

# this asci caracter are the one that i'am going to use 
# @ is the daaedkest and . 
ASCII_CHARS = [ "." , "."  , ":",  ";", "+", "*", "?",  "%",  "$",  "#",  "@" ]
# [ " " , "."  , ":",  ";", "+", "*", "?",  "%",  "$",  "#",  "@", ]
#  ["@", "#", "$", "%", "?", "*", "+", ";", ":", "." , " "]

# open and resize 
def openIMAGE(path): 
    # open the image 
    newWidth = 50
    img = Image.open(path) 
    # taking width and height 
    width, height = img.size
    # ratio
    ratio = (height / width) * 0.5
    newHeight = int (newWidth * ratio)

    # resize 
    return img.resize((newWidth, newHeight))


def toGray (img) : 
    return img.convert("L")

# gray scale into asci code for each oixel : 
def pixel_to_ascii(image):
    pixels = image.getdata()
    asciiSTR = ""
    for pixel in pixels:
        asciiSTR += ASCII_CHARS[pixel//25]
    return asciiSTR
# save art 
def saving (asciiART) : 
    #save the string to a file
    with open("asciiART.txt", "w") as f:
        f.write(asciiART)

# main 
if __name__ == "__main__" : 
    try:
        path = input ("enter path")
        img = openIMAGE(path)
    except:
        print( "Unable to find image ")
    #convert image to greyscale image
    imgTogray = toGray (img)
    # convert greyscale image to ascii characters
    asciiSTR = pixel_to_ascii(imgTogray)
    # imgTograyWidth to print it right in console 
    imgTograyWidth = imgTogray.width
    asciiStrLen = len(asciiSTR)
    ascii_img=""
    #Split the string based on width  of the image
    for i in range(0, asciiStrLen, imgTograyWidth):
        ascii_img += asciiSTR[i:i+imgTograyWidth] + "\n"
    print (ascii_img)
    #save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)
    
