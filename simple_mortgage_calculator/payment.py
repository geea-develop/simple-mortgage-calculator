
class Payment(object):
    """
        Payment.
    """

    def __init__(self, interest, principal, date=None):
        super(Payment, self).__init__()
        self.interest = interest
        self.principal = principal
        self.date = date

    def due_date(self):
        return self.date

    def due_amount(self):
        return self.interest + self.principal

    def due_interest_amount(self):
        return self.interest

    def due_principal_amount(self):
        return self.principal
