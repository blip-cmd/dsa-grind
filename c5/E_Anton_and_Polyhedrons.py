n = int(input())

result = 0
for _ in range(n):
    s = input()
    
    #interate once and check each on
    if s == "Tetrahedron":
        result += 4
    elif s == "Cube":
        result += 6
    elif s == "Octahedron":
        result += 8
    elif s == "Dodecahedron":
        result += 12
    elif s == "Icosahedron":
        result += 20
        
    # result += s.count('Tetrahedron') * 4 + s.count('Cube') * 6 + s.count('Octahedron') * 8 + s.count('Dodecahedron') * 12 + s.count('Icosahedron') * 20
print(result)