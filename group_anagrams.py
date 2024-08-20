class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        anagram_key = {}
        for word in strs:
            for char in word:
                if anagram_key:
                    if char in anagram_key:
                        anagram_key[char] += 1
                    else:
                        anagram_key[char] = 1
                else:
                    anagram_key[char] = 1
            this_key = frozenset(sorted(anagram_key.items()))
            anagram_key = {}
            if this_key in anagram_groups.keys():
                anagram_groups[this_key].append(word)
            else:
                anagram_groups[this_key] = [word]

        return list(anagram_groups.values())
