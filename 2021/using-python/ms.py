import sympy as s


class MS:
    """matrix solver"""

    def __init__(self) -> None:
        pass

    def pi_in_matrixDeterminant(self, d) -> bool:
        if "pi" in str(d):
            return True
        return False

    def solve_pi(self, m:s.Matrix, solution:list, debug=False) -> list:
        mdet = m.det()
        solution.append(None)

        if debug:
            print("debug mdet =\n",mdet)

        if self.pi_in_matrixDeterminant(mdet):
            solution = s.solve(mdet, s.pi, check=False, rational=None)
            # for i in rez: solution.append(i)
        else:
            solution.append(mdet)
            solution.pop(0)
