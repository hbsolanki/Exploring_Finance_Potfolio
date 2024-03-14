import pymongo

print("Connect To DB")
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
print(client)
db=client["FinancePotfolio"]
collection=db["business"]

def insertInDB(b):
  
    CYM=[]
    for m in b.currentYearMonths:
        CYM.append(getmonthDictionry(m))
    
    
    y=[]
    for m in b.years:
        y.append(getmonthDictionry(m))

    employee=b.employee
    employeesDetails=[]
    # eid,name,designation,salary,x
    for i in employee.employeesDetails:
        employeesDetails.append({"eid":i.eid,"name":i.name,"designation":i.designation,"salary":i.salary,"x":i.x})
    
    product=b.product
    allProduct=[]
    # pid,name,cost,revenue,x
    for i in product.allProduct:
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
        "years":y,
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

        
    monthObj={
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