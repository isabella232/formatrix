import sympy as s


class MS:
    """matrix solver"""

    def __init__(self) -> None:
        pass

    def pi_in_matrixDeterminant(self, d) -> bool:
        if "pi" in str(d):
            return True
        return False

    def solve_pi(self, m, debug=False) -> list:
        mdet = m.det()

        if debug:
            print("mdet =\n",mdet)
            print("check=True will used for solve for debug")
            # return s.solve(mdet, s.pi, check=True, rational=None)
            return s.solve(mdet, s.pi)
            #not work, still infinity/long process


        if self.pi_in_matrixDeterminant(mdet):
            return s.solve(mdet, s.pi, check=False, rational=None)
        # if no pi inside det then return det as solution, packed in list
        return [mdet]
