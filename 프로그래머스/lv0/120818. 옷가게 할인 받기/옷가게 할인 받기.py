def solution(price):
    price_num = price // 100000

    
    if price_num >= 5:
        price *= 0.8
    elif price_num>=3:
        price *= 0.9
    elif price_num>=1:
        price *= 0.95

    return int(price)