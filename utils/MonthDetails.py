# import matplotlib.pyplot as plt
import numpy as np

import utils.EmployeeManage as EmployeeManage 
import utils.ProductManage as ProductManage
import utils.SalesManage as SalesManage



class Month:

    def __init__(self,revenue,debt,haveEquity,EBITDA,assets,marketing,grossProfit,netProfit,totalSalaries,COGS,totalTaxes,other,employees,product,sales,shareMarket):
        self.revenue=revenue
        self.debt=debt
        self.haveEquity=haveEquity
        self.EBITDA=EBITDA     
        # self.annualRevenueRunRate=None
        self.assets=assets
        self.marketing=marketing
        self.grossProfit=grossProfit
        self.netProfit=netProfit
        self.totalSalaries=totalSalaries
        self.COGS=COGS    #cost of Goods Sold
        self.totalTaxes=totalTaxes
        self.other=other

        self.employees=employees
        self.product=product()
        self.sales=sales()
        self.shareMarket=shareMarket()
