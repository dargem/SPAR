"""
Hidden sequence is easier than it seems just uses 3 pointers
The 2 pointers that agree get advanced, the pointer that degrees stays still
"""

a = input()
b = input()
c = input()

a_it = 0
b_it = 0
c_it = 0

winners = ""

while (a_it < len(a) or b_it < len(b) or c_it < len(c)):
    if a_it < len(a) and b_it < len(b) and a[a_it] == b[b_it]:
        # agreement that c won
        a_it += 1
        b_it += 1
        winners += "3"
    elif a_it < len(a) and c_it < len(c) and a[a_it] == c[c_it]:
        a_it += 1
        c_it += 1
        winners += "2"
    elif b_it < len(b) and c_it < len(c) and b[b_it] == c[c_it]:
        b_it += 1
        c_it += 1
        winners += "1"

print(winners)
