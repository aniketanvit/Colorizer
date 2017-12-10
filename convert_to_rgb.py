#convert images to rgb and grayscale
import matplotlib.image as mpimg
import numpy as np
import re
import image_utils as graySc

imageArr = mpimg.imread("chihuahua.jpg")
imageArr1D = np.array(imageArr)

rowCount = 0
colCount = 0
with open('output_image_rgb.csv', 'a') as the_file:
    for row in imageArr1D:
        rowCount += 1
        for col in row:
            colCount += 1
            arr = ''
            for i in col:
                arr += str(i) + ','
            # the_file.write(re.sub("\s+", ",", str(col).strip("[]").strip()))
            the_file.write(arr.rstrip(',') + '\n')

print('row: ' + str(rowCount))
print('col: ' + str(colCount))
print('Image converted to RGB')

grayscaleImage = graySc.ImageUtility()
grayscaleImage.convertToGrayScale('./output_image_rgb.csv')
print('Image converted to Grayscale')
