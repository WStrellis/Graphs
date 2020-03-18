from random import randint


def fisher_yates_shuffle(l):
    for i in range(0, len(l)):
        rand_index = randint(i, len(l) - 1)
        # swap values
        l[rand_index], l[i] = l[i], l[rand_index]


if __name__ == '__main__':

    foo = [i for i in range(1, 11)]
    print(foo)
    fisher_yates_shuffle(foo)
    print(foo)
