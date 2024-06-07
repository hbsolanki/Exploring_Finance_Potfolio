
from utils.Management.EmployeeManage import Employees 
from utils.Management.ProductManage import Products

from utils.Management.SalesManage import Sales
from utils.MonthDetails import Month
import Database.CRUD as db

from Visualisation.Business import viewChartForAnalysis,viewTableForAnalysis,generateFinanceMatrix

class Business:

    def owner(self):
        choice=None

        while choice!="3":
            print()
            choice=input("(1)View Chart For Analysis (2)View Table For Analysis (3)Generate Finance Matrix PDF (4)Change Some IMPORTANT Term (5)Exit \n")
            
            if choice=="1":
                viewChartForAnalysis()

            elif choice=="2":
                viewTableForAnalysis()

            elif choice=="3":
                generateFinanceMatrix() 

            elif choice=="4":
                self.changeIMPORTANTTerm()
            
            elif choice=="5":
                break

            else:
                print("Invalid Option")



    def changeIMPORTANTTerm(self):
        semch=""
        while semch!="6":
            print()
            semch=input("(1)Business id (2)Business Name (3)haveEquity (4)assets (5)Debt (6)Exit\n")

            if semch=="1":
                newId=int(input("Enter New Business Id : "))
                self.bid=newId
                db.updateBusinessID(self)

            elif semch=="2":
                newName=input("Enter New Name For Business : ")
                self.name=newName
                db.updateBusinessName(self)

            elif semch=="3":
                newEquity=int(input("Enter New Business Equity : "))
                self.haveEquity=newEquity
                db.updateBusinessEquity(self)

            elif semch=="4":
                newAssets=int(input("Enter New Value Of Assets : "))
                self.assets=newAssets
                db.updateBusinessAssets(self)

            elif semch=="5":
                amount=float(input("Enter Amount Of Debt : "))
                totalMonth=int(input("If EMI Then Enter Total Month : "))
                persentage=float(input("Enter Persentage : "))
                self.debt={"amount":amount,"Total_EMI":totalMonth,"paidedEMI":0,"persentage":persentage}
                db.updateBusinessDebt(self)

            elif semch=="6":
                break

            else:
                print("Invalid Option")
                




    def manager(self):
        print()
        choice=None
        print("For Management Enter Number : ")
        
        while choice!="4":

            print()
            choice=input("(1)Add Month Details \n(2)Employee Management \n(3)Product Management \n(4)View Sale Details \n(5)View Chart For Analysis \n(6)View Table For Analysis \n(7)Generate Finance Matrix PDF \n(8)Exit \n")

            if choice=="1":
                saleObj=Sales()
                revenue=saleObj.saleInput(self.productObjectForBusiness)
                print("Revenue :",revenue)
                COGS=saleObj.COGS
                print("COGS",COGS)
                grossProfit=revenue-COGS
                print("Gross Profit : ",grossProfit)
                
                debt=self.debt
                haveEquity=self.haveEquity
                assets=self.assets

                print()

                marketing=int(input("Enter Marketing Cost : "))
                depreciation=int(input("Enter Depreciation Cost : "))
                other=int(input("Enter Other Cost : "))

                totalSalaries=self.employeeObjectForBusiness.allEmployeeSalaryTotal()
                print("Total Salaries :",totalSalaries)
                afterEMIProfit=self.currentDebtCalculation(grossProfit)
                print("afterEMIProfit :",afterEMIProfit )
                IncomeBeforeTaxes=afterEMIProfit-marketing-depreciation-other-totalSalaries
                IncomeBeforeTaxes=afterEMIProfit-marketing-depreciation-other-totalSalaries
                print("IncomeBeforetaxes :",)

                totalTaxes=self.taxCalculation(IncomeBeforeTaxes)  
                print("Total Taxes : ",totalTaxes)
                
                netProfit=IncomeBeforeTaxes-totalTaxes  
                print("Net Profit : ",netProfit)
                self.profit=(netProfit*self.haveEquity)/100
                print("Profit : ",self.profit)
                EBITDA=netProfit+depreciation+totalTaxes
               

                shareMarket=None
                if self.debt["amount"] and debt["Total_EMI"]:
                    EBITDA+=debt["amount"]/debt["Total_EMI"]

                print("EBITDA :",EBITDA)
                m=Month(revenue,debt,haveEquity,EBITDA,assets,marketing,grossProfit,netProfit,totalSalaries,COGS,totalTaxes,other,saleObj,shareMarket)
                
                self.storeDetails(m)

                
            elif choice=="2":
                self.employeeObjectForBusiness.employeeManagement()
                db.updateBusinessEmployeeDetails(self)

            elif choice=="3":
                self.productObjectForBusiness.productManagement()
                db.updateBusinessProductDetails(self)

            elif choice=="4":
                self.viewSaleDetails()

            elif choice=="5":
                self.viewChartForAnalysis()

            elif choice=="6":
                self.viewTableForAnalysis()

            elif choice=="7":
                self.generateFinanceMatrix()


            elif choice=="8":
                break

            else:
                print("INVALID Option")    


    def storeDetails(self,m):
        self.currentYearMonths.append(m)
        self.profit=(m.netProfit*m.haveEquity)/100
        print("Profit :",self.profit)
        db.upateBusinessProfit(self)
        print("profit Updated")

        if len(self.currentYearMonths)==12:
            self.years.append(self.currentYearMonths)
            self.currentYearMonths.clear()
            db.updateBusinessYears(self)

        else:
            self.currentYearRevenue+=m.revenue
            self.annualRevenueRunRate=((self.currentYearRevenue/len(self.currentYearMonths))*12)
            db.updateBusinessCurrentYearMonth(self)


    def currentDebtCalculation(self,grossProfit):

        if self.debt["Total_EMI"]!=self.debt["paidedEMI"]:
            print(self.debt)
            emiPrice=self.debt["amount"]/self.debt["Total_EMI"]
            if emiPrice<grossProfit:
                afterEMIProfit=grossProfit-emiPrice
                self.debt={"amount":self.debt["amount"],"Total_EMI":self.debt["Total_EMI"],"paidedEMI":self.debt["paidedEMI"]+1,"persentage":self.debt["persentage"]}
                print(self.debt)
                db.updateBusinessDebt(self)
                return afterEMIProfit
            
            else:
                return grossProfit
        else:
            return grossProfit
        

    def taxCalculation(self,IncomeBeforeTaxes):
        #corporate Tax  30% <1cr || 1<Pro>10 37% || >10cr 42%
        if IncomeBeforeTaxes<=0:
            return 0
        
        if IncomeBeforeTaxes>100000000:
            return (IncomeBeforeTaxes*42)/100
        
        if IncomeBeforeTaxes<10000000 and IncomeBeforeTaxes<=100000000:
            return (IncomeBeforeTaxes*37)/100
        
        return (IncomeBeforeTaxes*30)/100

        
    def viewSaleDetails(self):
        choice=input("(1)Last Month (2)Current Year")

        if choice=="1":
            m=None
            if self.currentYearMonths:
                m=self.currentYearMonths[len(self.currentYearMonths)-1]

            elif self.years:
                m=self.years[len(self.years)-1][11]

            m.sales.viewSaleDetails()

        elif choice=="2":
            if self.currentYearMonths:
                for i in self.currentYearMonths:
                    i.sales.viewAllProductSale()
        
        
        else:
            print("invalid option try again...")