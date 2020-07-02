<h1>Plus Minus</h1>
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.<br>

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.<br>

For example, given the array arr = [1,1,0,-1,-1] there are 5 elements, two positive, two negative and one zero. Their ratios would be 2/5=0.400000, 2/5=0.400000 and 1/5=0.200000. It should be printed as<br>
0.400000<br>
0.400000<br>
0.200000<br>

<h2>Function Description</h2>
Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.<br>
plusMinus has the following parameter(s):<br>
arr: an array of integers

<h2>Input Format</h2>
The first line contains an integer, n, denoting the size of the array.<br>
The second line contains n space-separated integers describing an array of numbers arr(arr[0], arr[1], arr[2],...., arr[n-1]).

<h2>Constraints</h2>
0 < n <=100<br>
-100 <= arr[i] <= 100

<h2>Output Format</h2>
You must print the following 3 lines:<br>
A decimal representing of the fraction of positive numbers in the array compared to its size.<br>
A decimal representing of the fraction of negative numbers in the array compared to its size.<br>
A decimal representing of the fraction of zeros in the array compared to its size.

<h3>Sample Input</h3>
6<br>
-4 3 -9 0 4 1<br>

<h3>Sample Output</h3>
0.500000<br>
0.333333<br>
0.166667
