
MONEY_LIST = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
TOTAL_MONEY_LIST = [73735, 9561, 4950, 600, 70590, 117440, 2350, 0, 52318, 12524, 55220, 510546, -6632, 523871]

def cal_minimum_number(total_money):
    
    dict_result = {}
    
    for money in MONEY_LIST:
        count = 0
        
        while total_money >= money:
            total_money -= money
            count += 1

        dict_result[money] = count
    
    return dict_result


if __name__ == '__main__':
    for total_money in TOTAL_MONEY_LIST:
        result = cal_minimum_number(total_money)
        print(total_money, result)