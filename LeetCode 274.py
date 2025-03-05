class Solution:
    def hIndex(self, citations: List[int]) -> int:

        Index = 0
        citations.sort(reverse=True)
        num = len(citations)

        if sum(citations) == 0:
            return Index
        else:
                
            for i in range(num):
                if citations[i] > Index:
                    Index += 1

            return Index
        