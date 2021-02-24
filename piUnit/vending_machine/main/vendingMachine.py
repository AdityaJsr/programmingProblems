
def currency_counter(amount):
    count = 0
    currency = [1000,500,100,50,10,5,2,1]
    currencyCount = [0, 0, 0, 0, 0, 0, 0, 0,0]
    result = ('')

    for c1, cc in zip (currency,currencyCount): 
        while (amount >= c1):
            cc = amount // c1
            count += cc
            amount = amount - cc*c1
            print(f'{c1} \t: {cc}')
            result += (str(c1) +" : "+ str(cc) + ",")
    print("The minimum number of notes : "+str(count))
    return (result)

if __name__ == '__main__':
    amount = int(input("Enter the amount : "))
    try:
        amount
    except ValueError:
        print("Incorrect value Enter number only!!")
    print(f'currency : count')
    currency_counter(amount)
