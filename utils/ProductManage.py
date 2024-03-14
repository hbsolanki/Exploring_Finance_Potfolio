import numpy as np
class Products:

    class Product:
        def __init__(self,pid,name,cost,revenue,x):
            self.pid=pid
            self.name=name
            self.cost=cost
            self.revenue=revenue
            self.x=x

    

    allProduct=[]
    # daySale=np.empty()

    # def generateBulkProduct(self,name,totalCost,quantity):
    #     perProductCost=totalCost//quantity
    #     print("Per Product cost is :",perProductCost)
    #     selePrice=int(input("Enter Expected Sale Price"))
    #     perProductRevenue=selePrice-perProductCost

    #     self.addProduct(name,perProductCost,perProductRevenue,"")

    
    
    def addProduct(self,pid,name,cost,revenue,x):
        p=self.Product(pid,name,cost,revenue,x)
        self.allProduct.append(p)

    def printAllProductDatails(self):
        # print("Eid  Name  designation   salary   Details")
        for i in self.allProduct:
            print(i.pid,i.name,i.cost,i.revenue,i.x)
        
    def perProductRevenue(self):
        pass
    

    def perProductCost(self):
        pass

    def copyProduct(self,p2):
        for i in p2.allProduct:
            self.addProduct(i.pid,i.name,i.cost,i.revenue,i.x)


    def productManagement(self):
        choice=None
        while choice !="4":
            choice=input("(1)Add Product \n(2)Remove Product \n(3)Increment All Product Price \n(4)Increment Price Particular Product \n(5)View All Product Details \n(6)View Particular Product Details \n(7)Exit \n")
            
            if choice=="1":

                pid=int(input("Enter Product ID : "))
                #,pid,name,cost,revenue,x
                name=input("Enter Name Of Product : ")
                cost=input("Enter Cost Of Product : ")
                revenue=int(input("Enter product Revenue : "))
                x=input("Enter Other Description Of Product : ")
                self.addProduct(pid,name,cost,revenue,x)

            elif choice=="2":
                pid=int(input("Enter Product ID : "))
                for i in self.allProduct:
                    if i.pid==pid:
                        self.allProduct.remove(i)
                        print("Product Successfuly Removed...")
                        break
                else:
                    print("This Product ID Not Found...")
            elif choice=="3":
                incrementPrice=int(input("Enter Increment Price : "))
                for i in self.allProduct:
                    i.cost+=incrementPrice
                else:
                    print("For All Product Price Incremented")
            elif choice=="4":
                pid=int(input("Enter Product ID : "))
                incrementPrice=int(input("Enter Increment Price : "))
                for i in self.allProduct:
                    if i.pid==pid:
                        i.cost+=incrementPrice
                        print("Product Price Incremented...")
                        break
                else:
                    print("This Product ID Not Found...")
            elif choice=="5":
                self.printAllProductDatails()
            elif choice=="6":
                eid=int(input("Enter Product ID : "))
                for i in self.employeesDetails:
                    if i.pid==pid:
                        print(i.pid,i.name,i.cost,i.revenue,i.x)
                        break
                else:
                    print("This Product ID Not Found...")
            elif choice=="7":
                break
            else:
                print("Invalid Option")
            