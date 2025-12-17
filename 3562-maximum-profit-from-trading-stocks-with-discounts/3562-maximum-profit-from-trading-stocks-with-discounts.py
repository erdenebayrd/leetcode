class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # dp[n][2][budget + 1]
        inf = float("inf")
        dp = [[[-inf] * (budget + 1) for _ in range(2)] for _ in range(n + 1)]
        # adj[n + 1]
        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)
        
        def combine_two(combined: List[int], current: List[int]) -> List[int]:
            assert len(combined) == budget + 1 and len(current) == budget + 1
            res = [-inf] * (budget + 1)
            for total_cost_for_BOTH_TWO_children in range(budget + 1):
                # max profit for given cost """total_cost_for_BOTH_TWO_children"""
                cur = res[total_cost_for_BOTH_TWO_children]
                # dividing TOTAL cost into 2 children by every ways
                for cost_for_child_ONE in range(total_cost_for_BOTH_TWO_children + 1):    
                    cost_for_child_TWO = total_cost_for_BOTH_TWO_children - cost_for_child_ONE
                    # total_cost_for_BOTH_TWO_children = cost_for_child_ONE + cost_for_child_TWO
                    # 1. cost_for_child_ONE
                    # 2. cost_for_child_TWO
                    cur = max(cur, combined[cost_for_child_ONE] + current[cost_for_child_TWO])
                res[total_cost_for_BOTH_TWO_children] = cur
            return res

        def combine_children(children: List[int]): # 2 x (budget + 1) array
            assert len(children) > 0
            # NO discount
            no_discount_combined = dp[children[0]][0] # first child with no discount
            for idx in range(1, len(children)):
                no_discount_combined = combine_two(no_discount_combined, dp[children[idx]][0])
            # Discount
            discount_combined = dp[children[0]][1] # first child with Discount
            for idx in range(1, len(children)):
                discount_combined = combine_two(discount_combined, dp[children[idx]][1])
            return [no_discount_combined, discount_combined]
                
        
        def merge_with_parent(parent_node: int, combined_children: List[List[int]]): # 2 x (budget + 1) array
            # for parent_node which is starting from 1 NOT 0
            full_price = present[parent_node - 1]
            half_price = full_price // 2
            profit_with_full_price = future[parent_node - 1] - full_price
            profit_with_half_price = future[parent_node - 1] - half_price
            
            # WITHOUT Discount from PARENT of parent_node
            without_discount = [-inf] * (budget + 1) # 0th row of parent_node

                # option 1: NOT buy, we can ONLY use combined_children's 0th row as the 0 means parent did NOT buy
            for total_cost_for_PARENT_NODE_and_children in range(budget + 1):
                # since parent_node didn't buy anything, the total given cost will be used only for it's children (combined) / pass given budget into combined_children
                not_buy_profit = combined_children[0][total_cost_for_PARENT_NODE_and_children]
                # option 2: Buy, we can use combined_children's BOTH 0th and 1st rows as if parent BOUGHT children can USE or NOT USE the Discount
                bought_profit = -inf # if total_cost_for_PARENT_NODE_and_children is NOT enough for given present of parent_node
                if total_cost_for_PARENT_NODE_and_children >= full_price: # here we ONLY use full_price, since wer are on WITHOUT Discount CONDITION
                    cost_for_combined_children_after_bought_by_parent = total_cost_for_PARENT_NODE_and_children - full_price
                    bought_profit = max(bought_profit, profit_with_full_price + combined_children[0][cost_for_combined_children_after_bought_by_parent]) # combined children NOT use the parent_node's DISCOUNT
                    bought_profit = max(bought_profit, profit_with_full_price + combined_children[1][cost_for_combined_children_after_bought_by_parent]) # combined children DID use the parent_node's DISCOUNT
                without_discount[total_cost_for_PARENT_NODE_and_children] = max(not_buy_profit, bought_profit)
                # print("total_cost_for_PARENT_NODE_and_children", total_cost_for_PARENT_NODE_and_children)
                # print("not_buy_profit", not_buy_profit)
                # print("bought_profit", bought_profit)
                # print("full_price", full_price)
                # print("-" * 100)

            # WITH Discount from PARENT of parent_node
            with_discount = [-inf] * (budget + 1) # 1st row of parent_node
                # option 1: NOT buy, we can ONLY use combined_children's 0th row as the 0 means parent did NOT buy
            for total_cost_for_PARENT_NODE_and_children in range(budget + 1):
                # since parent_node didn't buy anything even has a chance to use DISCOUNT, the total given cost will be used only for it's children (combined) / pass given budget into combined_children
                not_buy_profit = combined_children[0][total_cost_for_PARENT_NODE_and_children]
                # option 2: Buy, we can use combined_children's BOTH 0th and 1st rows as if parent BOUGHT children can USE or NOT USE the Discount
                bought_profit = -inf # if total_cost_for_PARENT_NODE_and_children is NOT enough for given present of parent_node
                if total_cost_for_PARENT_NODE_and_children >= half_price: # here we use half_price, since wer are on WITH Discount CONDITION
                    cost_for_combined_children_after_bought_by_parent = total_cost_for_PARENT_NODE_and_children - half_price
                    bought_profit = max(bought_profit, profit_with_half_price + combined_children[0][cost_for_combined_children_after_bought_by_parent]) # combined children NOT use the parent_node's DISCOUNT
                    bought_profit = max(bought_profit, profit_with_half_price + combined_children[1][cost_for_combined_children_after_bought_by_parent]) # combined children DID use the parent_node's DISCOUNT
                with_discount[total_cost_for_PARENT_NODE_and_children] = max(not_buy_profit, bought_profit)
            return [without_discount, with_discount]
        
        def init(cur_node: int) -> None:
            # calculate: dp[child][0 -> 1][0 -> budget + 1]
                # 1. No discount / Full price
                    # no buy
            dp[cur_node][0][0] = 0
                    # buy
            cost = present[cur_node - 1]
            profit = future[cur_node - 1] - cost
            dp[cur_node][0][cost] = profit
                # 2. Discount / Half price
                    # no buy
            dp[cur_node][1][0] = 0
                    # buy
                        # even has chance to use discount, child have a choice to NOT use discount
            cost = present[cur_node - 1]
            dp[cur_node][1][cost] = profit
                        # using discount
            cost //= 2
            profit = future[cur_node - 1] - cost
            dp[cur_node][1][cost] = profit
            dp[cur_node][1][cost] = profit

        def dfs(cur_node: int):
            init(cur_node)
            for child in adj[cur_node]:
                dfs(child)
            
            if len(adj[cur_node]) > 0: # at least 1 child, NOT Leaf
                combined_dp = combine_children(adj[cur_node])
                # print("Example 1, expected node 1:", cur_node)
                # print(combined_dp[0])
                # print(combined_dp[1])
                # replacing init(cur_node) if cur_node is not Leaf node
                dp[cur_node] = merge_with_parent(cur_node, combined_dp)

        dfs(1)
        # print(dp[2][0])
        # print(dp[2][1])
        # print(dp[1][0])
        return max(dp[1][0])