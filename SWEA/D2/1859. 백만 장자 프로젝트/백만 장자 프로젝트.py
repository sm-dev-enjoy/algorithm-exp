import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split())) 
    
    total_profit = 0
    max_price = 0
    
    for price in reversed(prices):
        if max_price <= price:
            max_price = price
        else:
            total_profit += (max_price - price)
    
    print(f'#{test_case} {total_profit}')
