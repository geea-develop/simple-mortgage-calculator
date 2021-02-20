from .payment import Payment

class Loan(object):
    """
        Loan.
    """

    # rate - intrest rate per month
    # nper - number of payments for loan.
    # pv - loan amount
    # fv - future value after the full loan is repaid
    # type -
    #   0 means payments are due at the end of the period.
    #   1 means payments are due at the beginning of the period.
    #

    def __init__(self, nper, rate, pv, fv=0, type=0):
        super(Loan, self).__init__()
        self.nper = nper
        self.rate = rate
        self.pv = pv
        self.type = type
        self.fv = 0
        self.pmt = self.PMT()

    def payment(self, per):
        """
            Payment,
        """
        interest = self.IPMT(per)
        principal = self.PPMT(per)
        return Payment(interest, principal)

    def PMT(self):
        """
            PMT - Monthly instalment
            PMT = (rate*(fv+pv*(1+ rate)^nper))/((1+rate*type)*(1-(1+ rate)^nper))
        """
        if self.rate!=0:
                   pmt = (self.rate*(self.fv+self.pv*(1+ self.rate)**self.nper))/((1+self.rate*self.type)*(1-(1+ self.rate)**self.nper))
        else:
                   pmt = (-1*(self.fv+self.pv)/self.nper)
        return(pmt)

    def PAF(self):
        """
            PAF - Present Annuity Factor
        """
        return self.pmt

    def IPMT(self, per):
        """
            IPMT - Interest portion of monthly instalment
            IPMT = -( ((1+rate)^(per-1)) * (pv*rate + PMT(rate, nper,pv, fv=0, type=0)) - PMT(rate, nper,pv, fv=0, type=0))
            per - nth period. 2 means calculating interest of second instalment.
        """
        ipmt = -( ((1+self.rate)**(per-1)) * (self.pv*self.rate + self.pmt) - self.pmt)
        return(ipmt)

    def PPMT(self, per):
        """
            PPMT - Principal portion of instalment
            PPMT = PMT(rate, nper,pv, fv=0, type=0) - IPMT(rate, per, nper, pv, fv=0, type=0)
            per - nth period. 2 means calculating interest of second instalment.
        """
        ppmt = self.pmt - self.IPMT(per)
        return(ppmt)
