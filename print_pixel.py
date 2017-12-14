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

#281
#174
def readColorImage(fileName, row_count = 0):
    with open(fileName, "r") as csvfile:
        image = []
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        if(row_count == 0):
            row_count =  sp.floor(sp.sqrt(len(reader_list)))
        ci = 0
        row_array = []
        for row in reader_list:
            row_array.append([float(row[0]), float(row[1]), float(row[2])])
            ci += 1
            if(ci == row_count):
                image.append(row_array)
                ci = 0
                row_array = []
        imageArr = np.uint8(image)
        ROWS = len(image)
        COLS = len(image[0])
        print(ROWS)
        print(COLS)
        displayImage(imageArr)

def readGrayscaleImage(fileName, row_count = 0):
    with open(fileName, "r") as csvfile:
        image = []
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        if(row_count == 0):
            row_count =  sp.floor(sp.sqrt(len(reader_list)))
        ci = 0
        row_array = []
        for row in reader_list:
            row_array.append([float(row[0]), float(row[0]), float(row[0])])
            ci += 1
            if(ci == row_count):
                image.append(row_array)
                ci = 0
                row_array = []
        imageArr = np.uint8(image)
        displayImage(imageArr)

def createModelInputFile(fileName, row_count=0):
    with open(fileName, "r") as csvfile:
        image = []
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        if row_count == 0:
            row_count = sp.floor(sp.sqrt(len(reader_list)))
        ci = 0
        row_array = []
        for row in reader_list:
            row_array.append([float(row[0]), float(row[0]), float(row[0])])
            ci += 1
            if(ci == row_count):
                image.append(row_array)
                ci = 0
                row_array = []

    with open(fileName.split(".")[0] + "_modelInput.csv", "w") as op:
        op_csv = csv.writer(op, delimiter = ',')
        ROWS = len(image)
        COLS = len(image[0])
        print(ROWS)
        print(COLS)
        for i in range(0, ROWS):
            for j in range (0, COLS):
                g_row = []

                for ii in range(-1, 2, 1):
                    for jj in range(-1, 2, 1):

                        if(i+ii < 0 or i+ii > ROWS-1 or j+jj < 0 or j+jj > COLS-1):
                            g_row.append(int(image[i][j][0]))
                        # elif(j == 0 and i != 0):
                        #     g_row = [imageArr[i-1][j-1][0], imageArr[i-1][j][0], imageArr[i-1][j+1][0],
                        #              imageArr[i][j - 1][0], imageArr[i - 1][j][0], imageArr[i - 1][j + 1][0],
                        #              imageArr[i + 1][j - 1][0], imageArr[i + 1][j][0], imageArr[i + 1][j + 1][0]]
                        # elif(i == ROWS-1 and j != COLS-1):
                        #     g_row = [imageArr[i-1][j-1][0], imageArr[i-1][j][0], imageArr[i-1][j+1][0],
                        #              imageArr[i][j - 1][0], imageArr[i - 1][j][0], imageArr[i - 1][j + 1][0],
                        #              imageArr[i + 1][j - 1][0], imageArr[i + 1][j][0], imageArr[i + 1][j + 1][0]]
                        # elif(j == COLS-1 and i != ROWS-1):
                        #     g_row = [imageArr[i-1][j-1][0], imageArr[i-1][j][0], imageArr[i-1][j+1][0],
                        #              imageArr[i][j - 1][0], imageArr[i - 1][j][0], imageArr[i - 1][j + 1][0],
                        #              imageArr[i + 1][j - 1][0], imageArr[i + 1][j][0], imageArr[i + 1][j + 1][0]]
                        else:
                            g_row.append (int(image[i+ii][j+jj][0]))

                op_csv.writerow(g_row)

if __name__ == '__main__':
    #readColorImage("output_image_rgb_reduced.csv")
    #readGrayscaleImage ("output_image_grayscale_reduced.csv")
    #for row in reader:
    #    print(row)
    # print(row[0], row[1], row[2])

# imageArr = mpimg.imread("chihuahua.jpg")
# imageArr = np.uint8([[[255,0,0],[0,255,0],[0,0,255]],[[0,0,255],[255,0,0],[255,0,0]],[[0,0,255],[255,0,0],[0,255,0]]])
# print(imageArr)
# displayImage(imageArr)
    createModelInputFile("output_image_grayscale_reduced.csv", 400)
