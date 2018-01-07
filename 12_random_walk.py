import random

def random_walk(n):
    """return coordinates after 'n' block random walk."""
    x = 0
    y = 0

    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        else:
            x -= 1
    
    return (x, y)

def random_walk2(n):
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        x += dx
        y += dy

    return (x, y)

# for i in range(25):
#     walk = random_walk2(10)
#     print(walk, " Distance from home = ", abs(walk[0]) + abs(walk[1]))

# Monte Carlo Simulation
number_of_walks = 10000
for walk_length in range(1, 31):
    no_transport = 0
    for i in range(number_of_walks):
        (x, y) = random_walk2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size: {0} / no_transport: {1} = {2}".format(walk_length, no_transport, no_transport_percentage*100))

# Walk size: 1 / no_transport: 100000 = 1.0
# Walk size: 2 / no_transport: 100000 = 1.0
# Walk size: 3 / no_transport: 100000 = 1.0
# Walk size: 4 / no_transport: 100000 = 1.0
# Walk size: 5 / no_transport: 87843 = 0.87843
# Walk size: 6 / no_transport: 93725 = 0.93725
# Walk size: 7 / no_transport: 76385 = 0.76385
# Walk size: 8 / no_transport: 86185 = 0.86185
# Walk size: 9 / no_transport: 67186 = 0.67186
# Walk size: 10 / no_transport: 79278 = 0.79278
# Walk size: 11 / no_transport: 59784 = 0.59784
# Walk size: 12 / no_transport: 72947 = 0.72947
# Walk size: 13 / no_transport: 53868 = 0.53868
# Walk size: 14 / no_transport: 67373 = 0.67373
# Walk size: 15 / no_transport: 48942 = 0.48942
# Walk size: 16 / no_transport: 62278 = 0.62278
# Walk size: 17 / no_transport: 44657 = 0.44657
# Walk size: 18 / no_transport: 58020 = 0.5802
# Walk size: 19 / no_transport: 41256 = 0.41256
# Walk size: 20 / no_transport: 54370 = 0.5437
# Walk size: 21 / no_transport: 38283 = 0.38283
# Walk size: 22 / no_transport: 51049 = 0.51049
# Walk size: 23 / no_transport: 35522 = 0.35522
# Walk size: 24 / no_transport: 48130 = 0.4813
# Walk size: 25 / no_transport: 33394 = 0.33394
# Walk size: 26 / no_transport: 45604 = 0.45604
# Walk size: 27 / no_transport: 31010 = 0.3101
# Walk size: 28 / no_transport: 42921 = 0.42921
# Walk size: 29 / no_transport: 29343 = 0.29343
# Walk size: 30 / no_transport: 40598 = 0.40598