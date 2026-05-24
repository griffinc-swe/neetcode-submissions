class Solution:
    
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for i in range(len(strs)):
            s = strs[i]
            alph = [0] * 26
            for j in range(len(s)):
                k = ord(s[j]) - ord('a')
                alph[k] = alph[k] + 1
            alph = tuple(alph)
            if alph not in dct:
                dct[alph] = [s]
            else:
                dct[alph].append(s)
        res = []
        for val in dct.values():
            res.append(val)
        return res