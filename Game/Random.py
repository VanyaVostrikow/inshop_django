import random
def randim():
    a = [0, 0, 0, 0]
    all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(a)):
        a[i] = random.choice(all)
        all.remove(a[i])
randim()

