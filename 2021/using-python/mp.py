import os


class MP:
    """matrix printer"""

    def __init__(self, mydir, k) -> None:
        self.mydir = mydir
        self.resultDir = self.mydir + os.sep + "resultFolder"+str(k)+"x"+str(k)
        self.resultSubDir = self.resultDir + os.sep + "result"

    def printMatrix(self, m, solution):
        print("----"+str(m[0]))  # matrix number
        print(m[2])  # symbolic matrix
        print(solution)

    def printToFile(self, solutionBox):
        """print result to file with matrix index"""
        # last calculated matrix index in this group
        fileName = str(solutionBox[-1][0])+".txt"
        rfDir = self.resultSubDir + os.sep + fileName
        resultFile = open(rfDir, mode="wt", encoding="utf-8")
        slines = []
        for one in solutionBox:
            sline = str(one[0])+"  "+str(one[-1])+"\n"
            slines.append(sline)
        resultFile.writelines(slines)
        resultFile.close()

        # refresh globalCounterValue
        gcfDir = self.resultDir + os.sep + "globalCounter.txt"
        gcv = str(solutionBox[-1][0])
        gcFile = open(gcfDir, mode="wt", encoding="utf-8")
        gcFile.write(gcv)
        gcFile.close()

        print("printed "+str(solutionBox[0][0])+" "+str(solutionBox[-1][0]))

    def globalCounterValue(self) -> int:
        gcv = 0
        gcfDir = self.resultDir + os.sep + "globalCounter.txt"

        # check if no previous completed inkrement of calculated matrices
        if not os.path.exists(self.resultDir):
            os.makedirs(self.resultDir)
        if not os.path.exists(self.resultSubDir):
            os.makedirs(self.resultSubDir)

        if not os.path.exists(gcfDir):
            gcFile = open(gcfDir, mode="wt", encoding="utf-8")
            gcFile.write("0")
            gcFile.close()

        gcFile = open(gcfDir, mode="rt", encoding="utf-8")
        gcv = int(gcFile.readline())
        gcFile.close()
        print("mp.py calculated "+str(gcv))
        return gcv
