import matplotlib.pyplot as plt
import numpy as np

import Employees 
import Marketing
import Product
import Sales
import ShareMarket



class Month:

    def __init__(self):
        self.dept={"amount":None,"Total_EMI":None,"paidedEMI":None,"persentage":None}
        self.haveEquity=None
        self.EBITA=None
        self.annualRevenueRunRate=None
        self.assets=None
        self.marketing=None

        self.employees=Employees()
        self.product=Product()
        self.sales=Sales()
        self.shareMarket=ShareMarket()

        self.grossProfit=None
        self.netProfit=None
        self.totalSalaries=None
        self.COGS=None    #cost of Goods Sold
        self.totalTaxes=None
        self.other=None
