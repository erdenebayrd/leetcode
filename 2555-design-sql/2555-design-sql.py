class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.table = defaultdict(lambda: -1)
        for idx, name in enumerate(names):
            self.table[name] = {"columns": columns[idx], "data": defaultdict(list), "curRow": 0}

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.table or self.table[name]["columns"] != len(row):
            return False
        self.table[name]["curRow"] += 1
        currentRow = self.table[name]["curRow"]
        self.table[name]["data"][currentRow] = row
        return True

    def rmv(self, name: str, rowId: int) -> None:
        # init: [["one","two","three"],[2,3,1]]
        # ins: ["two",["first","second","third"]]
        # sel: ["two",1,3]
        [["two",["fourth","fifth","sixth"]],["two"],["two",1],["two",2,2],["two"]]
        if name in self.table and rowId in self.table[name]["data"]:
            self.table[name]["data"].pop(rowId)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        columnId -= 1
        if name not in self.table or rowId not in self.table[name]["data"] or columnId >= len(self.table[name]["data"][rowId]):
            return "<null>"
        return self.table[name]["data"][rowId][columnId]

    def exp(self, name: str) -> List[str]:
        if name not in self.table:
            return []
        
        res = []
        for key in self.table[name]["data"]:
            res.append(",".join([str(key), ",".join(self.table[name]["data"][key])]))
        return res


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)