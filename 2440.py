x = int(input())

for i in range(x):
    for j in range(x - i):
        print("*", end="")
    print()