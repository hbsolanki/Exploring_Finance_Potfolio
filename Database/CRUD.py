import pymongo
from utils.EmployeeManage import Employees 
from utils.ProductManage import Products
from utils.SalesManage import Sales
from utils.MonthDetails import Month
from utils.Business import Business


#Connection With Database
print("Connect To DB")
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
print(client)
db=client["FinancePotfolio"]
collection=db["business"]



def updatePasswordForManagerInDB(b):
    pass

def insertInDB(b):

    CYM=[]
    for m in b.currentYearMonths:
        CYM.append(getmonthDictionry(m))
    
    
    Y=[]
    for y in b.years:
        allM=[]
        for m in y:
            allM.append(getmonthDictionry(m))
        Y.append(allM)   

    
    employeesDetails=[]
    for i in b.employeeObjectForBusiness.employeesDetails:
        employeesDetails.append({"eid":i.eid,"name":i.name,"designation":i.designation,"salary":i.salary,"x":i.x})
    
    
    allProduct=[]
    for i in b.productObjectForBusiness.allProduct:
        allProduct.append({"pid":i.pid,"name":i.name,"cost":i.cost,"revenue":i.revenue,"x":i.x})


    collection.insert_one({
        "password":b.password,
        "bid":b.bid,
        "name":b.name,
        "debt":{
            "amount":b.debt["amount"],
            "Total_EMI":b.debt["Total_EMI"],
            "paidedEMI":b.debt["paidedEMI"],
            "persentage":b.debt["persentage"]
        },
        "haveEquity":b.haveEquity,
        "assets":b.assets,
        "currentYearMonths":CYM,
        "years":Y,
        "profit":b.profit,
        "annualRevenueRunRate":b.annualRevenueRunRate,
        "currentYearRevenue":b.currentYearRevenue,
        "product":{
            "allProduct":allProduct
        },
        "employee":{
            "employeesDetails":employeesDetails
        }
    })

def getFromDB():
    return collection.find()




def reStart():
    allBusiness=getFromDB()
    allBusinessForMain=[]

    for i in allBusiness:
        print()
        print(i)
        print()
        password=i["password"]
        bid=i["bid"]
        name=i["name"]
        debt={"amount":i["debt"]["amount"],"Total_EMI":i["debt"]["Total_EMI"],"paidedEMI":i["debt"]["paidedEMI"],"persentage":i["debt"]["persentage"]}
        haveEquity=i["haveEquity"]
        assets=i["assets"]

        currentYearMonths=[]
        for j in i["currentYearMonths"]:
            currentYearMonths.append(createMonthObj(j))
        years=[]
        for j in i["years"]:
            allM=[]
            for k in j:
                allM.append(createMonthObj(k))
            years.append
        profit=i["profit"]
        annualRevenueRunRate=i["annualRevenueRunRate"]
        currentYearRevenue=i["currentYearRevenue"]
        

        b=Business(password,bid,name)
        print(bid,name)
        b.debt=debt
        b.haveEquity=haveEquity
        b.assets=assets
        b.currentYearMonths=currentYearMonths
        b.years=years
        b.profit=profit
        b.annualRevenueRunRate=annualRevenueRunRate
        b.currentYearRevenue=currentYearRevenue
        b.productObjectForBusiness=createProductObj(i["product"])
        b.employeeObjectForBusiness=createEmployeeObj(i["employee"])
        
        allBusinessForMain.append(b)
       
    return allBusinessForMain



def createEmployeeObj(emp):
    employee=Employees()
    for j in emp["employeesDetails"]:
        employee.addEmployee(j["eid"],j["name"],j["designation"],j["salary"],j["x"])

    return employee

def createProductObj(pdct):
    product=Products()
        # product.

    for j in pdct["allProduct"]:
        product.addProduct(j["pid"],j["name"],j["cost"],j["revenue"],j["x"])
    
    return product

# "listOfProductsSale":listOfProductsSale,
#             "totalRevenue":sale.totalRevenue,
#             "COGS":sale.COGS
def createSalesObj(s):
    sale=Sales()
    listOfProductSale=[]
    totalRevenue=s["totalRevenue"]
    COGS=s["COGS"]
    for i in s["listOfProductsSale"]:
        sale.productSaleAdd(i["pid"],i["name"],i["cost"],i["revenue"],i["noOfProductSale"])
    return sale


def getmonthDictionry(m):
    employee=m.employees
    employeesDetails=[]
    for i in employee.employeesDetails:
        employeesDetails.append({"eid":i.eid,"name":i.name,"designation":i.designation,"salary":i.salary,"x":i.x})
    
    product=m.product
    allProduct=[]
    for i in product.allProduct:
        allProduct.append({"pid":i.pid,"name":i.name,"cost":i.cost,"revenue":i.revenue,"x":i.x})

    sale=m.sales
    listOfProductsSale=[]
    for i in sale.listOfProductsSale:
        listOfProductsSale.append({"pid":i.pid,"name":i.name,"cost":i.cost,"revenue":i.revenue,"quantity":i.quantity})

        
    monthDic={
        "revenue":m.revenue,
        "debt":{
            "amount":m.debt["amount"],
            "Total_EMI":m.debt["Total_EMI"],
            "paidedEMI":m.debt["paidedEMI"],
            "persentage":m.debt["persentage"]
        },
        "haveEquity":m.haveEquity,
        "EBITDA":m.EBITDA,
        "assets":m.assets,
        "marketing":m.marketing,
        "grossProfit":m.grossProfit,
        "netProfit":m.netProfit,
        "totalSalaries":m.totalSalaries,
        "COGS":m.COGS,
        "totalTaxes":m.totalTaxes,
        "other":m.other,
        "employees":{
            "employeesDetails":employeesDetails
        },
        "product":{
            "allProduct":allProduct
        },
        "sales":{
            "listOfProductsSale":listOfProductsSale,
            "totalRevenue":sale.totalRevenue,
            "COGS":sale.COGS
        },
        "shareMarket":{}
    }

    return monthDic


def createMonthObj(m):
    revenue=m[revenue]
    debt={"amount":m["debt"]["amount"],"Total_EMI":m["debt"]["Total_EMI"],"paidedEMI":m["debt"]["paidedEMI"],"persentage":m["debt"]["persentage"]}
    haveEquity=m["haveEquity"]
    EBITDA=m["EBITDA"]
    assets=m["assets"]
    marketing=m["marketing"]
    grossProfit=m["grossProfit"]
    netProfit=m["netProfit"]
    totalSalaries=m["totalSalaries"]
    COGS=m["COGS"],
    totalTaxes=m["totalTaxes"]
    other=m["other"]

    employees=createEmployeeObj(m[employees])
    product=createProductObj(m["product"])
    sales=createSalesObj(m["sales"])
    shareMarket=m["shareMarket"]

    monthObj=Month(revenue,debt,haveEquity,EBITDA,assets,marketing,grossProfit,netProfit,totalSalaries,COGS,totalTaxes,other,employees,product,sales,shareMarket)
    return monthObj




