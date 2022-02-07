def create_multipliers():
    multipliers = []

    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier)
    
    return multipliers

mults = create_multipliers()

# print(mults[0](5))

def create_multipliers_lambda():
    return [lambda x, i=i: i * x for i in range(5)]

mults = create_multipliers_lambda()

for mult in mults:
    for val in range(6):
        print(mult(val))
    print('----')    