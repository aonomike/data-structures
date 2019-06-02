
def coin_change(amount):
    denominations = [1,5,10,20,50,100,200,500,1000]
    denominations.reverse()
    coins = []
    for denomination in denominations:
        if denomination < amount:
            number_of_denomination, amount = divmod(amount,denomination)
            coins.append({"number": number_of_denomination, "denomination": denomination})
    print(coins)
    print(sum(coins['denomination']))
coin_change(3454)