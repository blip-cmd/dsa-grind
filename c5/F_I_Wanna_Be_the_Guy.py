n= int(input())
s = set((map(int,(input().split()[1:] + input().split()[1:]))))
# print(s)

if s == set(range(1, n + 1)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")   

# print([x for x in range(1, n + 1)])

# print(range(1, n + 1))