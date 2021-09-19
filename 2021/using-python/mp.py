import os


class MP:
    """matrix printer"""

    def __init__(self) -> None:
        pass

    def printMatrix(self, m, solution):
        print("----"+str(m[0]))  # matrix number
        print(m[2])  # symbolic matrix
        print(solution)

    def printToFile(self, m, solution):
        """print result to file with matrix index"""

    def globalCounterValue(self) -> int:
        os.listdir()
