class Solution:
    def romanToInt(self, s: str) -> int:
        translate_dict = {'I': 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M': 1000}
        value = 0
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX').replace('CD', 'CCCC').replace('CM', 'DCCCC')
        for i in s:
            value += translate_dict[i]
        return value
