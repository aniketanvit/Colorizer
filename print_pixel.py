from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import scipy as sp
import numpy as np
import csv
import math

def displayImage(image):
    plt.axis("off")
    plt.imshow(image)
    plt.show()

with open('output_image_rgb.csv') as csvfile:
    image = []
    reader = csv.reader(csvfile)
    reader_list = list(reader)
    row_count = sp.floor(sp.sqrt(len(reader_list)))
    ci = 0
    row_array = []
    for row in reader_list:
        print(row)
        if(ci == row_count):
            image.append(row_array)
            ci = 0
            row_array = []
        row_array.append([float(row[0]), float(row[1]), float(row[2])])
        ci += 1
    #image.append(row_array)
    # image = np.array(image)
    imageArr = np.uint8(image)
    displayImage(imageArr)

    #for row in reader:
    #    print(row)
    # print(row[0], row[1], row[2])

# imageArr = mpimg.imread("chihuahua.jpg")
# imageArr = np.uint8([[[255,0,0],[0,255,0],[0,0,255]],[[0,0,255],[255,0,0],[255,0,0]],[[0,0,255],[255,0,0],[0,255,0]]])
# print(imageArr)
# displayImage(imageArr)
