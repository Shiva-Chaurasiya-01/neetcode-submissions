class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map ={}

        for ch in s :
            if ch in hash_map :
                hash_map[ch] += 1
            else :
                hash_map[ch] = 1
        
        for ch in t :
            if ch in hash_map:
                hash_map[ch] -= 1
            else : 
                return False

        for key in hash_map.keys() :
            if hash_map[key] != 0 :
                return False
        return True