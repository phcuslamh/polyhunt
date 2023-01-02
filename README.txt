CODE USAGE

a. Set input file name:
Put the source code into a directory named "datasets" together with data set files A, B, C, D, E. 
To import data set A, put 'datasets/A' into the parentheses in line 74. Similarly for files B, C, D, E.

*NOTE BEFORE PROCEEDING: among the parts
########### Find lambda ###########,
########### Find M ###########, and
########### Find w and MSE ###########, 
at most one can be uncommented at a time when we run the program. 
For example, when we find M, make sure that the two remaining parts are commented out properly.

b. Find lambda:
Uncomment the part ########### Find lambda ########### and run the program.

c. Find M:
Uncomment the part ########### Find M ###########. 
In line 108, set the value of the variable "lamb" to the value of lambda that we found earlier.
In line 110, set the value of the variable "rho" to the number of iterations we prefer.
Run the program.

d. Find w and MSE:
Uncomment the part ########### Find w and MSE ###########.
In line 132, set the value of the variable "M" to the value of M that we found earlier.
In line 133, set the value of the variable "lamb" to the value of lambda that we found earlier.
In line 143, change the range of our X-axis as we like. 
(In the original code, I used -1.1 and 1.1 as endpoints, as the x-coordinates in the data sets are between -1.0 and 1.0)
Run the program.  

--------------------------------------------------------------------------------
NOTES ON THE PARAMETER FILES

The parameters are contained in plain text files in the subdirectory "Parameters".
In each parameter files, the first line is M, the best fit order found. 
The remaining lines are coefficients of the best fit polynomial, from w_0, w_1, ... to w_M in that order.
We do not include the regularization constant, which is e^{-2} for all of the data sets. 