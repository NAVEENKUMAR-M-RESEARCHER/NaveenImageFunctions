# Developer : M NAVEENKUMAR, a Research Scholar, Department of Computer Applications, NIT Trichy, Tamilnadu, India


import numpy as np



#img and kernel both dimensions should be 3 x 3.
def naveenConvolve3(img,kernel):
    row1total = img[0,1]*kernel[0,1] + img[0,2]*kernel[0,2] + img[0,0]*kernel[0,0]
    row2total = 0
    row3total = img[2,1]*kernel[2,1] + img[2,2]*kernel[2,2] + img[2,0]*kernel[2,0]
    return row1total + row2total + row3total

#this function returns the 3 x 3 sub image from (i,j)
def naveenTakePartImage3(inpimg,i,j):
    image = np.zeros((3,3))
    # print(i,j)
    a = i
    b = j
    for k in range(0,3):
        b = j
        for l in range(0,3):
            #print(a,b)
            image[k,l] = inpimg[a,b]
            b = b+1
        a = a +1
    # print(image)
    return image

# This function returns the sobel X gradient image
def naveenSobelXgradient(inputimg):
    rows = len(inputimg)
    cols = len(inputimg[0])
    #print(rows,cols)
    Gx = np.array(np.mat('1 0 -1; 2 0 -2; 1 0 -1'))
    outputimg = np.zeros((rows,cols))
    for i in range(0,rows-3):
         for j in range(0,cols-3):
             image  = naveenTakePartImage3 (inputimg, i, j)
             outputimg[i,j] = naveenConvolve3(image,Gx)
    return outputimg

# This function returns the sobel Y gradient image
def naveenSobelYgradient(inputimg):
    rows = len(inputimg)
    cols = len(inputimg[0])
    #print(rows,cols)
    Gy = np.array(np.mat('1 2 1; 0 0 0; -1 -2 -1'))
    outputimg = np.zeros((rows,cols))
    for i in range(0,rows-3):
         for j in range(0,cols-3):
             #print('hai')
             # retreve the part of image of 3 x 3 dimension from inputimage
             #print(i,j)
             image  = naveenTakePartImage3 (inputimg, i, j)
             #print(image)
             outputimg[i,j] = naveenConvolve3(image,Gy)
    return outputimg

