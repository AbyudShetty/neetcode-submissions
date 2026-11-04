class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        seen = {}
        seen["".join(sorted(strs[0]))] = [strs[0]] 

        for value in strs[1:]: 

            key = "".join(sorted(value))
            
            if key in seen:
                seen[key].append(value)
            else:
                seen[key] = [value]

        return list(seen.values())