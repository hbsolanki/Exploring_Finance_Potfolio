from Management.Product import Product
from Management.Employee import Employee
from Management.Sale import Sale

class Business:

    def __init__(self,password,bid,name):
        self.password=password
        self.bid=bid
        self.name=name
        self.debt={"amount":0,"Total_EMI":0,"paidedEMI":0,"persentage":0}
        self.haveEquity=0
        self.assets=0
        self.currentYearMonths=[]
        self.years=[]
        self.profit=0   #Last Month Profit
        self.annualRevenueRunRate=0
        self.currentYearRevenue=0
        self.productObjectForBusiness=Product()
        self.employeeObjectForBusiness=Employee()