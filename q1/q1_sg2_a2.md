# SG2 Activity 2: Code Quality Assessment

NAME and CLASS #: #4 CARILLO | #5 FERRER | #6 FULLANTE 

SECTION: 9-SAMAT

---
#### 1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?
- Pseudocode 1 is much more efficient with a larger dataset, since it only goes through the list once. On the other hand, Pseudocode 2 compares each number with every other number, so it has to do many more comparisons as the list gets bigger. 
---
#### 2. Readability
Which algorithm is easier to understand at first glance? What makes it clearer?
- It’s easier for me to understand the flow of Pseudocode 1 because the code is rationally concise and adequate for simply looking for the maximum number. Pseudocode 2 however makes use of multiple indentations and for loops which seems to overcomplicate and overengineer the solution.
---
#### 3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?
- The algorithm of Pseudocode 1 would be easier to update as it is less cluttered and there are fewer lines of code that you need to consider when changing the flow of the program. Whereas in Pseudocode 2, the usage of multiple lines, loops, and if-statements require you to reorganize everything upon a new addition.
---
#### 4. Testability
Which algorithm is easier to test with different inputs? Why?
- PseudoCode 1 is easier to test because it has a simpler process for finding the largest number. You can try different lists, such as lists with positive numbers, negative numbers, or repeated numbers, and easily check whether the answer is correct. PseudoCode 2 is harder to test because it compares every number with all the other numbers, creating many more comparisons to check. Both algorithms have predictable outputs, but PseudoCode 1 has fewer conditions and is easier to understand and verify.

---
#### 5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?
- The algorithm should check for inputs that are letters or special characters as they do not comply with the required data type (floats and/or integers).
---
#### 6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer.
- Pseudocode 1 is the better algorithm in solving the problem we have. It is easier to read, easier to edit, handles errors better, is more efficient and and easier to test.


