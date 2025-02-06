def find_gcd(a, b):
    for x in range(1, min(a, b) + 1):
        if a % x == 0 and b % x == 0:
            gcd = x
    return gcd
print(find_gcd(15, 25))