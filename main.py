#1.some 2.sharemarket 3.marketing 4.product 5.employee
from utils.Business import Business
from Database.CRUD import insertInDB,updatePasswordForManagerInDB,deleteBusiness
from Database.getData import reStart

class Main:

    def __init__(self,password):
        self.allBusiness=[]
        self.ownerPass=password


    def mainFunc(self):
        #getting Data From Database
        self.allBusiness=reStart()

        choice=None
        

        while choice!="3":
            print()
            choice=input("(1)Owner \n(2)Manager \n(3)Exit \n")

            if choice=="1":
                password=input("Enter Password : ")
                if self.ownerPass==password:
                    self.owner()
                else:
                    print("Wrong password Try Again...")


            elif choice=="2":
                id=int(input("Enter Bussiness id : "))

                for i in self.allBusiness:
                    if i.bid==id:
                        password=input("Enter Password : ")
                        if i.password==password:
                            i.manager()
                            return
                        else:
                            print("Wrong password Try Again...")
                            break
                else:
                    print("This ID NOT VALID")


            elif choice=="3":
                break

            else:
                print("Invalid Option")

        
    def owner(self):
        choice=None

        while choice!="3":
            print()
            choice=input("(1)Analysis Business \n(2)Create Business \n(3)Add Manager For Particular Business \n(4)Delete Business \n(5)Exit \n ")

            # try:

            if choice=="1":

                print()
                for i in self.allBusiness:
                    print("Business ID :",i.bid,"Name :",i.name)
                print()
                
                idForANA=int(input("Enter Business ID For Analysis : "))
                for i in self.allBusiness:
                    if idForANA==i.bid:
                        i.owner()
                        break
                else:
                    print("INVALID Business ID")
                
            elif choice=="2":

                #Creating New Business and ADD All Business 
                print()
                self.newBusinessCreateAnalysis()

            elif choice=="3":
                self.addManager()

            elif choice=="4":
                print()
                print("Available Business :")
                print()
                for i in self.allBusiness:
                    print("Bid :",i.bid,"Name :",i.name)

                bid=int(input("Enter Business ID : "))
                deleteBusiness(bid)

            elif choice=="5":
                break

            else:
                print("INVALID Option")
                self.owner()


            # except:
            #         print("Error Occure")


    def newBusinessCreateAnalysis(self):
        totalProfit=0
        totalDebt=0

        for i in self.allBusiness:
            totalProfit+=i.profit
            if i.debt["Total_EMI"]:
                totalDebt+=((i.debt["amount"]/i.debt["Total_EMI"])*(i.debt["Total_EMI"]-i.debt["paidedEMI"]))

            if i.debt["Total_EMI"]==0 and i.debt["amount"]:
                totalDebt+=i.debt["amount"]

        print("** From All Business Total Profit :",totalProfit,"₹")
        print("** From All Business Total Debt :",round(totalDebt,2),"₹")
        print()
        print("(1)Create New Business (else)Exit")
        choice=input()

        if choice=="1":

            try:

                bid=int(input("Enter Business ID : "))
                name=input("Enter Business Name : ")
                haveEquity=int(input("You Have Equity : "))
                assets=int(input("Enter Cost Of Assets : "))
                b=Business("",bid,name)
                print(b.productObjectForBusiness.allProduct)
                b.haveEquity=haveEquity
                b.assets=assets
                ch=input("(1)Take Debt (2)Not Take Debt :")

                if ch=="1":
                    print("->Debt Details  ")
                    amount=int(input("Enter Amount : "))
                    b.debt["amount"]=amount
                    chemi=input("(1)Converted Into EMI (2)Not Converted Into EMI  : ")
                    if chemi=="1":
                        Total_EMI=int(input("Enter Total EMI Month : "))
                        
                        b.debt["Total_EMI"]=Total_EMI

                    else:
                        persentage=float(input("Enter Persentage Of Debt : "))
                        b.debt["persentage"]=persentage
                    
                
                self.allBusiness.append(b)
                insertInDB(b)
                print()
                print("Business ID :",b.bid,"Name :",b.name," is Created")

            except:

                print("Something Wrong....")
            
        else:
            return
        
    def addManager(self):
        id=int(input("Enter Bussiness id : "))
        print()
        password=input("Enter Password To set : ")
        for i in self.allBusiness:
            if i.bid==id:
                i.password=password
                updatePasswordForManagerInDB(i)
                break
        
        else:
            print("Invalid Id")
        

    
#Creating Main Object
Main("hb").mainFunc()