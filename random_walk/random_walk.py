import random


def random_walk(n):
    """generate coordinnates after random walk"""

    x, y = (0, 0)

    for i in range(n):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x += dx
        y += dy

    return (x, y)

number_of_walks = 10000

for walk_length in range(1,41):
    no_transport = 0
    for i in range(number_of_walks):
        x, y = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 5:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print(f"walk size = {walk_length},"
          f" no need for transport: {round(100*no_transport_percentage)}%")

