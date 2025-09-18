class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.sl = SortedList([])
        self.taskMap = {}
        for userId, taskId, priority in tasks:
            self.sl.add([priority, taskId, userId])
            self.taskMap[taskId] = (userId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMap[taskId] = (userId, priority)
        self.sl.add([priority, taskId, userId])

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, priority = self.taskMap[taskId]
        self.sl.remove([priority, taskId, userId])
        self.sl.add([newPriority, taskId, userId])
        self.taskMap[taskId] = (userId, newPriority)

    def rmv(self, taskId: int) -> None:
        userId, priority = self.taskMap[taskId]
        self.sl.remove([priority, taskId, userId])
        del self.taskMap[taskId]

    def execTop(self) -> int:
        if len(self.sl) == 0:
            return -1
        _, _, userId = self.sl[-1]
        self.sl.pop(-1)
        return userId


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()