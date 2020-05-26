def check_if_enough_coins(_coins, _coin_list):
    temporary_coins = dict(_coins)
    for coin in _coin_list:
        if temporary_coins[coin] > 0:
            temporary_coins[coin] -= 1
        else:
            return False
    return True


def calculate_optimal_solution(_coins, _change):
    coin_list = []
    possible_change = []
    for coin in _coins:
        possible_change.append([coin])
        coin_list.append(coin)
    while True:
        new_possible_change = []
        unique_list = []
        for possibility in possible_change:
            for coin in coin_list:
                new_possibility = possibility + [coin]
                new_possibility.sort()
                if new_possibility not in unique_list:
                    unique_list.append(new_possibility)
                    if check_if_enough_coins(_coins, new_possibility):
                        sum = 0
                        for _coin in new_possibility:
                            sum += _coin
                        if sum == _change:
                            return new_possibility
                        new_possible_change.append(new_possibility)
        if not new_possible_change:
            return new_possible_change
        possible_change = new_possible_change[:]


coins = {
    1: 10,
    20: 3,
    50: 3}

change = 60

optimal_change = calculate_optimal_solution(coins, change)
print(optimal_change)