# WARNING: The pseudo-random generators of this module should not be used for security purpose.
# Use os.urandome() or SystemRandom if you require a cryptographically secure pseudo-random number generator.

import random

dir(random)

# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', 'WichmannHill', '_BuiltinMethodT
# ype', '_MethodType', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_acos', '_ceil', '_cos', '_e',
# '_exp', '_hashlib', '_hexlify', '_inst', '_log', '_pi', '_random', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn
# ', 'betavariate', 'choice', 'division', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'jumpahead', 'lognormva
# riate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular',
#  'uniform', 'vonmisesvariate', 'weibullvariate']

for i in range(10):
    print random.random()

# Generator random numbers from interval [3, 7)

def my_random():
    # Random, scale, shift, return
    # return 4 * random.random() + 3
    return random.uniform(3, 7)

for i in range(10):
    print my_random()

# random() and uniform() are normal distribution(正太分布，aka "Bell Curve")

# discrete probability distributions (离散)

for i in range(10):
    print random.randint(1, 6)

outcomes = ["rock", "paper", "scissors"]

for i in range(10):
    print random.choice(outcomes)