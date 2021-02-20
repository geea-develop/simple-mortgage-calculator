import numpy as np
import pandas as pd
from .loan import Loan

class Mortgage(object):
    """
        Mortgage.
    """

    def __init__(self, years, annual_interest_rate, amount, payment_type=0):
        super(Mortgage, self).__init__()
        self.annual_interest_rate = annual_interest_rate
        self.years = years
        self.amount = amount
        self.payments_per_year = 12
        self.payment_type = payment_type
        loan = Loan(self.years*self.payments_per_year, self.annual_interest_rate/self.payments_per_year, self.amount, 0, self.payment_type)
        self.loans = [loan]

    def amortisation_schedule(self, loan):
        df = pd.DataFrame({'Principal' :[ loan.PPMT(i+1) for i in range(self.payments_per_year*self.years)],
                                     'Interest' :[loan.IPMT(i+1) for i in range(self.payments_per_year*self.years)]})

        df['Instalment'] = df.Principal + df.Interest
        df['Balance'] = self.amount + np.cumsum(df.Principal)
        return(df)

# Credit to - https://www.listendata.com/2019/10/amortisation-schedule-r-python.html
