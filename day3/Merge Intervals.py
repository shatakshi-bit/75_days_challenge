class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals==[]:
            return []
        result=[]
        intervals.sort()
        for intervals in intervals:
            if result==[] or result[-1][1]<intervals[0]:
                result.append(intervals)
            else:
                result[-1][1]=max(result[-1][1],intervals[1])
        return result
            
       
        
            