import csv

class ImageUtility:
    def __init__(self):
        self.outFileName = 'output.csv'

    def convertToGrayScale(self, inputFile):
        r = 0
        g = 0
        b = 0
        with open(inputFile, 'r') as inputImage:
            with open(self.outFileName, 'w') as grayImage:
                csvreader = csv.reader (inputImage, delimiter=',')
                csv_writer = csv.writer(grayImage,  delimiter=',')
                for row in csvreader:
                    r = int(row[0])
                    g = int(row[1])
                    b = int(row[2])
                    gray_value = ((0.21*r) + (0.72*g) + (0.07*b))
                    print(gray_value)
                    csv_writer.writerow([gray_value])


if __name__ == '__main__':
    iu = ImageUtility()
    iu.convertToGrayScale('./test.csv')
