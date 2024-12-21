#For loop

for x in range(1,7,2):
    print(x)

#half pyramide
def half_pyramid(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end="")
        print("")
n=5
half_pyramid(n)
