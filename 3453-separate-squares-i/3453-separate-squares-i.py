class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        totalArea = 0
        for _, _, l in squares:
            totalArea += l * l
        
        def check(yhat: float) -> bool:
            upArea = 0
            for _, y, l in squares:
                if yhat <= y:
                    upArea += l * l
                elif yhat <= y + l: # cut somewhere in mid
                    upArea += (y + l - yhat) * l
            return upArea <= totalArea / 2

        
        lo, hi = 0, 2e9
        eps = 1e-5
        while lo + eps < hi:
            md = (lo + hi) / 2
            if check(md):
                hi = md
            else:
                lo = md

        return hi