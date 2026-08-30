nums = input().split()
filt = [int(num) for num in nums]

price, refund, total = filt

total_bottles_bought = 0
while total >= price:
    num_buy = total // price
    total -= num_buy * price

    total_bottles_bought += num_buy

    refund_money = refund * num_buy
    total += refund_money

print(total_bottles_bought)