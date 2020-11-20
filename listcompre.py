import math

# _list = [2*x+1 for x in [10, 20, 30] if x > 0 ] map(lambda x: 2*x+1, filter(lambda x: x > 0, [10, 20, 30]))
x = [2*x+5 for x in [10, 20, 30] if x > 0]
map(lambda x: 2*x+1,
    filter(lambda x: x > 0, [10, 20, 90]))

print(x)