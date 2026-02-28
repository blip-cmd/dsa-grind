n = input()
a = "I hate "
b = "that I love "
c = "that I hate "


feel = a
for i in range(2, int(n) + 1):
    # print(i)
    if i % 2 == 0:
        feel += b
    else:
        feel += c

print(feel + "it")