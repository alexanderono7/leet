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
                    print("(" + str(x) + "," + str(y) + ")")
                    length = 1 # length variable for coordinate instance 
                    path = [[-1 for j in range(y_length)] for i in range(x_length)] # matrix that tracks which order of the path & which squares have been visited.
                    length = search(x, y, matrix, length, path)
                    if(length > max_length):
                        max_length = length
            return max_length

# Return longest strictly-increasing path starting from (x,y). Works recursively.
def search(x, y, matrix: List[List[int]], length, path: List[List[int]]):
    saved_path = path
    x_length = len(matrix)
    y_length = len(matrix[0])
    path = [[-1 for j in range(y_length)] for i in range(x_length)] # matrix that tracks which order of the path & which squares have been visited.
    path[x][y] = length
    path_length = 1
    for f in path:
        print(f)
    print("")
    # Check adjacent boxes
    if(y-1 in range(0, len(matrix[0])) and path[x][y-1] == -1 and matrix[x][y-1] > matrix[x][y]):
        print("LEFT")
        path_length = search(x, y-1, matrix, path[x][y]+1, path)
        if(path_length > length):
            length = path_length
    if(y+1 in range(0, len(matrix[0])) and path[x][y+1] == -1 and matrix[x][y+1] > matrix[x][y]):
        print("RIGHT")
        path_length = search(x, y+1, matrix, path[x][y]+1, path)
        if(path_length > length):
            length = path_length
    if(x-1 in range(0, len(matrix)) and path[x-1][y] == -1 and matrix[x-1][y] > matrix[x][y]):
        print("UP")
        path_length = search(x-1, y, matrix, path[x][y]+1, path)
        if(path_length > length):
            length = path_length
    if(x+1 in range(0, len(matrix)) and path[x+1][y] == -1 and matrix[x+1][y] > matrix[x][y]):
        print("DOWN")
        path_length = search(x+1, y, matrix, path[x][y]+1, path)
        if(path_length > length):
            length = path_length
    print("RETURN'D (" + str(length) + ")")
    return length

foo = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
matrix = [[7,6,1,1],[2,7,6,0],[1,3,5,1],[6,6,3,2]]
print("\n"*9)
print(foo.longestIncreasingPath(matrix))
print("finale^")
