from collections import deque, defaultdict

class Solution:
    def maxAmount(self, initial_currency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        # time: O(V + E)
        # space: O(V + E)
        # method: BFS
        
        def get_rates(currency: str, pairs: list, rates: list) -> dict:
            adj = defaultdict(list)
            m = len(pairs)
            for i in range(m):
                u, v = pairs[i]
                weight = rates[i]
                adj[u].append((v, weight))
                adj[v].append((u, -weight))
            
            rates = {currency: (1, 1)}
            queue = deque([(currency, 1, 1)])
            while queue:
                currency, mul, div = queue.popleft()
                for neighbor, weight in adj[currency]:
                    if neighbor in rates:
                        continue
                    neighbor_mul, neighbor_div = mul, div
                    if weight > 0:
                        neighbor_mul *= weight
                    else:
                        neighbor_div *= -weight
                    rates[neighbor] = (neighbor_mul, neighbor_div)
                    queue.append((neighbor, neighbor_mul, neighbor_div))
            return rates

        result = 1.0
        currency_rates_day1 = get_rates(initial_currency, pairs1, rates1) # day1 rates
        # print(currency_rates_day1)
        currency_rates_day2 = get_rates(initial_currency, pairs2, rates2) # day2 rates
        # print(currency_rates_day2)
        for currency_day2 in currency_rates_day2:
            if currency_day2 not in currency_rates_day1:
                continue
            mul_day1, div_day1 = currency_rates_day1[currency_day2]
            div_day2, mul_day2 = currency_rates_day2[currency_day2]
            # print(currency_day2, mul_day1, mul_day2, div_day1, div_day2)
            result = max(result, mul_day1 * mul_day2 / (div_day1 * div_day2))
        return result