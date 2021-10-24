import sympy as s


class MS:
    """matrix solver"""

    def __init__(self) -> None:
        pass

    def pi_in_matrixDeterminant(self, d) -> bool:
        if "pi" in str(d):
            return True
        return False

    def solve_pi(self, m) -> list:
        mdet = m.det()
        if self.pi_in_matrixDeterminant(mdet):
            return s.solve(mdet, s.pi, check=False, rational=None)
        # if no pi inside det then return det as solution, packed in list
        return [mdet]
