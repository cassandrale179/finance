import re
import sys
if (len(sys.argv)) > 1:
    acc = "spending/" + sys.argv[1]
else:
    acc = "spending/2018may.csv"
f  = open(acc, "r")

#------- GLOBAL ARRAY -------
food = ["NASSAU", "STARBUCKS", "KIWI", "SBUCKS", "GRUBHUB", "GYRO", "COFFEE", "PENANG", "HALAL", "TEA", "SHAKE SHACK", "TRYCAVIARCOM", "CAFE"]
transportation = ["UBER", "LYFT", "SEPTA", "NJT"]
grocery = ["INSTACART", "WALMART", "TARGET", "WEGMANS", "MARKETPLACE"]
amazon = ["AMAZON"]
housing = ["AIRBNB"]
utilites = ["PECO", "VERIZON", "GAS", "US MOBILE", "ATT", "NOTARIZE"]
entertainment = ["Spotify", "MintSIM", "HBO", "AMC", "US MOBILE"]
healthcare = ["HEALTHCARE"]
transfer = ["TRANSFER"]
deposit = ["HIREGENICS", "PLUS RELOCATION", "PAYPAL"]

name = ["food", "transportation", "grocery", "amazon", "housing", "utilites", "entertainment", "healthcare",  "transfer", "deposit"]
category = [food, transportation, grocery, amazon, housing, utilites, entertainment, healthcare, transfer, deposit]
values = [0]*len(category)
statement = []

known = []
unknown = []


for line in f:
    line = line.strip()
    statement.append(line)

ind = 0
for item in category:
    for line in statement:

        #----------------- CREATE STUFF ----------------
        line = line.strip()
        i = [m.start() for m in re.finditer('"', line)]
        date = line[i[0]:i[1]][1:]
        title = line[i[2]:i[3]]
        withdrawal = line[i[4]:i[5]][2:].replace(',', '')
        deposit = line[i[6]:i[7]][2:].replace(',', '')

        value = 0
        if withdrawal:
            value = float(withdrawal)*-1
        elif deposit:
            value = float(deposit)

        if any(s in title for s in item):
            values[ind] += value
            known.append(line)
    ind += 1

for i in range(0,7):
    print(name[i], values[i])

print("Total spending", sum(values))


unknown = list(set(statement) - set(known))
