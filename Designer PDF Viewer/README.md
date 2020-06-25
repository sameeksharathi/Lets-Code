<h1>Designer PDF Viewer</h1>
When you select a contiguous block of text in a PDF viewer, the selection is highlighted with a blue rectangle.
In this PDF viewer, each word is highlighted independently.

In this challenge, you will be given a list of letter heights in the alphabet and a string.
Using the letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.

For example, the highlighted word = torn. Assume the heights of the letters are t=2,o=1,r=1 and n=1. The tallest letter is 2 high and there
are 4 letters.The hightlighted area will be 2*4=8 mm^2 so the answer is 8.

<h2>Function Description:</h2>
Complete the designerPdfViewer function in the editor below. It should return an integer representing the size of the highlighted area.
designerPdfViewer has the following parameter(s):
h: an array of integers representing the heights of each letter
word: a string

<hr>
<h2>Input Format</h2>
The first line contains 26 space-separated integers describing the respective heights of each consecutive lowercase English letter, 
ascii[a-z].
The second line contains a single word, consisting of lowercase English alphabetic letters.

<h2>Output Format</h2>
Print a single integer denoting the area in mm^2 of highlighted rectangle when the given word is selected. Do not print units of measure.

<hr>
<h3>Sample Input 1</h3>
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba

<h3>Sample Output 1</h3> 
28
