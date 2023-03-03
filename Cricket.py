import random
X = ['NR','S','D','T','F','SX','W']
def score(X):
    p = random.choice(X)
    return p
print("\n### Welcome to Cricket Now ###")
n = input("\nEnter the number of balls to be played:")
sum = 0
for i in range(1,int(n)+1):
    Y = score(X)
    print(Y)
    run = 0
    if Y=='NR':
        run = 0
        print("---0 runs---\n")
    if Y=='S':
        run = 1
        print("---1 runs---\n")
    if Y=='D':
        run = 2
        print("---2 runs---\n")
    if Y=='T':
        run = 3
        print("---3 runs---\n")
    if Y=='F':
        run = 4
        print("---4 runs---\n")
    if Y=='SX':
        run = 6
        print("---6 runs---\n")
    if Y=='W':
        print("Out!!!\n")
        run = 0
        print("Game Ended!!!")
        print("\nYou scored:",sum,"runs")
        exit(0)
    sum = sum + run
print("\nYou scored:",sum,"runs")