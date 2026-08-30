n = input()
dat = input().split()

prices = [int(n) for n in dat]

prices.sort()

if len(prices) != 3:
    dif = prices[-2] - prices[1]

    print(dif)
    exit()

case_1 = prices[1] - prices[2]
case_2 = prices[0] - prices[1]

print(max(case_1, case_2))
