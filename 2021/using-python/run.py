from mg import MG

"""trying calculate all in one flow without preparing every partion of matrices"""


class MGAS:
    """matrix generator and solver"""

    def __init__(self) -> None:
        # names of parameters. first element empty(old code recoding result)
        self.input_n = ["", "R", "S", "P", "PS", "N", "RN", "O", "C", "OC", "F", "A", "FA", "AC", "AS", "ACAS", "FAC", "RR", "SS", "PP", "PSPS", "NN", "RNRN", "OO", "CC", "OCOC", "FF", "AA", "FAFA",
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
        self.out1 = 1
        # generate matrices to 3
        self.out2 = 3

        self.mg = MG(
            self.input_n,
            self.k,
            self.ignoriism,
            self.iism0,
            self.iism1,
            self.iism2
        )

    def runAll(self):
        print("test")
        print(self)
        print(self.input_n)
        print(self.mg.generateMatrices(
            self.input_n, self.k, self.ignoriism, self.iism0, self.iism1, self.iism2, self.out1, self.out2
        ))
        input("enter to close")


mbox = MGAS()
mbox.runAll()
