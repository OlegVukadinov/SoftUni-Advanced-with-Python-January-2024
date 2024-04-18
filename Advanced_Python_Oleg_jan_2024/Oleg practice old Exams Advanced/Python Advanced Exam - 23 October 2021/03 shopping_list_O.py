def shopping_list(budget,**product_data):

    if budget < 100:
        return "You do not have enough budget."

    bought_products = {}

    for product_name, product_info in product_data.items():
        current_price = product_info[0] * product_info[1]
        result = ""
        if 100 <= budget < current_price:
            continue
        # elif budget < 100:
        #     result += "You do not have enough budget."
        #     break
        if budget >= current_price:
            if product_name not in bought_products:
                bought_products[product_name] = current_price
                budget -= current_price

        if len(bought_products.keys()) == 5:
            break
    result = ""
    for product_name, total_price in bought_products.items():
        result += f"You bought {product_name} for {total_price:.2f} leva.\n"

    return result

print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))




