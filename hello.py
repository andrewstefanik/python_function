def my_function(b, a=25.00):
    area = b
    price = a
    total = area * price
    plus_tax = 0.08 * total
    after_tax = plus_tax + total
    print(after_tax)


my_function(100, )
