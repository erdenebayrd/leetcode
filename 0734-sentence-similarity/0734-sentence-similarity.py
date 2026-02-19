class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        similar = defaultdict(set)
        for word in sentence1:
            similar[word].add(word)
        for word in sentence2:
            similar[word].add(word)
        for u, v in similarPairs:
            similar[u].add(v)
            similar[v].add(u)
        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word2 not in similar[word1]:
                return False
        return True