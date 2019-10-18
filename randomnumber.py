import timeit

def random_number(min,max):

    """
        Returns random from [min,max]

    """

    range = max - min + 1

    seed_time = timeit.default_timer()
    seed = int((seed_time - int(seed_time))* (10000000))
    seed = (seed % range)

    return seed + min

def six_sided_dice():

    return random_number(1,6)

def coin_flip():

    "Slight skew toward heads?"

    x = random_number(0,1)
    if x == 1:
        return 'H'
    else:
        return 'T'

print(six_sided_dice())
print(coin_flip())
