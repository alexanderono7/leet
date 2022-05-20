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
                    note("(" + str(x) + "," + str(y) + ")")
                    length = 1 # length variable for coordinate instance 
                    cache = [[-1 for j in range(y_length)] for i in range(x_length)]
                    length = search(x, y, matrix, length, cache)
                    if(length > max_length):
                        max_length = length
            return max_length


# Return longest strictly-increasing path starting from (x,y). Works recursively.
def search(x, y, matrix: List[List[int]], length, cache):
    saved_length = length
    path_length = 1
    for f in cache:
        note(f)
    print("")
    # Check adjacent boxes
    if(y-1 in range(0, len(matrix[0])) and matrix[x][y-1] > matrix[x][y]):
        if(cache[x][y-1] != -1):
            path_length = length
            path_length += cache[x][y-1]
        else:
            path_length = search(x, y-1, matrix, saved_length+1, cache)
        if(path_length > length):
            length = path_length
    path_length = 1
    if(y+1 in range(0, len(matrix[0])) and matrix[x][y+1] > matrix[x][y]):
        if(cache[x][y+1] != -1):
            path_length = length
            path_length += cache[x][y+1]
        else:
            path_length = search(x, y+1, matrix, saved_length+1, cache)
        if(path_length > length):
            length = path_length
    path_length = 1
    if(x-1 in range(0, len(matrix)) and matrix[x-1][y] > matrix[x][y]):
        if(cache[x-1][y] != -1):
            path_length = length
            path_length += cache[x-1][y]
        else:
            path_length = search(x-1, y, matrix, saved_length+1, cache)
        if(path_length > length):
            length = path_length
    path_length = 1
    if(x+1 in range(0, len(matrix)) and matrix[x+1][y] > matrix[x][y]):
        if(cache[x+1][y] != -1):
            path_length = length
            path_length += cache[x+1][y]
        else:
            path_length = search(x+1, y, matrix, saved_length+1, cache)
        if(path_length > length):
            length = path_length
    path_length = 1
    cache[x][y] = length
    return length

def note(string):
    if(switch):
        print(string)

