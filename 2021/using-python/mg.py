from __future__ import division
from sympy import Matrix


class MG:
    """matrix generator"""

    def __init__(self, n: list, k: int,
                 ignoriism: bool,
                 iism0: list, iism1: int, iism2: int
                 ) -> None:
        self.c = []
        self.nmassive = n
        self.n = len(self.nmassive)-1
        self.k = k
        self.ignoriism = ignoriism
        self.iism0 = iism0
        self.iism1 = iism1
        self.iism2 = iism2

    def generateMatrix(self, c: list, k, nmassiv: list, ignoriism, iism0, iism1, iism2) -> Matrix:

        mdata = []
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
                mrow = []  # matrix row symbols name list
                for i in range(1, k+1):
                    mrow.append(nmassiv[c[i]]+str(iism))
                    if i < k:
                        pass
                    else:
                        mdata.append(mrow)
                        mrow = []
            elif ignorthis:
                ignorthis = False
        m = Matrix(mdata)
        return m

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

        for i in range(1, k+1):
            self.c.append(i)
        inkrement = 1
        if (inkrement >= out1 and inkrement <= out2):
            matrices.append(
                self.generateMatrix(self.c, self.k, self.nmassiv,
                                    self.ignoriism,
                                    self.iism0, self.iism1, self.iism2)
            )

        while self.c[1] < self.n-self.k+1:
            i = self.k
            while self.c[i] + self.k - i + 1 > self.n:
                i -= 1
            self.c[i] += 1
            for j in range(i+1, self.k+1):
                self.c[j] = self.c[j-1]+1
            inkrement += 1
            if inkrement >= out1 and inkrement <= out2:
                matrices.append(
                    self.generateMatrix(self.c, self.k, self.nmassiv,
                                        self.ignoriism,
                                        self.iism0, self.iism1, self.iism2)
                )
        return matrices

    # def debugM()
