from mg import MG
from ms import MS
from mp import MP

import time
import sys
import os

if getattr(sys, 'frozen', False):
    mydir = os.path.dirname(sys.executable)
elif __file__:
    mydir = os.path.dirname(os.path.abspath(__file__))

"""trying calculate all in one flow without preparing every partion of matrices"""


class MGAS:
    """matrix generator and solver"""

    def __init__(self, mydir) -> None:
        self.mydir = mydir
        """run.py script file path"""
        # names of parameters. first element target(old code recoding result) is will pi
        self.input_n = ["pi", "R", "S", "P", "PS", "N", "RN", "O", "C", "OC", "F", "A", "FA", "AC", "AS", "ACAS", "FAC", "RR", "SS", "PP", "PSPS", "NN", "RNRN", "OO", "CC", "OCOC", "FF", "AA", "FAFA",
                        "ACAC", "ASAS", "ACASACAS", "FACFAC", "NU", "XU", "XR", "o", "f", "r", "ac", "as", "Af", "Rr", "v", "NUNU", "XUXU", "XRXR", "oo", "ff", "rr", "acac", "asas", "AfAf", "RrRr", "vv"]

        self.k = 5  # matrix size it should be square
        # turn on ignore some number indices from parameters flow f.e.: n1 n2 n4
        self.ignoriism = True
        # which number/s of parameters indices will ignored
        self.iism0 = [5]

        # generated parameter indices from 2
        self.iism1 = 2
        # generated parameter indices to 7
        self.iism2 = 7

        # generate matrices from 1
        self.out1 = 55
        # generate matrices to 3
        self.out2 = 57

        self.mg = MG(
            self.input_n,
            self.k,
            self.ignoriism,
            self.iism0,
            self.iism1,
            self.iism2
        )
        self.globalLimit = self.mg.summcount()

        self.ms = MS()
        self.mp = MP(self.mydir, self.k)
        self.calcSize = 1
        """how much matrices will calculated before time sleep, must be < saveSize"""
        self.saveSize = 5
        """how much matrices will calculated before save to file"""
        self.sessionSize = 0
        """how much calculated at present moment and not printed"""
        self.globalCounter = self.mp.globalCounterValue()

    def runAll(self):

        solutionBox = []
        saveChecker = 0
        self.globalCounter += 1
        calcChecker = self.globalCounter
        self.out1 = self.globalCounter
        self.out2 = self.globalCounter + self.calcSize - 1
        # calculation with pause between steps
        while calcChecker <= self.globalLimit:
            time.sleep(1)

            try:
                mx = self.mg.generateMatrices(
                    self.input_n, self.k, self.ignoriism, self.iism0, self.iism1, self.iism2, self.out1, self.out2
                )

                for m in mx:
                    solution = self.ms.solve_pi(m[1])
                    solutionBox.append([*m, solution])
                    saveChecker += 1
                    calcChecker += 1
                    if saveChecker >= self.saveSize or calcChecker == self.globalLimit:
                        self.mp.printToFile(solutionBox)
                        solutionBox = []
                        saveChecker = 0

            except:
                print(sys.exc_info())
                print("some fail with matrices " +
                      str(self.out1)+" "+str(self.out2)+" range")

            if calcChecker == self.globalLimit:
                break
            elif self.globalCounter + self.calcSize > self.globalLimit:
                self.calcSize = self.globalLimit - self.globalCounter

            self.globalCounter += self.calcSize
            self.out1 = self.globalCounter
            self.out2 = self.globalCounter + self.calcSize - 1

        input("enter to close")


mbox = MGAS(mydir)
mbox.runAll()
