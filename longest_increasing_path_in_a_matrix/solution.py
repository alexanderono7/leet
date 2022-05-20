from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if(matrix == None):
            return None
        else:
            max_length = 1
            x_length = len(matrix)
            y_length = len(matrix[0])
            for x in range(x_length):
                for y in range(y_length):
                    length = 1 # length variable for coordinate instance 
                    path = [[-1 for j in range(y_length)] for i in range(x_length)] # matrix that tracks which order of the path & which squares have been visited.
                    print("x: " + str(x)) 
                    print("y: " + str(y))
                    length = self.search(x, y, matrix, length, path)
                    if(length > max_length):
                        max_length = length
            return max_length

    # Return longest strictly-increasing path starting from (x,y). Works recursively.
    def search(self, x, y, matrix: List[List[int]], length, path: List[List[int]]):
        # Check adjacent boxes
        path[x][y] = length
        for f in path:
            print(f)
        print("\n")
        if(y-1 in range(0, len(matrix[0])) and path[x][y-1] == -1 and matrix[x][y-1] > matrix[x][y]):
            path_length = self.search(x, y-1, matrix, length+1, path)
            print("UP")
        if(y+1 in range(0, len(matrix[0])) and path[x][y+1] == -1 and matrix[x][y+1] > matrix[x][y]):
            path_length = self.search(x, y+1, matrix, length+1, path)
            print("DOWN")
        if(x-1 in range(0, len(matrix)) and path[x-1][y] == -1 and matrix[x-1][y] > matrix[x][y]):
            path_length = self.search(x-1, y, matrix, length+1, path)
            print("LEFT")
        if(x+1 in range(0, len(matrix)) and path[x+1][y] == -1 and matrix[x+1][y] > matrix[x][y]):
            path_length = self.search(x+1, y, matrix, length+1, path)
            print("RIGHT")
        print("RETURN'D (" + str(length) + ")")
        return length


foo = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(foo.longestIncreasingPath(matrix))
