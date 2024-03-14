#1.some 2.sharemarket 3.marketing 4.product 5.employee
from utils.Business import Business
from Database.CRUD import insertInDB,getFromDB

class Main:

    def __init__(self,password):
        self.allBusiness=[]
        self.ownerPass=password
        # self.managers=[]

    def addManager(self):
        id=int(input("Enter Bussiness id : "))
        print()
        password=input("Enter Password To set : ")
        # d={"id":id,"password":password}
        for i in self.allBusiness:
            if i.bid==id:
                i.password=password
        else:
            print("Invalid Id")

    def mainFunc(self):
        type=None
        print()

        while type!="3":
            type=input("(1)Owner \n(2)Manager \n(3)Exit \n")
            if type=="1":
                password=input("Enter Password : ")
                if self.ownerPass==password:
                    self.owner()
                else:
                    print("Wrong password Try Again...")
            elif type=="2":
                id=int(input("Enter Bussiness id : "))
                for i in self.managers:
                    if i["id"]==id:
                        password=input("Enter Password : ")
                        if i["password"]==password:
                            self.manage(i["id"])
                            return
                        else:
                            print("Wrong password Try Again...")
                            break
                else:
                    print("This ID NOT VALID")

        for i in self.allBusiness:
            insertInDB(i)
            
            

    def owner(self):
        choice=None
        while choice!="3":
            choice=input("(1)Analysis Business \n(2)Create Business \n(3)Add Manager For Particular Business \n(4)Exit \n ")
            if choice=="1":
                print()
                for i in self.allBusiness:
                    print(i.bid,i.name)
                print()
                try:
                    idForANA=int(input("Enter Business ID For Analysis : "))
                    for i in self.allBusiness:
                        if idForANA==i.id:
                            print("Hello")
                            i.main()
                            print("Hello2")
                            return
                    else:
                        print("INVALID Business ID")
                except:
                    print("Error Occure")
            elif choice=="2":
                #Creating New Business and ADD All Business 
                print()
                self.newBusinessCreateAnalysis()
            elif choice=="3":
                self.addManager()
            elif choice=="4":
                break
            else:
                print("INVALID Option")
                self.owner()
            
            

    def manage(self,bid):
        bid.manager()


    def newBusinessCreateAnalysis(self):
        totalProfit=0
        totalDebt=0
        for i in self.allBusiness:
            totalProfit+=i.profit
            totalDebt+=((i.debt["amount"]/i.debt["Total_EMI"])*(i.debt["Total_EMI"]-i.debt["paidedEMI"]))

        print("** From All Business Total Profit :",totalProfit,"₹")
        print("** From All Business Debt Profit :",totalDebt,"₹")

        print("(1)Create New Business (else)Exit")
        choice=input()

        if choice=="1":
            #bid,name,debt,haveEquity,assets
            try:
                bid=int(input("Enter Business ID : "))
                name=input("Enter Business Name : ")
                haveEquity=int(input("You Have Equity : "))
                assets=int(input("Enter Cost Of Assets : "))
                b=Business("",bid,name)
                b.haveEquity=haveEquity
                b.assets=assets
                ch=input("(1)Take Debt (2)Not Take Debt :")
                if ch=="1":
                    print("->Debt Details  ")
                    amount=int(input("Enter Amount : "))
                    chemi=input("(1)Converted Into EMI (2)Not Converted Into EMI")
                    if chemi=="1":
                        Total_EMI=int(input("Enter Total EMI Month : "))
                        b.debt["amount"]=amount
                        b.debt["Total_EMI"]=Total_EMI
                    else:
                        
                        persentage=int(input("Enter Persentage Of Debt : "))
                        b.debt["persentage"]=persentage
                    
                
                self.allBusiness.append(b)

            except:
                print("Some Error Occur")
            
        else:
            return

    #   collection.insert_one({
    #     "password":b.password,
    #     "bid":b.bid,
    #     "name":b.name,
    #     "debt":{
    #         "amount":b.debt["amount"],
    #         "Total_EMI":b.debt["Total_EMI"],
    #         "paidedEMI":b.debt["paidedEMI"],
    #         "persentage":b.debt["persentage"]
    #     },
    #     "haveEquity":b.haveEquity,
    #     "assets":b.assets,
    #     "currentYearMonths":CYM,
    #     "years":y,
    #     "profit":b.profit,
    #     "annualRevenueRunRate":b.annualRevenueRunRate,
    #     "currentYearRevenue":b.currentYearRevenue,
    #     "product":{
    #         "allProduct":allProduct
    #     },
    #     "employee":{
    #         "employeesDetails":employeesDetails
    #     }
    # })


    def reStart(self):
        allBusiness=getFromDB()
        for i in allBusiness:
            password=i.password
            bid=i.bid
            name=i.name
            debt={"amount":i.debt["amount"],"Total_EMI":i.debt["Total_EMI"],"paidedEMI":i.debt["paidedEMI"],"persentage":i.debt["persentage"]}
            haveEquity=i.haveEquity
            assets=i.assets
            currentYearMonths=[]

    # def getMonth(m):

Main("hb").mainFunc()