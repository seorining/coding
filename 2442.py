x = int(input())

for i in range(x):
    for j in range(x - i - 1):
        print(" ", end="")
    for j in range(2*i + 1):
        print("*", end="")
    print()
