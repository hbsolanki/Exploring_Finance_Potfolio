#1.some 2.sharemarket 3.marketing 4.product 5.employee

class Main:

    def __init__(self,password):
        self.allBusiness=[]
        self.ownerPass=password
        self.managers=[]

    def addManager(self):
        id=int(input("Enter Bussiness id : "))
        print()
        password=input("Enter Password To set : ")
        d={"id":id,"password":password}

    def mainFunc(self):
        type=input("(1)Owner \n(2)Manager \n")
        print()

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
            

    def owner(self):
        choice=input("(1)Analysis Business (2)Create Business")
        if choice=="1":
            print()
            for i in self.allBusiness:
                print(i.bid,i.name)
            print()
            idForANA=int(input("Enter Business ID For Analysis : "))
            for i in self.allBusiness:
                if idForANA==i.id:
                    i.main()
        elif choice=="2":
            #Creating New Business and ADD All Business 
            pass
            
            

    def manage(self,bid):
        bid.manager()



Main("hb").mainFunc()