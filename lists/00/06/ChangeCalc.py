COIN_VALUES = [25, 10, 5, 1]
val = float(input("Enter desired value:"))
val *= 100
rem = int(val)

for coin in COIN_VALUES:
    num_coins = int(rem/coin)
    rem = int(rem % coin)
    print(f"{num_coins} {coin}-cent pieces")
