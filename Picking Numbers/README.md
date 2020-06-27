<h1>Picking Numbers</h1>
Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference
between any two of the chosen integers is less than or equal to 1. For example, if your array is a=[1,1,2,2,4,4,5,5,5], you can create two
subarrays meeting the criterion: [1,1,2,2] and [4,4,5,5,5]. The maximum length subarray has 5 elements.

<h2>Function Description</h2>
Complete the pickingNumbers function in the editor below. It should return an integer that represents the length of the longest array
that can be created.
<br>
pickingNumbers has the following parameter(s):
a: an array of integers

<h2>Input Format</h2>
The first line contains a single integer n, the size of the array a.<br>
The second line contains n space-separated integers a[i].

<h2>Output Format</h2>
A single integer denoting the maximum number of integers you can choose from the array such that the absolute difference between
any two of the chosen integers is <=1.
