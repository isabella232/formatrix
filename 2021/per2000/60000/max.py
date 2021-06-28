import os
import sys
import datetime
import math

if getattr(sys, 'frozen', False):
    mydir = os.path.dirname(sys.executable)
elif __file__:
    mydir = os.path.dirname(os.path.abspath(__file__))

print("------------mydir------------")
print(mydir)
print("------------------------")


def findMax(filePath: str, whatNeed: str, maxVal: str):
    file = open(filePath, "r")
    lines = file.readlines()
    file.close()
    box = ""
    result = ""
    for line in lines:
        for point in whatNeed[len(result):]:
            box += point
            if len(result) < len(box) and box in line:
                result = box
        box = result
    return result


maxVal = ""
try:
    pis = str(math.pi)
    sep = os.sep
    for tail in ["1", "2", "3", "4", "5"]:
        outDir = mydir + sep + tail
        for file in os.listdir(outDir):
            if "output" in file:
                filePath = outDir + sep + file
                newVal = findMax(filePath, pis, maxVal)
                if len(newVal) > len(maxVal):
                    maxVal = newVal
except:
    print(sys.exc_info())
print("maxVal = "+maxVal)
input("done / enter to close")
