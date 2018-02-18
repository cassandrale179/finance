import re
feb = "/Users/cassandrale/Desktop/finance/account.csv"
f  = open(feb, "r")

class Category:
    def __init__(self):
        self.transfer = 0
        self.t = 0
        self.f = 0
        self.g = 0
        self.s = 0
        self.u = 0
        self.h = 0
        self.a = 0
        self.v = 0
        self.r = 0
        self.depo = 0
        self.spend = 0

    def PRINT(self):
        print("Transportation: ", self.t)
        print("Food: ", self.f)
        print("Grocery: ", self.g)
        print("Subscription: ", self.s)
        print("Utilities: ", self.u)
        print("Eye surgery: ", self.h)
        print("Amazon: ", self.a)
        print("Transfer: ", self.transfer)
        print("Venmo / Paypal: ", self.v)
        print("Rent: ", self.r)
        print("Total deposit: ", self.depo)
        print("Total spending: ", self.spend)

#-------------- CREATE OBJECT PAYMENT ----------
class Payment:
    def __init__(self, d, t, v, c):
        self.value = v
        self.title = t
        self.date = d
        self.category = c


c = Category()
for line in f:

    #----------------- CREATE STUFF ----------------
    line = line.strip()
    i = [m.start() for m in re.finditer('"', line)]
    date = line[i[0]:i[1]][1:]
    title = line[i[2]:i[3]]
    withdrawal = line[i[4]:i[5]][2:].replace(',', '')
    deposit = line[i[6]:i[7]][2:].replace(',', '')


    #--------- CHECK WITHDRAWAL OR DEPOSIT --------
    value = 0
    if withdrawal:
        value = float(withdrawal)*-1
        c.spend += value
    elif deposit:
        value = float(deposit)
        c.depo += value

    #--------- CATEGORY -------
    category = ""
    if "UBERUS" in title or "LYFT" in title:
        category = "Transportation"
        c.t += value
    elif "PIZZA" in title or "STARBUCKS" in title or "FOOD TRUCK" in title or "GYRO" in title or "SBUCKS" in title:
        category = "Food"
        c.f += value
    elif "MARKETPLACE" in title or "INSTACART" in title:
        category = "Groceries"
        c.g += value
    elif "AMAZON" in title:
        category = "Amazon"
        c.a += value
    elif "AIRBNB" in title:
        category = "Rent"
        c.r += value
    elif "VENMO" in title or "PAYPAL" in title and value < 0:
        category = "Venmo and Paypal"
        c.v += value
    elif "PECO" in title:
        category = "Utilities"
        c.u += value
    elif "US MOBILE" in title or "Spotify" in title:
        category = "Subscription"
        c.s += value
    elif "HEALTHCARE" in title:
        category = "Eye Surgery"
        c.h += value
    elif "ONLINE TRANSFER" in title and value < 0:
        category = "Online Transfer"
        c.transfer += value
    elif value > 0 or "DEPOSIT" in title:
        category = "Deposit"
    else:
        category = "Unknown"

    p = Payment(date,title,value,category)

#----------- END OF PROGRAM ---------
c.PRINT()
