# Implementation of Four Russians Algorithm for boolean square matrices multiplication

## Quick start
Clone the repository, open the project folder in your terminal and run:

    python3 src/main.py

At first you will be asked to enter matrix size. Enter just one integer number.
Then enter your matrices one by one in the following format:
    
    1 0 1
    0 1 1
    1 1 1

This is what 3 x 3 matrix should like (regardless spaces). If you enter a number that is less than 0 or more than one, or any other format mistake, you will be asked to re-enter the matrix.
Finally, the program will perform the multiplication and the result will be shown.

    four_russians_impl$ python3 src/main.py 
    Welcome to the 4 Russians algorithm implementation!
    NOTE: The algorithm works only with boolean square matrices!
    Each matrix size is n x n, enter n (just one integer number):
    3
    Please, enter the first boolean matrix, size 3 x 3:
    1 0 1
    0 0 1
    1 1 1
    The first matrix is:
    1 0 1
    0 0 1
    1 1 1
    Enter the second boolean matrix, size 3 x 3:
    1 0 0
    1 1 1
    1 1 0
    The second matrix is:
    1 0 0
    1 1 1
    1 1 0
    The final matrix is:
    0 1 0
    1 1 0
    1 0 1
    Want to run the algorithm again? Enter y/n
    n


## How does it work?
