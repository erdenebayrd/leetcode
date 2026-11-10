class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # time: O(n log k * log k) n is len of arrival
        # space: O(k)
        # method: segment tree

        st = [0] * 4 * k
        n = len(arrival)
        count = [0] * k

        def __find_sub(pointer: int, left: int, right: int, value: int) -> int:
            if left > right or st[pointer] > value:
                return -1
            if left == right:
                return right # index

            left_index = __find_sub(2 * pointer, left, (left + right) // 2, value)
            if left_index != -1:
                return left_index
            right_index = __find_sub(2 * pointer + 1, (left + right) // 2 + 1, right, value)
            return right_index


        def __find(pointer: int, left: int, right: int, query_left: int, query_right: int, value: int) -> int:
            if left > right or left > query_right or right < query_left:
                return -1
            if query_left <= left and right <= query_right:
                return __find_sub(pointer, left, right, value)
            left_index = __find(2 * pointer, left, (left + right) // 2, query_left, query_right, value)
            right_index = __find(2 * pointer + 1, (left + right) // 2 + 1, right, query_left, query_right, value)
            if left_index == -1:
                return right_index
            return left_index

        def find(left: int, right: int, value: int) -> int:
            return __find(1, 0, k - 1, left, right, value)
            
        
        def __update(pointer: int, left: int, right: int, index: int, value: int) -> None:
            if left > right or left > index or right < index:
                return
            if left == index == right:
                st[pointer] = value
                return
            __update(2 * pointer, left, (left + right) // 2, index, value)
            __update(2 * pointer + 1, (left + right) // 2 + 1, right, index, value)
            st[pointer] = min(st[2 * pointer], st[2 * pointer + 1])

        def update(index: int, value: int) -> None:
            __update(1, 0, k - 1, index, value)

        for i in range(n):
            left = i % k
            right = k - 1
            index = find(left, right, arrival[i])
            if index != -1:
                update(index, arrival[i] + load[i])
                count[index] += 1
            else:
                left = 0
                right = (i % k) - 1
                index = find(left, right, arrival[i])
                if index != -1:
                    update(index, arrival[i] + load[i])
                    count[index] += 1
        
        max_count = max(count)
        result = []
        for i in range(k):
            if max_count == count[i]:
                result.append(i)
        return result