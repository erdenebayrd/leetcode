class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.seen = set(dictionary)
        self.abbreviations = {}
        for word in self.seen:
            word = self.abbreviation(word)
            if word not in self.abbreviations:
                self.abbreviations[word] = 0
            self.abbreviations[word] += 1
    
    def abbreviation(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word: str) -> bool:
        if self.abbreviation(word) not in self.abbreviations or (word in self.seen and self.abbreviations[self.abbreviation(word)] == 1):
            return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)