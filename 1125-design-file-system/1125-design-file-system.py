class FileSystem:

    def __init__(self):
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths:
            return False
        if len(path.split("/")) == 2:
            self.paths[path] = value
            return True
        arr = path.split("/")
        prefix = "/".join(arr[:len(arr) - 1])
        if prefix in self.paths:
            self.paths[path] = value
            return True
        return False

    def get(self, path: str) -> int:
        if path in self.paths:
            return self.paths[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)