class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # rows = len(matrix)
        # cols = len(matrix[0])
        
        # # transposed_matrix = [[0]* rows for _ in range(cols)]
        # transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
        
        # for i in range(rows):
        #     for j in range(cols):
        #         transposed_matrix[j][i] = matrix[i][j]
                
        # return transposed_matrix



        rows = len(matrix)
        cols = len(matrix[0])

        res = []
        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(matrix[j][i])
            res.append(row)
        return res