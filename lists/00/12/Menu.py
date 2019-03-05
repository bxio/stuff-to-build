menu = [3.50,
        2.50,
        4.00,
        3.50,
        1.75,
        1.50,
        2.25,
        3.75,
        1.25
        ]

items = input("give items:")
total = 0
for c in items:
    if c.isdigit():
        c = int(c)
        if c-1 >= 0:
            total += menu[int(c-1)]
print(total)
