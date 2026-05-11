from collections import deque

class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        result = [float('inf')] * n
        # 1 exit, 0 enter
        entering, exiting = deque(), deque()
        index = 0
        current_time = arrival[0]
        prev = -1 # none of exit or enter

        while index < n:
            while index < n and current_time >= arrival[index]:
                if state[index] == 1: # exiting
                    exiting.append(index)
                else: # entering
                    entering.append(index)
                index += 1

            if not entering and not exiting and index < n:
                current_time = arrival[index]
                prev = -1 # none of enter or exit

            if entering or exiting:
                if prev == -1: # no prev second record
                    if exiting:
                        idx = exiting.popleft()
                        result[idx] = current_time
                        current_time += 1
                        prev = 1
                    elif entering:
                        idx = entering.popleft()
                        result[idx] = current_time
                        current_time += 1
                        prev = 0
                else: # existing record of prev second
                    if prev == 1: # exiting
                        if exiting:
                            idx = exiting.popleft()
                            result[idx] = current_time
                            current_time += 1
                            prev = 1
                        elif entering:
                            idx = entering.popleft()
                            result[idx] = current_time
                            current_time += 1
                            prev = 0
                    else: # entering, prev must be 0
                        if entering:
                            idx = entering.popleft()
                            result[idx] = current_time
                            current_time += 1
                            prev = 0
                        elif exiting:
                            idx = exiting.popleft()
                            result[idx] = current_time
                            current_time += 1
                            prev = 1
        
        while entering or exiting:
            if prev == -1: # no prev second record
                if exiting:
                    idx = exiting.popleft()
                    result[idx] = current_time
                    current_time += 1
                    prev = 1
                elif entering:
                    idx = entering.popleft()
                    result[idx] = current_time
                    current_time += 1
                    prev = 0
            else: # existing record of prev second
                if prev == 1: # exiting
                    if exiting:
                        idx = exiting.popleft()
                        result[idx] = current_time
                        current_time += 1
                        prev = 1
                    elif entering:
                        idx = entering.popleft()
                        result[idx] = current_time
                        current_time += 1
                        prev = 0
                else: # entering, prev must be 0
                    if entering:
                        idx = entering.popleft()
                        result[idx] = current_time
                        current_time += 1
                        prev = 0
                    elif exiting:
                        idx = exiting.popleft()
                        result[idx] = current_time
                        current_time += 1
                        prev = 1
        return result