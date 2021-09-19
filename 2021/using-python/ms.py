import sympy as s


class MS:
    """matrix solver"""

    def __init__(self) -> None:
        pass

    def solve_pi(self, m) -> float:
        mdet = m.det()
        return s.solve(mdet, s.pi, check=False, rational=None)
