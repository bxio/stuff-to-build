def memoize(func):
    memo = dict()

    def decorated(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]

    return decorated


@memoize
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


for i in range(100):
    print(fib(i))

