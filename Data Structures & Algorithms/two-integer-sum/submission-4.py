class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = [(i,num) for i,num in enumerate(nums)]
        indexed.sort(key=lambda x: x[1])
        i, j = 0, len(nums)-1
        while i < j:
            if indexed[i][1]+indexed[j][1] == target:
                return [min(indexed[i][0],indexed[j][0]), max(indexed[j][0],indexed[i][0])]
            elif indexed[i][1]+indexed[j][1] < target:
                i+=1
            else:
                j-=1;
                
        return []