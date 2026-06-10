class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        res=list()
        i=1
        while i*i<=area:
            if area%i==0:
                res.append(i)
                res.append(area//i)
            i+=1
        res.sort()
        a=len(res)
        return [res[a//2],res[a//2-1]]