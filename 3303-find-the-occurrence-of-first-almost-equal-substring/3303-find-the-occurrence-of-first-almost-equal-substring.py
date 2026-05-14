class Solution:
    def minStartingIndex(self, text: str, pattern: str) -> int:
        """
        this problem is asking to find first occurence of pattern in given text
        but one special thing here is almost equal
        what does it mean
        if there is at most one character is different in comparison, we can consider it almost identical

        okay
        so we can think in this way

        lets assume we already know how many characters of pattern is matched starting at "i" index of given text
        suffix as well

        for example:
            
            text = b a a b a a c
            prefix 0 2 1 0 2 1 0
            
            pattern = a a x b a

            what does this prefix number mean?
            second "a" character
            prefix number here is 2 right
            meaning 
            if I start to match pattern with given text STARTING from here, what is the longest match
            thats the what number says

            
        now lets assume we already know how many characters of pattern is matched starting at "i" index of given text in OPPOSITE direction (right to left)

        for example:
                   V
            text = b a a c b a a c
            prefix 0 2 1 0 0 2 1 0
            suffix 0 2 1 0 0 2 1 0

            pattern = a a x b a
                              ^
        
        if we already know this prefix and suffix information
        we can solve this problem by this way

        the length of the pattern here is 5

        we can start from left to right of the prefix array
        how many characters are same with the pattern starting from this index "i"
        we easily calculate how many characters from suffix at index "j" is needed

        for example:
                   
            text = b a a c b a a c
                   0 1 2 3 4 5 6 7

                     i         
            prefix 0 2 1 0 0 2 1 0
                           
                             j
            suffix 0 2 1 0 0 2 1 0

            j = i + len(pattern) - 1

            if abs(prefix[i] + suffix[j] - len(pattern)) <= 1
                this is condition is TRUE
                we can say we found the almost identical substring of given text starting from index "i"
                since we need to find first index of the given text
                we can just return the index and end the programm

                      a a c b a
                      2
                              2
  
            pattern = a a x b a
        
            now if we know the prefix and suffix we mentioned above
            we can just solve this problem by O(N) N is the length of given text

            most important part is how we calculate this prefix suffix arrays in linear time complexity

            here we can use Z-Function

            which gives us a how many characters are same from the string prefix

            for example:

                a a b a a b a a
                8 1 0 5 1 0 2 1

            this Z function algo works linear time

           how we can transform the given problem to this Z function

           we can just concat
           the pattern with given string
                                  
                                  V
          s  =.  pattern + "#" + text
          zvalues [   1 0.2 9 ... 7 2  .  ]

          suffix array that we talked earlier

          r = reversed(pattern) + "#" + reversed(text)
          zvalues of r string is the suffix array

          zvalues of the s string is the prefix array

          now we can solve this problem in linear time

          the most important thing here is 
          how this zvalues array built = how this z function algorithm works

          lets assume we are building zvalues (z function) on given string "text"

          the trivial way is to compare every index 'i' with 0th index if those are equal goes right by 1 until it reaches different character of end of the string
          but here is the thing

          we can just keep track of the RIGHT most index of the z values
          left is the index "i"
          right is the ending index of (i + z_values[i] - 1) the longest identical string starting from i with the prefix of given string "text"
          when we calculate z value of the 'i' posittion
          if i > right
            that means
            we can just run the trivial algorightm
            which is just check text[i] == text[0]
            if it is equal (same) we increment the zvalue of index "i" until it reaches different character of end of the string
            then we update right
            we now know the zvalue of index "i"
            i + zvalue[i] - 1 is the right index (ending at here)
            left is just simply "i" (starting from index "i"), end at right index
          otherwise (i <= right)
            we have some identical index from around beginning of the given text
            which is just i - left
            we already calculate zvalue of i - left 'th position
            we can use this zvalue here
            zvalue[i] = min(zvalue[i - left], right - i + 1),  i means starting from i and end here at "right"
            until now we only saw the string until index "right"
            after right index this might be same characters like we may need to extend zvalue[i]
            how to extend
            just run the trivial algorithm
            total time woudl be linear O(len(text) + len(pattern) + 1) if we add "$" or "#"
        """

        def z_function(text: str) -> list:
            n = len(text)
            left = right = -1
            z_values = [0] * n
            z_values[0] = n
            for i in range(1, n):
                if i <= right:
                    z_values[i] = min(z_values[i - left], right - i + 1)
                while i + z_values[i] < n and text[z_values[i]] == text[i + z_values[i]]:
                    z_values[i] += 1
                
                if i + z_values[i] - 1 > right:
                    right = i + z_values[i] - 1
                    left = i
            return z_values

        prefix = z_function(pattern + "$" + text)
        suffix = z_function(pattern[::-1] + "$" + text[::-1])
        suffix = suffix[:len(pattern) + 1] + suffix[len(pattern) + 1:][::-1]
        # print(prefix)
        # print(suffix)
        n = len(prefix)
        for i in range(len(pattern) + 1, n):
            j = i + len(pattern) - 1
            if prefix[i] == len(pattern): # true identical (not almost)
                return i - len(pattern) - 1
            if j < n and abs(prefix[i] + suffix[j] - len(pattern)) <= 1:
                return i - len(pattern) - 1
        return -1