def special_case(l):
    return pow(l + pow(l, 2), 0.5)
 
a, b  = map(float, input().split())

Xa = special_case(a)
Xb = special_case(b)

print(160 + 40 * pow(Xa, 2))
print(128 + 40 * pow(Xb, 2))
