def format_price(price):
    price = int(price)
    price = f'Цена:{price} руб'
    return(price)
p = format_price(56.24)
print(p)

