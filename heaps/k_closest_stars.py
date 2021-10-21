from heapq import heappushpop as pushpop
from heapq import heappush as push


def k_closest_stars(stars, k):
    h = []
    for i in range(k):
        d = stars[i][0]**2 + stars[i][1]**2
        push(h, (-d, stars[i]))

    for i in range(k, len(stars)):
        d = stars[i][0]**2 + stars[i][1]**2
        pushpop(h, (-d, stars[i]))
    return [star[1] for star in h]


if __name__ == "__main__":
    print(k_closest_stars([(-1, -2), (3, 2), (17, 18), (39, 16), (7, 3),  (-3, -6)], 3))
