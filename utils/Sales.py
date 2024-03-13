import numpy as np
import Product as pdct

class Sales:

    class Sale:
        def __init__(self,name,cost,revenue,quantity):
            self.name=name
            self.cost=cost
            self.revenue=revenue
            self.quantity=quantity

    # currentMonthDaySale=np.empty([31], dtype=object)
    # currentYearMonthSale=np.empty([12], dtype=object)
    # yearlySale=[]
    listOfProductsSale=[]
    totalRevenue=None
    COGS=None

    def saleInput(self,pdct): 
        allProductDetails=pdct.allProduct
        listOfProductsSale=[]
        for i in allProductDetails:
            noOfProductSale=int(input("Enter "+i.name+" quantity sale : "))
            listOfProductsSale.append(Sales(i.name,i.cost,i.revenue,noOfProductSale))
            self.totalRevenue+=(noOfProductSale*i.revenue)
            self.COGS+=(noOfProductSale*i.cost)

        return self.totalRevenue
        
    