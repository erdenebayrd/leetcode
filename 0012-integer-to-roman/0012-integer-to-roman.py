class Solution:
    def intToRoman(self, num: int) -> str:
        """
            Symbol	Value
            I	    1
            V	    5
            X	    10
            L	    50
            C	    100
            D	    500
            M	    1000

            we can split those 7 different symbols into 2 different group

            ----- group 1 ------
            Symbol	Value power of 10
            I	    1.     0
            X	    10.    1
            C	    100    2
            M	    1000.  3

            ----- group 2 ------
            Symbol	Value power of 10
            V	    5     0
            L	    50    1
            D	    500.  2

            function(decimal, powerOfTen)
                case 1
                decimal is 4 or 9
                    case 1.1
                        decimal is 4
                        powerOfTen index from group number 1 and concanate power of ten index from group number 2
                    case 1.2 
                        decimal is 9
                        power of ten index from group number 1 and power of ten + 1 index from group number 1, concanate them

                case 2 
                decimal is 5
                    I can just use power of ten index from group number 2
                case 3
                others 1, 2, 3, 6, 7, 8
                    case 3.1 -> 1, 2, 3
                    power of ten index from group number 1 and concanate decimal times the character

                    case 3.2 -> 6, 7, 8
                    power of ten index from group number 2 then plus the number - 5 times pwoer of ten index from group number 1
        """

        # time: O(log(n))
        # space: O(log(n))
        # method: simulation

        group1 = ["I", "X", "C", "M"]
        group2 = ["V", "L", "D"]

        def toRoman(decimal: int, power: int) -> int:
            if decimal == 4 or decimal == 9: # case 1
                if decimal == 4:
                    # powerOfTen index from group number 1 and concanate power of ten index from group number 2
                    return group1[power] + group2[power]
                else: # decimal is 9
                    # power of ten index from group number 1 and power of ten + 1 index from group number 1, concanate them
                    return group1[power] + group1[power + 1]
            elif decimal == 5: # case 2
                return group2[power]
            else: # case 3
                if decimal <= 3:
                    # power of ten index from group number 1 and concanate decimal times the character
                    return group1[power] * decimal
                else:
                    # power of ten index from group number 2 then plus the number - 5 times pwoer of ten index from group number 1
                    return group2[power] + group1[power] * (decimal - 5)
        
        s = str(num)
        n = len(s)
        result = ""
        for i in range(n):
            result += toRoman(int(s[i]), n - 1 - i)
        return result