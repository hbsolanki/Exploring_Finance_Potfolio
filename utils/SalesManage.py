import matplotlib.pyplot as plt

class Sales:

    class Sale:
        def __init__(self,pid,name,cost,revenue,quantity):
            self.pid=pid
            self.name=name
            self.cost=cost
            self.revenue=revenue
            self.quantity=quantity

    listOfProductsSale=[]
    totalRevenue=0
    COGS=0   #Cost Of Goods sold



    def productSaleAdd(self,pid,name,cost,revenue,noOfProductSale):
        self.listOfProductsSale.append(self.Sale(pid,name,cost,revenue,noOfProductSale))


    def saleInput(self,pdct): 
        
        for i in pdct.allProduct:
            
            noOfProductSale=int(input("Pid "+str(i.pid)+" Name :" +i.name+" quantity sale : "))
            self.listOfProductsSale.append(self.Sale(i.pid,i.name,i.cost,i.revenue,noOfProductSale))
            # print(i.revenue)
            self.totalRevenue+=(noOfProductSale*i.revenue)
            self.COGS+=(noOfProductSale*(i.cost-i.revenue))

        return self.totalRevenue
    

    def viewSaleDetails(self):
        choice=None

        while choice!=4:
            choice=input("(1)View All Product Sale (2)View Particular Product Sale (3)Chart For All Product Quantity (4)Exit \n")

            if choice=="1":
                self.viewAllProductSale()

            elif choice=="2":
                pid=int(input("Enter Product Id : "))
                for i in self.listOfProductsSale:
                    if i.pid==pid:
                        print((i.pid,i.name,i.cost,i.revenue,i.quantity))
                        print()

            elif choice=="3":
                
                name=[]
                quan=[]
                for i in self.listOfProductsSale:
                    name.append(i.name)
                    quan.append(i.quantity)

                plt.subplot(1,2,1)
                plt.pie(quan,labels=name,startangle=90,shadow=True,radius=1.2,autopct='%1.2f%%')
                plt.subplot(1,2,2)
                plt.bar(name,quan)
                plt.legend()
                plt.show()

            elif choice=="4":
                break
            
            else:
                print("Invalid Option try again...")


    def viewAllProductSale(self):
        print()
        for i in self.listOfProductsSale:
            print("Pid :",i.pid," Name :",i.name," Cost :",i.cost," Revenue :",i.revenue," Quantity :",i.quantity)
            print()
        