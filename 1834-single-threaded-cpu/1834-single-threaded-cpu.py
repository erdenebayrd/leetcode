import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        lets think in this way
        we have tasks which contains 2 information
        1. when this task will be available to be processed
        2. how much time it will take to done 
        we need to make sure available time is non-decreasing order if it is not, we can sort it by available time

        current_time starts from 0'th second
        we need to have a 2 list or some other Data structure
            * available to run tasks
            * unavailable tasks (at the moment)

        if the cpu is idle right now,
            we need to increase the current time to equal to first available time of the not available tasks
        when current time is greater than or equal to some the unavailable tasks we need to move those tasks with available time is lower or equal to current time to available tasks
        then process the first available tasks by one by one.

        then we will update the current time to finish time of the current processing tasks

        basically 
        we have 2 heap
            * available tasks
            * unavailable tasks
        current time = 0

        if available tasks is empty
            we need to check unavailable tasks
                if it is empty.
                    we already done all tasks
                otherwise
                    we need to update the current time to first unavailable tasks (it's enque time)
        otherwise
            run from available task (first task on the top of heap)
        """
        # time: O(N log N) N is the total number of tasks
        # space: O(N)
        # method: min heap

        n = len(tasks)
        available_tasks = []
        unavailable_tasks = [(tasks[index][0], tasks[index][1], index) for index in range(len(tasks))] # first value is enque time, second value process time, third value is index of the tasks
        heapq.heapify(unavailable_tasks) # O(N log N)
        current_time = 0
        result = []
        
        while available_tasks or unavailable_tasks:
            while unavailable_tasks and current_time >= unavailable_tasks[0][0]:
                enqueue_time, process_time, task_index = heapq.heappop(unavailable_tasks)
                heapq.heappush(available_tasks, (process_time, task_index))

            if available_tasks:
                process_time, task_index = heapq.heappop(available_tasks)
                result.append(task_index)
                current_time += process_time
            else: # no available tasks at the moment
                enqueue_time, _, _ = unavailable_tasks[0]
                current_time = enqueue_time
        
        return result