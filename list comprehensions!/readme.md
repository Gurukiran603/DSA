📌 List Comprehension – 3D Coordinates Problem
🧠 Problem Statement

Given four integers x, y, z, and n, representing the dimensions of a cuboid and a constraint value:

Generate a list of all possible coordinates [i, j, k] such that:

0 ≤ i ≤ x
0 ≤ j ≤ y
0 ≤ k ≤ z
The sum i + j + k ≠ n

Use list comprehension to solve the problem.

📥 Input Format
Four integers, each on a new line:
x
y
z
n
📤 Output Format
Print a list of coordinates in lexicographic increasing order
✅ Example
Input
1
1
1
2
Output
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
💡 Approach
Generate all combinations using nested loops
Filter out combinations where i + j + k == n
Use list comprehension for concise code
🚀 Solution (List Comprehension)
x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] 
          for i in range(x + 1) 
          for j in range(y + 1) 
          for k in range(z + 1) 
          if i + j + k != n]

print(result)
🔍 Explanation
range(x + 1) ensures values from 0 to x
Nested loops generate all possible [i, j, k]
Condition i + j + k != n filters unwanted combinations
Final result is stored as a list of lists
🧪 Sample Test Case
Input
2
2
2
2
Output
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], 
 [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], 
 [1, 2, 0], [1, 2, 1], [1, 2, 2], 
 [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 1]]
🎯 Key Concepts
List Comprehension
Nested Iteration
Conditional Filtering
🏷️ Tags

Python List-Comprehension Beginner DSA
