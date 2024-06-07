import matplotlib.pyplot as plt

class Business:

    def viewChartForAnalysis(self):
        # choice=input("(1)UnitEconomics Pie-Chart  ")
        # if choice=="1":

            activities=["COGS","Commissions,Logistics Packaging & Other","Performance Marketing","Salaries & Rent","EBITDA"]
            semiChoice=input("(1)Last Month (2)Current Year (3)Last 3 year (4)Exit")

            if semiChoice=="1":
                self.chartsUnitEconomicsForLastMonth(activities)

            elif semiChoice=="2":
                self.chartsUnitEconomicsForCurrentYear(activities)
            
            elif semiChoice=="3":
                self.chartsUnitEconomicsForLastYear(activities)

            elif semiChoice=="4":
                print("HElli")

            else:
                print("invalid option try again...")

        # elif choice=="2":
        #     self.

        # elif choice=="3":
        #     pass

        # else:
        #     print("invalid option")


    def chartsUnitEconomicsForLastMonth(self,activities):
            
            if self.currentYearMonths:
                m=self.currentYearMonths[len(self.currentYearMonths)-1]

            elif self.years:
                m=self.years[len(self.years)-1][11]

            
            revenue=m.revenue
            logistics=0
            if self.debt["Total_EMI"]!=self.debt["paidedEMI"]:
                logistics=self.debt["amount"]//self.debt["Total_EMI"]

            slices=[(m.COGS*100)/revenue,((logistics+m.other)*100)/revenue,(m.marketing*100)/revenue,(m.totalSalaries*100)/revenue,(m.EBITDA*100)/revenue]
            
            plt.pie(slices,labels=activities,startangle=90,shadow=True,radius=1.2,autopct='%1.2f%%')
            plt.legend()
            plt.show()


    def chartsUnitEconomicsForCurrentYear(self,activities):
        if self.currentYearMonths:
            logistics=0
            # if self.debt["Total_EMI"]!=self.debt["paidedEMI"]:
            #     logistics=self.debt["amount"]//self.debt["Total_EMI"]
            m=self.calculateTermsInGivenTime(self.currentYearMonths)
            slices=[(m["COGS"]*100)/m["revenue"],((logistics+m["other"])*100)/m["revenue"],(m["marketing"]*100)/m["revenue"],(m["totalSalaries"]*100)/m["revenue"],(m["EBITDA"]*100)/m["revenue"]]
        
            plt.pie(slices,labels=activities,startangle=90,shadow=True,radius=1.2,autopct='%1.2f%%')
            plt.legend()
            plt.show()

            
    def chartsUnitEconomicsForLastYear(self,activities):
        if len(self.years)>=1:
            mList=[]
            for i in self.years:
                mList.append(i)
            m=self.calculateTermsInGivenTime(mList)
            logistics=0
            # if self.debt["Total_EMI"]!=self.debt["paidedEMI"]:
            #     logistics=self.debt["amount"]//self.debt["Total_EMI"]

            slices=[(m["COGS"]*100)/m["revenue"],((logistics+m["other"])*100)/m["revenue"],(m["marketing"]*100)/m["revenue"],(m["totalSalaries"]*100)/m["revenue"],(m["EBITDA"]*100)/m["revenue"]]
        
            plt.pie(slices,labels=activities,startangle=90,shadow=True,radius=1.2,autopct='%1.2f%%')
            plt.legend()
            plt.show()



    def viewTableForAnalysis(self):
        thch=input("(1)Current Month (2)Current Year (3)Last 3 Year \n")

        if thch=="1":
            m=None
            if self.currentYearMonths:
                m=self.currentYearMonths[len(self.currentYearMonths)-1]
            else:
                m=self.years[len(self.years)-1][11]

            print(f"            *-* {self.name} *-*")
            print("--> Current Month : ")
            print("")
            print()
            print("haveEquity :",m.haveEquity)
            print("assets :",m.assets)
            print("Profit :",(m.netProfit*m.haveEquity)/100)
            print()
            print("Revenue :",m.revenue)

            print("COGS :",m.COGS)
            print("Gross Profit :",m.grossProfit)

            if m.debt["amount"]:
                print("•Dept : amount=",m.debt["amount"],"month left =",m.debt["Total_EMI"]-m.debt["paidedEMI"],"Persentage =",m.debt["persentage"])
            
            print("Marketing :",m.marketing)
            print("Salaries To Employees :",m.totalSalaries)
            print("Taxes :",m.totalTaxes)
            print("Other :",m.other)
            print()
            print("Net Profit :",m.netProfit)
            print("EBITDA :",m.EBITDA)
            print()
            print("Annual Revenue Run Rate :",self.annualRevenueRunRate)


        elif thch=="2":
            if self.currentYearMonths:
                m=self.calculateTermsInGivenTime(self.currentYearMonths)
                self.tableForAnalysis(m,"Current Year")
        
        elif thch=="3":
            if len(self.years)>=3:
                mList=[]
                for i in self.years[len(self.years)-1]:
                    mList.append(i)
                for i in self.years[len(self.years)-2]:
                    mList.append(i)
                for i in self.years[len(self.years)-3]:
                    mList.append(i)
                m=self.calculateTermsInGivenTime(mList)
                self.tableForAnalysis(m,"Last 3 Years")

        else:
            print("Invalid Option")


    def tableForAnalysis(self,m,time):
        print(f"            *-* {self.name} *-*")
        print("-->",time,": ")
        print("")
        print()
        print("Profit :",m["profit"])
        print()
        print("Revenue :",m["revenue"])

        print("COGS :",m["COGS"])
        print("Gross Profit :",m["grossProfit"])

        print("Marketing :",m["marketing"])
        print("Salaries To Employees :",m["totalSalaries"])
        print("Taxes :",m["totalTaxes"])
        print("Other :",m["other"])
        print()
        print("Net Profit :",m["netProfit"])
        print("EBITDA :",m["EBITDA"])
        print()


    def tableForAnalysisSaveInPDF(self,m,time):
        f=open("Finance_Portfolio.pdf","+w")
        f.write(f"            *-* {self.name} *-*\n")
        f.write("--> "+time+" : \n")
        f.write("\n")
        f.write("\n")
        f.write("Profit : "+str(m["profit"])+" \n")
        f.write("\n")
        f.write("Revenue : "+str(m["revenue"])+" \n")

        f.write("COGS : "+str(m["COGS"])+" \n")
        f.write("Gross Profit : "+str(m["grossProfit"])+" \n")

        f.write("Marketing : "+str(m["marketing"])+" \n")
        f.write("Salaries To Employees : "+str(m["totalSalaries"])+" \n")
        f.write("Taxes : "+str(m["totalTaxes"])+" \n")
        f.write("Other : "+str(m["other"])+" \n")
        f.write("\n")
        f.write("Net Profit : "+str(m["netProfit"])+" \n")
        f.write("EBITDA : "+str(m["EBITDA"])+" \n")
        f.close()
        print("All Data Saved in Finance_Portfolio.pdf file")


    def calculateTermsInGivenTime(self,givenTimeInMonth):
        ans={"profit":0,"revenue":0,"COGS":0,"grossProfit":0,"marketing":0,"totalSalaries":0,"totalTaxes":0,"other":0,"netProfit":0,"EBITDA":0}

        for m in givenTimeInMonth:
            ans["profit"]+=(m.netProfit*m.haveEquity)/100
            ans["revenue"]+=m.revenue
            ans["COGS"]+=m.COGS
            ans["grossProfit"]+=m.grossProfit
            ans["marketing"]+=m.marketing
            ans["totalSalaries"]+=m.totalSalaries
            ans["totalTaxes"]+=m.totalTaxes
            ans["other"]+=m.other
            ans["netProfit"]+=m.netProfit
            ans["EBITDA"]+=m.EBITDA

        return ans
    

    def generateFinanceMatrix(self):
        thch=input("(1)Current Month (2)Current Year (3)Last 3 Year \n")
        f=open("Finance_Portfolio.pdf","+w")
        m=None

        if self.currentYearMonths:
            m=self.currentYearMonths[len(self.currentYearMonths)-1]
        else:
            m=self.years[len(self.years)-1][11]

    
        if thch=="1":
            f.write(f"            *-* {self.name} *-*\n")
            f.write("--> Current Month : \n")
            f.write("\n")
            f.write("\n")
            f.write("haveEquity : "+str(m.haveEquity)+" \n")
            f.write("assets : "+str(m.assets)+" \n")
            f.write("Profit : "+str((m.netProfit*m.haveEquity)/100)+" \n")
            f.write("\n")
            f.write("Revenue : "+str(m.revenue)+" \n")

            f.write("COGS : "+str(m.COGS)+" \n")
            f.write("Gross Profit : "+str(m.grossProfit)+" \n")

            if m.debt["amount"]:
                f.write("•Dept : amount= "+str(m.debt["amount"])+" month left = "+str(m.debt["Total_EMI"]-m.debt["paidedEMI"])+" Persentage = "+str(m.debt["persentage"])+" \n")
            
            f.write("Marketing : "+str(m.marketing)+" \n")
            f.write("Salaries To Employees : "+str(m.totalSalaries)+ " \n")
            f.write("Taxes : "+str(m.totalTaxes)+" \n")
            f.write("Other : "+str(m.other)+" \n")
            f.write("\n")
            f.write("Net Profit : "+str(m.netProfit)+" \n")
            f.write("EBITDA : "+str(m.EBITDA)+" \n")
            f.write("\n")
            f.write("Annual Revenue Run Rate : "+str(self.annualRevenueRunRate)+" \n")
            f.close()
            print()
            print("All Data Saved in Finance_Portfolio.pdf file")

        elif thch=="2":
            if self.currentYearMonths:
                m=self.calculateTermsInGivenTime(self.currentYearMonths)
                self.tableForAnalysisSaveInPDF(m,"Current Year")
        
        elif thch=="3":
            if len(self.years)>=3:
                mList=[]
                for i in self.years[len(self.years)-1]:
                    mList.append(i)
                for i in self.years[len(self.years)-2]:
                    mList.append(i)
                for i in self.years[len(self.years)-3]:
                    mList.append(i)
                m=self.calculateTermsInGivenTime(mList)
                self.tableForAnalysisSaveInPDF(m,"Last 3 Years")

        else:
            print("invalid option try again....")