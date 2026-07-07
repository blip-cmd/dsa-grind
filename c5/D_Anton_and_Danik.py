n = int(input())
s = input()

anton = 0
danik = 0

for c in s:
    if c == 'A':
        anton += 1
    elif c == 'D':
        danik += 1

if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
else:
    print("Friendship")