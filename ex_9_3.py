# ex 9.3 -  maximal common subarray

word_a, word_b = input().split()

a, b, = len(word_a), len(word_b)

solution_subarray = [[0] * b for i in range(a)]
solution_substring = [[0] * b for i in range(a)]

for i in range(a):
    for j in range(b):
        if word_a[i] == word_b[j]:
            solution_subarray[i][j] = solution_subarray[max(0, i - 1)][max(0, j - 1)] + 1
            solution_substring[i][j] = solution_substring[max(0, i - 1)][max(0, j - 1)] + 1
        else:
            solution_subarray[i][j] = max(solution_subarray[i][max(0, j - 1)], solution_subarray[max(0, i - 1)][j])
            solution_substring[i][j] = 0

print(solution_subarray)
print(solution_substring)
