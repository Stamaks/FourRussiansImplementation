# Implementation of Four Russians Algorithm for boolean square matrices multiplication

## Quick start
Clone the repository, open the project folder in your terminal and run:

    python3 src/main.py

Here is the example of the main scenario:

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

At first you will be asked to enter matrix size. Enter just one integer number.
Then enter your matrices one by one in the following format:
    
    1 0 1
    0 1 1
    1 1 1

This is what 3 x 3 matrix should like (regardless spaces). If you enter a number that is less than 0 or more than one, or any other format mistake, you will be asked to re-enter the matrix.
Finally, the program will perform the multiplication and the result will be shown.


## How does it work?
Main logic can be found here: `src/lib/matrices_multiplication.py`

At first, the binary log of matrices size is calculated, let's call it `k`. For each pair of numbers from range `(0, 2^k - 1)` we calculate bitwise AND and see if the number of bits equal to 1 is odd. If it is, the bitwise AND is put into the set. We'll need it later. This operation takes `O(2^(k*2*k))` time. Precalculated set is dumped into the `.data/k` file just to minimize the furher runs' calculations.
Then each matrix is being compressed. If the matrix is the first one, each row is divided into vectors of size `k` (otherwise - each col). Each binary vector represents a decimal number. We calculate the number and put it elementwise to the compressed matrix. It takes us `O(2*n^2)` time for both matrices.
After that, we "multiply" two compressed matrices. Though, instead of element wise multiplication, we do bitewise AND and then lookup the result in the precalculated set. If it is there, we put 1 in the result matrix. Otherwise, put 0.

The algorithm asymptotics is `O(n^3/logn)`. Actually, in this implemntation it should be multiplied by a constant of bitwise AND, which depends on one's processor (yet, it still remains a constant).
