import sympy as s


class SG:
    """symbols generator

    R,S,P,PS,N,RN,O,C,OC,
    F,A,FA,AC,AS,ACAS,FAC,
    RR,SS,PP,PSPS,NN,RNRN,OO,CC,OCOC,
    FF,AA,FAFA,ACAC,ASAS,ACASACAS,FACFAC,

    NU,XU,XR,o,f,r,ac,as,Af,Rr,v
    NUNU,XUXU,XRXR,oo,ff,rr,acac,asas,AfAf,RrRr,vv

    linear values:
    R - radius of circle outside polygon, one for all.
    S - side of polygon
    P - perimeter of polygon
    PS - perimeter minus side
    N - normal (perpendicular) from side center to circle center
    RN - radius minus normal
    O - circle length
    C - circle arc length between two polygon vertex
    OC - full circle length minus C

    NU - normal from polygon side to circle center , to intersection with polygon oposite direction
    perimeter
    XU - sum of NU for each polygon side
    XR - sum of RN for each polygon side
    o - internal circle length

    Rr - R minus r, ring width
    v - "vertex -> center -> side" length

    squared values:
    F - full circle area
    A - area of polygon
    FA - full circle area minus polygon area
    AC - area of  circle sector
    AS - area of polygon sector
    ACAS - AC minus AS
    FAC - full circle area minus AC

    f - internal circle area
    r - ring area, F minus f
    ac - area of internal circle section
    as - area AS minus ac
    Af - area A minus f

    repeating is power of two

    """
    sv = dict()
    """symbol values"""
    R = s.Integer(1)
    O = 2 * s.pi * R
    F = s.pi * R ** 2
    RR = R * R
    OO = O * O
    FF = F * F

    def __init__(self, sn: list, R=1) -> None:
        self.sn = ["pi", "R", "S", "P", "PS", "N", "RN", "O", "C", "OC", "F", "A", "FA", "AC", "AS", "ACAS", "FAC", "RR", "SS", "PP", "PSPS", "NN", "RNRN", "OO", "CC", "OCOC", "FF", "AA", "FAFA",
                   "ACAC", "ASAS", "ACASACAS", "FACFAC", "NU", "XU", "XR", "o", "f", "r", "ac", "as", "Af", "Rr", "v", "NUNU", "XUXU", "XRXR", "oo", "ff", "rr", "acac", "asas", "AfAf", "RrRr", "vv"]
        """symbol names"""

        self.R = s.Rational(R)
        self.O = 2 * s.pi * self.R
        self.F = s.pi * self.R ** 2
        self.RR = self.R * self.R
        self.OO = self.O * self.O
        self.FF = self.F * self.F

        self.sv = {
            "R2": self.R, "R3": self.R, "R4": self.R, "R6": self.R, "R7": self.R,
            "O2": self.O, "O3": self.O, "O4": self.O, "O6": self.O, "O7": self.O,
            "F2": self.F, "F3": self.F, "F4": self.F, "F6": self.F, "F7": self.F,
            "RR2": self.RR, "RR3": self.RR, "RR4": self.RR, "RR6": self.RR, "RR7": self.RR,
            "OO2": self.OO, "OO3": self.OO, "OO4": self.OO, "OO6": self.OO, "OO7": self.OO,
            "FF2": self.FF, "FF3": self.FF, "FF4": self.FF, "FF6": self.FF, "FF7": self.FF
        }

        self.sv["S2"] = 2*self.R
        self.sv["P2"] = 4*self.R
        self.sv["PS2"] = self.sv["P2"]-self.sv["S2"]
        self.sv["N2"] = s.Rational(0)
        self.sv["RN2"] = self.sv["R2"]-self.sv["N2"]
        self.sv["C2"] = self.sv["O2"]/2
        self.sv["OC2"] = self.sv["O2"]-self.sv["C2"]
        self.sv["A2"] = s.Rational(0)
        self.sv["FA2"] = self.sv["F2"]-self.sv["A2"]
        self.sv["AC2"] = self.sv["F2"]/2
        self.sv["AS2"] = self.sv["A2"]/2
        self.sv["ACAS2"] = self.sv["AC2"]-self.sv["AS2"]
        self.sv["FAC2"] = self.sv["F2"]-self.sv["AC2"]
        self.sv["NU2"] = s.Rational(0)
        self.sv["XU2"] = s.Rational(0)
        self.sv["XR2"] = self.sv["RN2"]*2
        self.sv["o2"] = 2*s.pi*self.sv["N2"]
        self.sv["f2"] = s.pi*self.sv["N2"]**2
        self.sv["r2"] = self.sv["F2"]-self.sv["f2"]
        self.sv["ac2"] = self.sv["f2"]/2
        self.sv["as2"] = self.sv["AS2"]-self.sv["ac2"]
        self.sv["Af2"] = self.sv["A2"]-self.sv["f2"]
        self.sv["Rr2"] = self.sv["R2"]-self.sv["N2"]
        self.sv["v2"] = self.sv["R2"]*2

        self.sv["SS2"] = self.sv["S2"] ** 2
        self.sv["PP2"] = self.sv["P2"] ** 2
        self.sv["PSPS2"] = self.sv["PS2"] ** 2
        self.sv["NN2"] = self.sv["N2"] ** 2
        self.sv["RNRN2"] = self.sv["RN2"] ** 2
        self.sv["CC2"] = self.sv["C2"] ** 2
        self.sv["OCOC2"] = self.sv["OC2"] ** 2
        self.sv["AA2"] = self.sv["A2"] ** 2
        self.sv["FAFA2"] = self.sv["FA2"] ** 2
        self.sv["ACAC2"] = self.sv["AC2"] ** 2
        self.sv["ASAS2"] = self.sv["AS2"] ** 2
        self.sv["ACASACAS2"] = self.sv["ACAS2"] ** 2
        self.sv["FACFAC2"] = self.sv["FAC2"] ** 2
        self.sv["NUNU2"] = self.sv["NU2"] ** 2
        self.sv["XUXU2"] = self.sv["XU2"] ** 2
        self.sv["XRXR2"] = self.sv["XR2"] ** 2
        self.sv["oo2"] = self.sv["o2"] ** 2
        self.sv["ff2"] = self.sv["f2"] ** 2
        self.sv["rr2"] = self.sv["r2"] ** 2
        self.sv["acac2"] = self.sv["ac2"] ** 2
        self.sv["asas2"] = self.sv["as2"] ** 2
        self.sv["AfAf2"] = self.sv["Af2"] ** 2
        self.sv["RrRr2"] = self.sv["Rr2"] ** 2
        self.sv["vv2"] = self.sv["v2"] ** 2
