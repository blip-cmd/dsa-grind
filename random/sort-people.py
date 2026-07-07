class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    #1st thought
    #make a dictionary and sort by keys(heights)
	order = sorted(list(zip(heights,names),reverse=True))
	return [_[1] for _ in order]