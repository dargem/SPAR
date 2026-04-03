needed = int(input())

bits = 1

while (pow(2, bits) - 1 < needed):
    bits *=2

if (bits == 1):
    print("1 bit")
else:
    print(f"{bits} bits")