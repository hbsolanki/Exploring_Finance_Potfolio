import numpy as np
import Product as pdct

class Sales:

    class Sale:
        def __init__(self,name,cost,revenue,quantity):
            self.name=name
            self.cost=cost
            self.revenue=revenue
            self.quantity=quantity

    currentMonthDaySale=np.empty([31], dtype=object)
    currentYearMonthSale=np.empty([12], dtype=object)
    yearlySale=[]

    def daySaleInput(self,pdct): 
        allProductDetails=pdct.allProduct
        listOfProductsSale=[]
        for i in allProductDetails:
            noOfProductSale=int(input("Enter "+i.name+" quantity sale : "))
            listOfProductsSale.append(Sales(i.name,i.cost,i.revenue,noOfProductSale))

        self.reStoreAndReGenerate()
        # name=input("Enter Product Name")
            
    def reStoreAndReGenerate(self):
        if(len(self.currentMonthDaySale)==30):
            if(len(self.currentYearMonthSale)==12):
                self.yearlySale.append(self.currentYearMonthSale.copy())
            else:
                for i in range(12):
                    if(self.currentYearMonthSale[i]==None):
                        self.currentYearMonthSale[i]=self.currentMonthDaySale

    def getMonthSale():
        pass

    def getDaySale():
        pass

    def getYearSale():
        pass

    