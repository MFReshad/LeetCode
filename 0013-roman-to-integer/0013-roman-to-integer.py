class Solution:
    def romanToInt(self, s: str) -> int:
        romanInt = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        total = 0
        i = 0

        if len(s) <= 15 and 1<=len(s):
            while i<len(s):
                if i+1 < len(s) and romanInt[s[i]] < romanInt[s[i+1]]:
                    total -= romanInt[s[i]]
                else:
                    total += romanInt[s[i]]
                i+=1
            return total
            
