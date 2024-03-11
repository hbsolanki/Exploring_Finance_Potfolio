import numpy as np
import matplotlib.pyplot as plt
import Employees 
import Marketing
import Product
import Sales
import ShareMarket

class Business:
    def __init__(self,bid,name):
        self.bid=bid
        self.name=name
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

    class Marketing:
        pass

    def generateAllDetailsFile(self):
        pass

    def chartsUnitEconomicsForLastMonth(self):
        pass

    def chartsUnitEconomicsForAllMonth(self):
        pass

    def chartsUnitEconomicsForLastYear(self):
        pass

    def chartsUnitEconomicsForAllYear(self):
        pass
    