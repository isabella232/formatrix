from __future__ import division
from sympy import Matrix
from sg import SG


class MG:
    """matrix generator"""

    def __init__(self, n: list, k: int,
                 ignoriism: bool,
                 iism0: list, iism1: int, iism2: int
                 ) -> None:
        self.c = []
        self.nmassiv = n
        self.n = len(self.nmassiv)-1
        self.k = k
        self.ignoriism = ignoriism
        self.iism0 = iism0
        self.iism1 = iism1
        self.iism2 = iism2
        self.sg = SG(self.n, 1)

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def summcount(self):
        sumc = self.factorial(self.n) / self.factorial(self.k) / \
            self.factorial(self.n - self.k)
        print("original matrices number "+str(int(sumc)))
        return sumc

    def generateMatrix(self, c: list, k, nmassiv: list, ignoriism, iism0, iism1, iism2) -> list:

        mdata = []
        """number matrix data"""
        sdata = []
        """symbolic matrix data"""
        for iism in range(iism1, iism2+1):
            if ignoriism:
                ignorthis = False
                j = 0
                while j < len(iism0):
                    if iism == iism0[j]:
                        ignorthis = True
                        break
                    j += 1

            if not ignorthis:
                mrow = []  # matrix row number list
                srow = []  # matrix row symbols name list

                for i in range(1, k+1):
                    mSymbol = nmassiv[c[i]]+str(iism)
                    mrow.append(self.sg.sv[mSymbol])
                    srow.append(mSymbol)
                    if i < k:
                        pass
                    else:
                        mdata.append(mrow)
                        sdata.append(srow)
                        mrow = []
                        srow = []
            elif ignorthis:
                ignorthis = False
        m = Matrix(mdata)
        msym = Matrix(sdata)
        return [m, msym]

    def generateMatrices(self, n: list, k: int,
                         ignoriism: bool,
                         iism0: list, iism1: int, iism2: int,
                         out1: int, out2: int
                         ) -> list:
        self.c = [0]  # little cheat vs js early version
        self.nmassiv = n
        self.n = len(n)-1
        self.k = k
        self.ignoriism = ignoriism
        self.iism0 = iism0
        self.iism1 = iism1
        self.iism2 = iism2

        matrices = []
        """each element is [number, matrix, symbol matrix]"""

        for i in range(1, k+1):
            self.c.append(i)
        inkrement = 1
        if (inkrement >= out1 and inkrement <= out2):
            bothMatrix = self.generateMatrix(self.c, self.k, self.nmassiv,
                                             self.ignoriism,
                                             self.iism0, self.iism1, self.iism2)
            mxd = []
            mxd.append(inkrement)
            mxd.append(bothMatrix[0])
            mxd.append(bothMatrix[1])
            matrices.append(mxd)

        while self.c[1] < self.n-self.k+1:
            i = self.k
            while self.c[i] + self.k - i + 1 > self.n:
                i -= 1
            self.c[i] += 1
            for j in range(i+1, self.k+1):
                self.c[j] = self.c[j-1]+1
            inkrement += 1
            if inkrement >= out1 and inkrement <= out2:
                bothMatrix = self.generateMatrix(self.c, self.k, self.nmassiv,
                                                 self.ignoriism,
                                                 self.iism0, self.iism1, self.iism2)
                mxd = []
                mxd.append(inkrement)
                mxd.append(bothMatrix[0])
                mxd.append(bothMatrix[1])  # symbolic form matrix
                matrices.append(mxd)
        return matrices
