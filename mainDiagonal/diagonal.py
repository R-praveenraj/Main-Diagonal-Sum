# You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.
# Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.

# Input Format
# There are 1 lines in the input. First 2 integers R, C are the number of rows and columns. Then R * C integers follow corresponding to the row-wise numbers in the 2D array A.
# Output Format
# Return an integer denoting the sum of main diagonal elements.
# Input
# 3 3 1 -2 -3 -4 5 -6 -7 -8 9

# Output
# 15
def diagonal(matrix):
    total=0
    for i in range(len(matrix)):
        total+=matrix[i][i]
    return total

input=list(map(int,input().split()))
row=input[0]
column=input[1]
column1=2
matrix=[]
for i in range(row):
    matrix.append(input[column1:row+column1])
    column1+=row
print(diagonal(matrix))