foo = Solution()
matrix = [[8,11,12,6,6,19,16,8,14,15,11,14,12,4,8,4,14,12,1,14,3,12,14,13,9,5,6,16,12,11,2,8,1,2,6,0,17,5],[11,9,12,16,7,6,14,5,0,12,1,19,4,5,18,8,7,11,16,10,3,8,7,13,13,19,6,7,0,10,12,16,18,16,17,17,11,11],[13,1,19,0,0,8,1,6,17,0,18,0,17,0,0,14,7,16,11,8,9,11,2,7,10,1,10,13,11,14,1,0,9,4,18,18,12,1],[1,8,14,11,12,13,16,9,19,3,18,15,1,17,15,7,16,19,7,8,19,12,12,8,3,13,16,13,11,0,5,12,10,0,1,2,8,3],[13,17,2,14,16,11,18,8,12,2,9,15,15,17,0,12,13,2,3,11,0,5,10,12,3,16,10,5,8,13,6,0,3,14,15,15,11,4],[19,11,3,4,15,2,3,19,5,19,2,0,11,9,16,19,14,7,1,13,19,7,13,19,16,13,8,13,16,3,5,14,16,7,18,1,9,5],[10,18,7,11,11,2,1,8,13,1,16,17,13,15,19,19,15,2,3,14,14,11,4,13,9,0,0,0,11,9,19,3,8,4,18,14,8,4],[16,15,18,1,11,18,5,2,8,12,2,7,10,14,17,3,10,6,7,18,3,10,15,1,9,17,10,11,17,10,8,2,11,6,19,19,0,6],[6,7,0,3,3,13,19,15,7,9,4,9,12,10,2,9,17,15,19,9,3,3,16,12,8,13,4,10,16,12,15,17,3,13,1,15,5,6],[10,8,14,17,5,11,11,14,17,13,3,13,18,14,3,2,12,0,16,8,14,18,17,0,2,10,5,8,13,16,4,2,12,4,16,15,0,15],[12,18,19,5,19,14,4,17,10,10,13,14,7,10,5,19,3,7,8,19,9,16,11,11,13,6,16,5,3,4,7,5,19,16,9,7,18,10],[6,4,17,15,10,14,19,13,0,0,1,0,7,11,17,1,10,7,19,2,19,13,15,10,5,10,9,14,14,5,16,6,4,15,15,7,0,4],[2,1,5,17,8,4,19,1,13,19,16,13,2,10,13,13,18,15,2,9,17,4,15,13,13,16,18,13,4,12,2,8,17,4,15,19,2,6],[13,6,19,11,8,16,6,17,1,10,2,6,14,14,0,16,19,17,4,1,13,18,17,18,13,13,3,11,6,9,13,19,5,15,5,11,5,9],[4,4,19,18,4,3,17,18,4,12,19,10,18,14,19,15,0,14,12,1,2,7,18,8,1,11,6,6,8,17,9,15,15,15,8,18,0,2],[14,9,15,8,10,8,7,10,5,15,7,8,8,2,0,3,15,15,8,2,9,16,12,8,7,2,11,9,16,10,2,11,19,18,12,6,17,15],[3,1,8,14,2,16,13,14,2,15,17,15,0,3,13,9,13,16,3,19,9,19,10,1,13,7,11,5,16,8,16,3,1,19,18,17,3,13],[10,3,0,19,0,3,4,3,2,0,14,17,5,17,15,5,11,13,15,13,2,14,5,18,14,8,7,5,4,8,12,0,3,6,2,15,0,15],[0,9,2,3,8,4,9,12,3,18,6,17,10,8,9,10,1,13,7,17,15,13,7,1,5,13,17,19,15,7,13,8,17,6,6,9,7,7],[15,5,1,19,8,12,2,6,14,17,12,1,16,12,14,1,17,2,8,11,19,14,16,12,15,1,6,10,1,1,11,0,19,4,7,19,16,16],[17,11,18,2,0,6,13,16,7,16,4,11,15,15,6,7,13,17,10,2,7,16,0,17,11,14,1,19,3,11,7,3,9,5,1,17,7,15],[5,16,4,9,14,15,5,8,18,10,6,10,2,4,13,9,10,15,13,17,17,8,8,11,16,18,3,5,15,18,0,13,0,5,3,15,13,10],[2,3,2,10,14,7,8,18,18,5,9,1,15,1,7,19,7,19,4,9,19,8,0,6,8,4,15,0,5,15,19,5,15,4,3,13,11,4],[18,9,0,3,13,5,14,18,15,15,11,2,19,8,9,5,5,5,1,11,14,11,10,10,6,7,19,19,4,2,15,1,1,16,11,16,11,4],[13,5,1,16,0,1,15,11,16,12,8,2,5,15,0,19,9,1,9,17,2,15,14,12,11,19,13,4,5,16,2,2,10,1,13,11,10,11],[11,6,18,9,14,13,4,15,18,0,12,11,15,18,16,8,4,4,18,12,15,12,8,18,3,15,11,9,12,11,2,1,9,13,5,12,7,15],[16,12,3,14,17,12,18,14,2,16,15,2,6,2,17,16,0,7,18,7,9,15,4,9,14,19,13,8,10,9,12,15,11,2,8,16,8,12],[9,2,19,13,6,19,1,16,8,13,7,15,10,17,4,11,2,4,17,12,1,14,8,5,7,9,0,0,8,12,15,11,16,5,15,0,2,13],[12,14,17,18,15,17,4,19,7,19,18,4,0,14,10,5,13,3,2,18,7,16,8,9,9,9,19,16,3,4,14,5,11,4,10,12,7,10],[3,8,12,16,17,14,1,6,10,11,7,10,15,9,17,7,4,10,5,11,13,2,14,14,11,6,17,7,13,2,11,2,7,15,17,3,13,5],[3,11,5,17,7,4,12,15,5,8,2,13,16,3,8,3,16,10,0,10,12,13,16,16,8,0,1,9,3,7,15,18,14,11,2,7,8,13],[19,19,7,13,17,4,10,15,7,8,13,11,14,12,10,16,17,7,0,13,5,11,13,0,12,4,19,18,18,14,0,15,2,18,8,11,7,0],[18,18,18,0,2,6,9,19,4,3,6,10,10,17,2,7,9,18,18,3,12,14,12,4,17,7,11,15,11,9,0,17,18,8,17,0,18,7],[16,13,5,6,1,18,3,19,13,10,17,1,11,16,16,17,13,13,8,14,8,14,16,0,5,19,12,14,8,7,9,18,7,12,7,5,13,18],[17,4,17,8,6,13,13,2,12,8,16,11,9,7,0,0,7,8,10,18,5,10,3,1,16,6,3,5,16,17,1,2,3,19,7,13,0,19],[14,6,14,2,14,13,16,18,14,16,5,0,14,6,16,14,2,19,18,11,0,9,1,4,3,7,1,1,3,8,10,5,4,3,1,16,14,11],[16,7,12,2,1,13,6,15,15,16,5,4,19,19,17,14,10,8,14,16,8,2,4,11,10,1,5,18,5,18,9,12,10,2,1,19,7,11],[13,0,8,14,4,5,3,11,7,1,18,12,10,14,2,10,18,9,14,2,12,1,14,19,3,18,6,16,5,11,7,13,3,3,16,16,8,17],[3,2,17,6,15,16,18,4,2,16,10,13,19,8,16,11,5,12,19,3,12,7,11,16,14,8,18,18,3,8,3,5,14,14,4,0,7,4],[8,6,5,13,19,17,13,8,19,13,9,12,1,8,16,5,13,8,3,8,19,7,13,15,18,16,4,8,11,17,11,8,3,13,13,12,10,15],[3,4,12,10,19,5,10,17,17,5,10,19,14,4,5,12,13,6,13,14,6,0,3,16,18,1,19,4,13,18,3,12,2,18,15,7,9,9],[18,3,0,7,2,0,4,9,18,2,4,11,5,4,2,5,7,4,14,1,4,16,1,7,1,12,2,17,15,18,9,4,16,0,9,3,13,19],[16,15,6,17,14,4,12,17,2,16,12,3,17,6,10,16,9,3,17,15,7,17,10,2,15,3,4,8,12,9,15,1,14,5,2,17,19,4],[3,5,18,5,9,3,8,11,9,9,14,17,10,9,9,6,15,8,5,10,4,1,16,6,0,13,14,4,1,2,10,3,3,5,4,15,11,9],[19,4,13,6,3,2,4,6,11,12,2,19,13,13,17,14,14,17,0,0,17,16,12,12,17,18,10,12,18,7,10,17,2,1,6,11,17,5],[1,2,15,7,15,16,14,15,13,11,2,13,15,9,18,12,15,11,18,11,17,7,8,0,5,16,0,3,0,9,10,11,10,1,6,4,2,10],[16,5,16,3,4,8,17,12,1,9,1,2,14,12,13,17,8,12,0,12,18,8,11,19,12,0,10,6,11,2,11,1,4,15,1,15,8,14],[6,18,11,18,18,7,0,12,4,11,0,0,0,9,8,6,11,9,6,19,18,19,17,5,6,10,13,8,13,12,9,17,2,2,19,13,19,0],[14,11,12,8,3,7,9,9,10,8,4,12,1,5,1,18,19,13,11,16,7,13,0,4,8,2,14,13,1,12,16,19,6,13,0,0,5,19],[14,7,3,2,7,15,16,18,5,12,6,2,6,3,14,1,12,0,13,10,4,14,13,19,8,6,1,18,3,12,15,5,8,2,9,4,2,11],[19,13,2,1,14,0,3,4,11,9,4,0,4,8,1,17,12,3,4,18,3,15,15,11,16,16,14,4,14,3,18,11,14,3,17,18,7,16],[14,19,17,17,18,4,4,0,17,19,17,12,3,11,11,14,18,18,4,6,16,19,15,5,19,16,2,8,17,9,12,8,16,14,4,8,14,16],[18,6,9,12,4,6,6,17,10,5,14,8,19,4,4,9,7,4,14,13,10,7,3,18,6,6,11,0,13,4,13,8,18,10,19,18,6,12],[0,0,0,15,6,1,14,13,19,0,0,3,9,6,10,13,15,3,9,9,0,6,7,14,11,15,16,16,4,19,2,19,6,16,5,12,10,14],[8,15,0,17,16,6,1,4,2,10,0,19,17,9,11,10,2,1,11,11,4,17,13,19,4,6,7,12,9,4,17,6,5,3,13,16,8,13],[7,2,19,5,15,6,14,19,1,16,3,7,13,6,1,16,8,1,8,2,0,18,15,3,9,2,10,12,2,17,12,12,13,17,4,7,15,19],[19,1,12,14,0,13,3,6,8,0,3,9,3,3,16,12,5,10,1,13,14,11,12,4,11,3,1,8,9,0,16,16,17,5,5,19,19,14],[18,1,5,7,8,4,0,0,0,0,13,16,13,7,9,8,14,17,7,3,17,7,19,11,0,19,8,13,5,12,16,11,0,4,0,17,9,17],[19,3,7,4,8,12,17,17,19,2,1,11,6,11,3,19,5,5,12,13,12,15,10,3,5,0,5,3,4,12,4,0,5,5,6,5,1,16],[17,18,17,10,13,4,9,19,9,3,11,18,2,10,12,10,6,0,12,0,4,6,15,9,15,6,12,17,17,15,13,4,9,7,14,12,5,18],[3,11,17,16,1,1,10,6,9,11,3,10,0,16,18,5,11,9,4,18,10,1,7,10,13,2,9,11,6,11,13,15,18,7,10,9,0,3],[4,5,7,16,3,13,13,16,6,4,9,15,17,5,3,9,12,6,11,7,9,14,18,4,14,5,16,11,7,2,3,15,10,15,18,6,16,5],[12,15,5,15,12,7,1,18,5,19,2,11,7,0,13,13,17,7,0,5,6,4,2,0,18,19,19,12,6,2,8,3,12,14,11,18,14,17]]
matrix = [[9,9,4],[6,6,8],[2,1,1]]
matrix = [[7,6,1,1],[2,7,6,0],[1,3,5,1],[6,6,3,2]]
switch = 1
print("\n"*9)
print(foo.longestIncreasingPath(matrix))
print("finale^")
