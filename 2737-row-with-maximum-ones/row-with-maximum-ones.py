class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
         max_count = 0
         row_index = 0
         for i in range(len(mat)):
            count = mat[i].count(1)

            if count > max_count:
                max_count = count
                row_index = i

         return [row_index, max_count]