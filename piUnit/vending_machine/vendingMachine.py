# count = 0

# currency = ["1000","500","100","50","10","5","2","1"]
# currencyCount = ["0","0","0","0","0","0","0","0"]
# amount = int(input("Enter the amount you want to withdraw : "))

# for i in range (8):
#     while (amount >= int(currency[i])):
#         a = i
#         amount = amount - int(currency[i])
#         count += 1
# print(count)

 
def currency_count(change): 
      
    notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1] 
                 
    note_count = [0, 0, 0, 0, 0, 0, 0, 0,0] 
      
    print ("Change : Note Count ") 

    result = ""
    for number1, number2 in zip(notes, note_count):
        if change >= number1: 
            number2 = change // number1  #floor division
            change = change - number2 * number1
            print (number1 ," : ", number2) 
            result += (str(number1) +" : "+ str(number2) + ",") #converting integer to string take as list
    return result

if __name__ == '__main__':
    change = int(input("Enter The Money: "))
    currency_count(change)
