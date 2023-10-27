

# from queue import PriorityQueue


# class Currency:
#     def __init__(self, cur_from, cur_to, price):
#         self.cur_from = cur_from
#         self.cur_to = cur_to
#         self.price = price

#     def __gt__(self, other):
#         return self.cur_to > other.cur_to


# pairs = int(input())
# currencies = {}

# for _ in range(pairs):
#     cur_from, cur_to, price = input().split()
#     exchange_rate = Currency(cur_from, cur_to, float(price))
#     if cur_from not in currencies:
#         currencies[cur_from] = []
#     if cur_to not in currencies:
#         currencies[cur_to] = []
#     currencies[cur_from].append(exchange_rate)

# target = input()


# arbitrage = {currency: float('-inf') for currency in currencies.keys()}

# pq = PriorityQueue()
# path = [target]
# new_arbitrage = 0

# for _ in range(pairs):
#     pq.put((-1, target))
#     while not pq.empty():
#         max_profit, currency = pq.get()
#         if arbitrage[target] != float('-inf'):
#             break
#         sorted_currency_pair = sorted(currencies[currency], key=lambda x: x.price, reverse=True)
#         pair = sorted_currency_pair[0]
#         new_arbitrage = -max_profit * pair.price
#         if new_arbitrage > arbitrage[pair.cur_to]:
#             path.append(pair.cur_to)
#             pq.put((-new_arbitrage, pair.cur_to))
#             arbitrage[pair.cur_to] = new_arbitrage


# if new_arbitrage < 1:
#     arbitrage[target] = 1
#     print('False')
#     [print(f'{key}: {value:.3f}') for key, value in arbitrage.items()]
# else:
#     print('True')
#     print(*path)
