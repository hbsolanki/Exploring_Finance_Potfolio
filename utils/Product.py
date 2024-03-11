import numpy as np
class Products:

    class Product:
        def __init__(self,name,cost,revenue,x):
            self.name=name
            self.cost=cost
            self.revenue=revenue
            self.x=x

    

    allProduct=np.empty()
    # daySale=np.empty()

    def generateBulkProduct(self,name,totalCost,quantity):
        perProductCost=totalCost//quantity
        print("Per Product cost is :",perProductCost)
        selePrice=int(input("Enter Expected Sale Price"))
        perProductRevenue=selePrice-perProductCost

        self.addProduct(name,perProductCost,perProductRevenue,"")

    
    
    def addProduct(self,name,cost,revenue,x):
        p=self.Product(name,cost,revenue,x)
        
    def perProductRevenue(self):
        pass
    

    def perProductCost(self):
        pass
