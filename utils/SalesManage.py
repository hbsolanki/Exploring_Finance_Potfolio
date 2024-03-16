import numpy as np
import utils.ProductManage as pdct

class Sales:

    class Sale:
        def __init__(self,pid,name,cost,revenue,quantity):
            self.pid=pid
            self.name=name
            self.cost=cost
            self.revenue=revenue
            self.quantity=quantity

    # currentMonthDaySale=np.empty([31], dtype=object)
    # currentYearMonthSale=np.empty([12], dtype=object)
    # yearlySale=[]
    listOfProductsSale=[]
    totalRevenue=0
    COGS=0

    def productSaleAdd(self,pid,name,cost,revenue,noOfProductSale):
        self.listOfProductsSale.append(self.Sale(pid,name,cost,revenue,noOfProductSale))

    def saleInput(self,pdct): 
        allProductDetails=pdct.allProduct
        listOfProductsSale=[]
        for i in allProductDetails:
            
            noOfProductSale=int(input(str(i.pid)+" " +i.name+" quantity sale : "))
            listOfProductsSale.append(self.Sale(i.pid,i.name,i.cost,i.revenue,noOfProductSale))
            # print(i.revenue)
            self.totalRevenue+=(noOfProductSale*i.revenue)
            self.COGS+=(noOfProductSale*(i.cost-i.revenue))

        return self.totalRevenue
        
    