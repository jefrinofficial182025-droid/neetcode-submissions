class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1 
        while top<=bottom : 
            middlerow = top + (bottom-top)//2
            if target>matrix[middlerow][-1]: 
                top = middlerow + 1
            elif target<matrix[middlerow][0]:
                bottom = middlerow - 1
            else: 
                break 
        if not(top<=bottom): 
            return False
        middlerow = top + (bottom-top)//2
        left, right = 0, cols-1
        while left<=right: 
            m= left + (right-left)//2
            if matrix[middlerow][m]>target: 
                right = m-1 
            elif matrix[middlerow][m]<target: 
                left = m+1 
            else : 
                return True
        return False