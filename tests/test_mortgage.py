import pytest

from .context import simple_mortgage_calculator, ROOT
from simple_mortgage_calculator import *

def test_pmt():
    loan = Loan(12*6, 0.085/12, 50000)
    pmt = loan.pmt
    print(pmt)
    assert pmt == -888.9192307634946

def test_ipmt():
    loan = Loan(12*6, 0.085/12, 50000)
    ipmt = loan.IPMT(1)
    # print(ipmt)
    assert ipmt == -354.16666666666674

def test_ppmt():
    loan = Loan(12*6, 0.085/12, 50000)
    ppmt = loan.PPMT(1)
    # print(ppmt)
    assert ppmt == -534.7525640968279

def test_paf():
    loan = Loan(12, 0.12/12, 1000)
    paf = loan.PAF()
    # print(paf)
    assert paf == -88.84878867834166

def test_schedule():
    mortgage = Mortgage(6, 0.085, 50000)
    loans = mortgage.loans
    df = mortgage.amortisation_schedule(loans[0])
    print(df)
