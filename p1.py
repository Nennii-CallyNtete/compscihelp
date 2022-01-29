def ten_percent (price):
    disc_price = price * 0.9
    price_print(disc_price)


def twenty_percent (price):
    disc_price = price * 0.8
    price_print(disc_price)


def price_print (disc_price):
    print("Discounted Price is ", disc_price)
    
    
price = input("Enter the total regular price of purchase:")
price = float(price)

if(price > 100):
    twenty_percent(price)
elif(price <=100):
    ten_percent(price)