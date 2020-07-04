<h1>Apple and Orange</h1>
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where s is the start point, and t is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.<br>

When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. A negative value of d means the fruit fell d units to the tree's left, and a positive value of d means it falls d units to the tree's right.

Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?<br>

For example, Sam's house is between s=7 and t=10. The apple tree is located at a=4 and the orange at b=12. There are m=3 apples and n=3 oranges. Apples are thrown apples=[2,3,-4] units distance from a, and oranges=[3,-2,-4] units distance. Adding each apple distance to the position of the tree, they land at [4+2,4+3,4+-4]=[6,7,0]. Oranges land at [12+3,12+-2,12+-4]=[15,10,8]. One apple and two oranges land in the inclusive range 7-10 so we print<br>
1<br>
2

<h2>Function Description</h2>
Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.<br>
countApplesAndOranges has the following parameter(s):<br>
s: integer, starting point of Sam's house location.<br>
t: integer, ending location of Sam's house location.<br>
a: integer, location of the Apple tree.<br>
b: integer, location of the Orange tree.<br>
apples: integer array, distances at which each apple falls from the tree.<br>
oranges: integer array, distances at which each orange falls from the tree.<br>

<h2>Input Format</h2>
The first line contains two space-separated integers denoting the respective values of s and t.<br>
The second line contains two space-separated integers denoting the respective values of a and b.<br>
The third line contains two space-separated integers denoting the respective values of m and n.<br>
The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a.<br>
The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

## Constraints
1 <= s,t,a,b,m,n <= 10^5<br>
-10^5 <= d <= 10^5<br>
a < s < t < b

## Output Format
Print two integers on two different lines:<br>
The first integer: the number of apples that fall on Sam's house.<br>
The second integer: the number of oranges that fall on Sam's house.

### Sample Input 0
7 11<br>
5 15<br>
3 2<br>
-2 2 1<br>
5 -6<br>

### Sample Output 0
1<br>
1
