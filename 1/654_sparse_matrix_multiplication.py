class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        output = []
        
        for row in A:
            row_output = []
            if row == [0]*len(row):
                output.append(row[:])
                continue
            for j in range(len(B[0])):
                v = 0
                for i in range(len(row)):
                    v += row[i]*B[i][j]
                row_output.append(v)
            output.append(row_output)
        return output

if __name__ == "__main__":
    print(Solution().multiply([[1,0,0],[-1,0,3]],[[7,0,0],[0,0,0],[0,0,1]]))
    print(Solution().multiply([[1,0],[0,1]],[[0,1],[1,0]]))
