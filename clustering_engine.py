import csv
import math
import sys
import numpy as np

class ClusteringEngine:

    def __init__(self):
        self.outputFileName = 'color.csv'
        self.outputClusterHeadFile = 'output_color_clusterhead.csv'
        self.rgbClusterHead = []
        self.loadOutputClusterHeads ()


    def loadOutputClusterHeads (self):
        r = 0
        g = 0
        b = 0
        with open(self.outputClusterHeadFile, 'r') as clusterHeadFile:
            csvreader = csv.reader (clusterHeadFile, delimiter=',')
            for row in csvreader:
                r = int(row[0])
                g = int(row[1])
                b = int(row[2])
                self.rgbClusterHead.append([r, g, b])


    def convertHexFileToRGB(self):
        try:
            with open("color_categories.csv", "r") as ipf:
                with open ("output_color_clusterhead.csv", "w") as opf:
                    input_csv = csv.reader (ipf, delimiter=',')
                    output_csv = csv.writer(opf, delimiter=',')
                    for color in input_csv:
                        for c in color:
                            cr = self.convertHexToRGB([c])
                            output_csv.writerow(cr[0])
        except Exception as e:
            pass

    def clusterOutputSpace(self, inputFileName):
        try:
            mindiff = sys.maxsize
            with open(inputFileName, "r") as inputImage:
                with open(inputFileName.split(".")[0] + "_reduced.csv", "w") as reducedOutputFile:
                    input_csv = csv.reader(inputImage,  delimiter=',')
                    output_csv = csv.reader (reducedOutputFile, delimiter=',')

                    for color in input_csv:
                        ic = [int(color[0]), int(color[1]), int(color[2])]
                        xx = self.getNearestColor(ic)
                        xy = str(xx[0]) + "," + str(xx[1]) + "," + str(xx[2]) + "\n"
                        reducedOutputFile.write(xy)
        except Exception as e:
            pass

    def getNearestColor(self, color):
        assert (len(color) == 3)
        nearestColor = color
        minDiff = int(sys.maxsize)
        for c in self.rgbClusterHead:
            c_diff = self.normDiff(c, color)
            if(c_diff < minDiff):
                minDiff = c_diff
                nearestColor = c

        return nearestColor

    def convertHexToRGB(self, row):
        #row = ['#D19FE8', '#88540B', '#A52A2A']
        converted_rgb = []
        for x in row:
            h = x.lstrip ('#')
            converted_rgb.append (tuple (int (h[i:i + 2], 16) for i in (0, 2, 4)))
        return converted_rgb

    def clusterInputSpace(self, inputFileName):
        try:
            with open(inputFileName, "r") as inputImage:
                with open(inputFileName.split(".")[0] + "_reduced.csv", "w") as reducedOutputFile:
                    input_csv = csv.reader(inputImage,  delimiter=',')
                    output_csv = csv.writer(reducedOutputFile, delimiter=',')
                    values = []
                    for line in inputImage:
                        v = line.rstrip("\n")
                        val = int(float(v))
                        rv = self.getReducedGrayscale(val)
                        output_csv.writerow([rv])
        except Exception as e:
            pass

    def clusterInputSpace_training(self, inputFileName):
        try:
            with open(inputFileName, "r") as inputImage:
                with open(inputFileName.split(".")[0] + "_reduced.csv", "w") as reducedOutputFile:
                    input_csv = csv.reader(inputImage,  delimiter=',')
                    output_csv = csv.writer(reducedOutputFile, delimiter=',')

                    for line in input_csv:
                        print(line)
                        old_val = []
                        for v in line:
                            old_val.append(int(self.getReducedGrayscale(v)))
                        output_csv.writerow(old_val)
        except Exception as e:
            pass

    def getReducedGrayscale(self, _val):

        val = int(_val)
        clusterRange = 10
        assert (val >= 0)
        assert (val <= 255)

        for i in range(0, 11):
            l = val - i
            r = val + i
            if((l % clusterRange) == 0):
                return l
            elif((r % clusterRange) == 0):
                return r

    def normDiff(self, vec1, vec2):
        n1 = len(vec1)
        n2 = len(vec2)
        assert (n1 == n2)
        diff = 0

        for i in range(0, n1):
            diff += int(math.fabs(vec1[i] - vec2[i]))

        return diff

    def CreateInputClusterFile(self):
        with open("grayscale_categories.csv", "w+") as grayscale:
            output_csv = csv.writer(grayscale, delimiter=',')
            for i in range(0, 260, 5):
                output_csv.writerow([i])
                print(i)

if __name__ =='__main__':
    ce = ClusteringEngine()
    #ce.convertHexFileToRGB()
    #ce.loadOutputClusterHeads()
    #ce.getNearestColor([2,2,3])
    ce.clusterInputSpace("output_image_grayscale.csv")
    #ce.clusterOutputSpace("color.csv")