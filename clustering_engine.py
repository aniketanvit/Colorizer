import csv
import math
import sys

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
                with open(self.outputFileName.split(".")[0] + "_reduced.csv", "a+") as reducedOutputFile:
                    input_csv = csv.reader(inputImage,  delimiter=',')
                    output_csv = csv.reader (reducedOutputFile, delimiter=',')

                    for color in input_csv:
                        ic = [int(color[0]), int(color[1]), int(color[2])]
                        xx = self.getNearestColor(ic)
                        xy = str(xx[0]) + "," + str(xx[1]) + "," + str(xx[2]) + "\n"
                        print(xy)
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

    def clusterInputSpace(self):
        pass

    def normDiff(self, vec1, vec2):
        n1 = len(vec1)
        n2 = len(vec2)
        assert (n1 == n2)
        diff = 0

        for i in range(0, n1):
            diff += int(math.fabs(vec1[i] - vec2[i]))

        return diff

if __name__ =='__main__':
    ce = ClusteringEngine()
    #ce.convertHexFileToRGB()
    #ce.loadOutputClusterHeads()
    #ce.getNearestColor([2,2,3])
    ce.clusterOutputSpace("color.csv")