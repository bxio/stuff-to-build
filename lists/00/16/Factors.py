def print_factors(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)

    print(f"The factors of {x} are: {factors}")

num = int(input("Enter a number: "))
print_factors(num)
