stock_price = {}

with open("Book1.xlsx",'r') as f:
    for line in f:
        tokens = line.split(',')
    print(tokens)