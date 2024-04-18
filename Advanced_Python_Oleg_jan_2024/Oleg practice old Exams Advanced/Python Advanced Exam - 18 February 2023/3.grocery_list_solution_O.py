def shop_from_grocery_list(budget, init_products, *args):

    bought_products = []

    for product_name, product_price in args:
        if product_name not in init_products:
            continue
        if product_name not in bought_products:
            if budget >= product_price:
                bought_products.append(product_name)
                budget -= product_price
                init_products.remove(product_name)
            else:
                break
        if product_name in bought_products:
             continue

    if not init_products:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(init_products)}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
