#convert images to rgb and grayscale
import matplotlib.image as mpimg
import numpy as np
import re

imageArr = mpimg.imread("chihuahua.jpg")
imageArr1D = np.array(imageArr)

with open('output_image_rgb.csv', 'a') as the_file:
    for row in imageArr1D:
        for col in row:
            the_file.write(re.sub("\s+", ",", str(col).strip("[]").strip()))
            
