import numpy as np
# import matplotlib.pyplot as plt
from utils.EmployeeManage import Employees 
# import Marketing
from utils.ProductManage import Products
from utils.SalesManage import Sales
# import ShareMarket
from utils.MonthDetails import Month


class Business:
    def __init__(self,password,bid,name):
        self.password=password
        self.bid=bid
        self.name=name
        self.debt={"amount":None,"Total_EMI":None,"paidedEMI":None,"persentage":None}
        self.haveEquity=None
        self.assets=None
        self.currentYearMonths=[]
        self.years=[]
        self.profit=None
        self.annualRevenueRunRate=None
        self.currentYearRevenue=None
        
        self.product=Products()
        self.employee=Employees()


    def manager(self):
        choice=None
        print("For Management Enter Number : ")
        print("(1)Add Month Details \n(2)Employee \n(3)Product \n(4)Exit")
        choice=input()
        if choice=="1":
            saleObj=Sales()
            revenue=saleObj.saleInput(self.product)
            COGS=saleObj.COGS
            grossProfit=revenue-COGS
            
            debt=self.debt
            haveEquity=self.haveEquity
            assets=self.assets

            print()

            marketing=int(input("Enter Marketing Cost : "))
            depreciation=int(input("Enter Depreciation Cost : "))
            other=int(input("Enter Other Cost : "))
            totalSalaries=self.employee.allEmployeeSalaryTotal()
            afterEMIProfit=self.currentDebtCalculation(grossProfit)
            IncomeBeforeTaxes=afterEMIProfit-marketing-depreciation-afterEMIProfit-other
            totalTaxes=self.taxCalculation(IncomeBeforeTaxes)  #corporate Tax  30% <1cr || 1<Pro>10 37% || >10cr 42%
            netProfit=IncomeBeforeTaxes-totalTaxes

            self.profit=(netProfit*self.haveEquity)/100

            employeesObj=Employees()
            employeesObj.copyEmployee(self.employee)
            productObj=Products()
            productObj.copyProduct(self.product)
            shareMarket=None
            EBITDA=netProfit+totalTaxes+debt+depreciation

            m=Month(revenue,debt,haveEquity,EBITDA,assets,marketing,grossProfit,netProfit,totalSalaries,COGS,totalTaxes,other,employeesObj,productObj,saleObj,shareMarket)

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
        else:
            self.currentYearRevenue+=m.revenue
            self.annualRevenueRunRate=((self.currentYearRevenue/len(self.currentYearMonths))*12)
        



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
        choice=None
        while choice!="3":
            choice=input("(1)View Chart For Analysis (2)View Table For Analysis (3)Generate Finance Matrix PDF (4)Change Some IMPORTANT Term (5)Exit")
            
            if choice=="1":
                pass
            elif choice=="2":
                pass
            elif choice=="3":
                pass
            elif choice=="4":
                pass
            elif choice=="5":
                break
            else:
                print("Invalid Option")

    def generateAllDetailsFile(self):
        pass

    def chartsUnitEconomicsForLastMonth(self):
        
        if self.currentYearMonths:
            m=self.currentYearMonths[len(self.currentYearMonths)-1]

        else:
            m=self.years[len(self.years)-1][11]
        activities=["COGS","Commissions,Logistics Packaging & Other","Performance Marketing","Salaries & Rent","EBITDA"]
        revenue=m.revenue
        # self.debt={"amount":None,"Total_EMI":None,"paidedEMI":None,"persentage":None}
        logistics=0
        if self.debt["Total_EMI"]!=self.debt["paidedEMI"]:
            logistics=self.debt["amount"]//self.debt["Total_EMI"]
        slices=[(m.COGS*100)/revenue,((logistics+m.other)*100)/revenue,(m.marketing*100)/revenue,(m.totalSalaries*100)/revenue,(m.EBITDA*100)/revenue]
        color=['r','y','g','b','v']
        plt.pie(slices,labels=activities,colors=color,startangle=90,shadow=True,radius=1.2,autopct='%1.2f%%')
        plt.legend()
        plt.show()


    def chartsUnitEconomicsForAllMonth(self):
        pass

    def chartsUnitEconomicsForLastYear(self):
        pass

    def chartsUnitEconomicsForAllYear(self):
        pass
    

    # def pieChart(self,activities,slices,color):
    #     plt.pie(slices,labels=activities,colors=color,startangle=90,shadow=True,radius=1.2,autopct='%1.2f%%')
    #     plt.legend()
    #     plt.show()

