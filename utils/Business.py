import numpy as np
import matplotlib.pyplot as plt
import Employees 
import Marketing
import Product
import Sales
import ShareMarket
from utils.MonthDetails import Month

class Business:
    def __init__(self,bid,name):
        self.bid=bid
        self.name=name
        self.currentYearMonths=[]
        self.years=[]
        self.debt={"amount":None,"Total_EMI":None,"paidedEMI":None,"persentage":None}
        self.haveEquity=None
        # self.EBITA=None
        self.annualRevenueRunRate=None
        self.assets=None
        # self.marketing=None
        # self.employees=Employees()
        self.product=Product()
        self.employee=Employees()
        # self.sales=Sales()
        # self.shareMarket=ShareMarket()

    class Marketing:
        pass

    def manager(self):
        
        
        choice=None
        print("For Management Enter Number : ")
        print("(1)Add Month Details \n(2)Employee \n(3)Product \n(4)Exit")
        choice=input()
        if choice=="1":
            saleObj=Sales()
            # self.
            revenue=saleObj.saleInput(self.product)
            COGS=saleObj.COGS
            grossProfit=revenue-COGS
            
            debt=self.debt
            haveEquity=self.haveEquity
            assets=self.assets
            print()
            # marketingASK=input({"Are You "})
            marketing=int(input("Enter Marketing Cost : "))
            depreciation=int(input("Enter Depreciation Cost : "))
            other=int(input("Enter Other Cost : "))
            totalSalaries=self.employee.allEmployeeSalaryTotal()
            afterEMIProfit=self.currentDebtCalculation(grossProfit)
            IncomeBeforeTaxes=afterEMIProfit-marketing-depreciation-afterEMIProfit-other
            totalTaxes=self.taxCalculation(IncomeBeforeTaxes)  #corporate Tax  30% <1cr || 1<Pro>10 37% || >10cr 42%
            netProfit=IncomeBeforeTaxes-totalTaxes
            employeesObj=Employees()
            employeesObj.copyEmployee(self.employee)
            productObj=Product()
            productObj.copyProduct(self.product)
            # sales=None
            shareMarket=None
            EBITA=netProfit+totalTaxes+debt+depreciation
    # def __init__(self,revenue,debt,haveEquity,EBITA,assets,marketing,grossProfit,netProfit,totalSalaries,COGS,totalTaxes,other,employees,product,sales,shareMarket):

            m=Month(revenue,debt,haveEquity,EBITA,assets,marketing,grossProfit,netProfit,totalSalaries,COGS,totalTaxes,other,employeesObj,productObj,saleObj,shareMarket)

            self.storeDetails(m)
            
        elif choice=="2":
            self.employee.employeeManagement()
        elif choice=="3":
            self.product.productManagement()
        else:
            print("INVALID Option")


    def storeDetails(self,m):
        self.currentYearMonths.append(m)
        if len(self.currentYearMonths)==12:
            self.years.append(self.currentYearMonths)
            self.currentYearMonths.clear()



    def currentDebtCalculation(self,grossProfit):
        # self.dept={"amount":None,"Total_EMI":None,"paidedEMI":None,"persentage":None}
        if self.debt["Total_EMI"]!=self.debt["paidedEMI"]:
            emiPrice=self.debt["amount"]/self.debt["Total_EMI"]
            if emiPrice<grossProfit:
                afterEMIProfit=grossProfit-emiPrice
                self.debt={"amount":self.debt["amount"],"Total_EMI":self.debt["Total_EMI"],"paidedEMI":self.debt["paidedEMI"]+1,"persentage":self.debt["persentage"]}
                return afterEMIProfit
            else:
                return grossProfit
        else:
            return grossProfit

    def taxCalculation(self,IncomeBeforeTaxes):
        #corporate Tax  30% <1cr || 1<Pro>10 37% || >10cr 42%
        if IncomeBeforeTaxes>100000000:
            return (IncomeBeforeTaxes*42)/100
        if IncomeBeforeTaxes<10000000 and IncomeBeforeTaxes<=100000000:
            return (IncomeBeforeTaxes*37)/100
        
        return (IncomeBeforeTaxes*30)/100

    def main(self):
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
    
