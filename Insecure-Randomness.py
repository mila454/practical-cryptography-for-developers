import random, time

random.seed(time.time())
r1 = random.randrange(1e49, 1e50-1)

random.seed(time.time())
r2 = random.randrange(1e49, 1e50-1)

print(r1)
print(r2)
#53285353661739398833155340591358345604323255820576
#53285353661739398833155340591358345604323255820576
