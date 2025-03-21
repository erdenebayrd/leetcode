class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = {}
        n = len(recipes)
        sup = {}
        for el in supplies:
            sup[el] = True
        for _ in range(n):
            for i in range(n):
                if recipes[i] in res:
                    continue
                flag = True
                for el in ingredients[i]:
                    flag &= (el in sup)
                if flag is True:
                    if recipes[i] not in res:
                        res[recipes[i]] = True
                    if recipes[i] not in sup:
                        sup[recipes[i]] = True
        return [key for key in res]