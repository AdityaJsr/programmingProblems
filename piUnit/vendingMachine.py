count = 0

currency = ["1000","500","100","50","10","5","2","1"]
amount = int(input("Enter the amount you want to withdraw : "))

for i in range (8):
    while (amount >= int(currency[i])):
        a = i
        amount = amount - int(currency[i])
        count += 1
print(count)

