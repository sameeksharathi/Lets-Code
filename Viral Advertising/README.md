<h1>Viral Advertising</h1>
HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly 5 people on social media.
On the first day, half of those 5 people (i.e., floor(5/2) = 2) like the advertisement and each shares it with 3 of their friends. 
At the beginning of the second day, floor(5/2)*3 = 2*3 = 6 people receive the advertisement.
Each day, floor(recipients/2) of the recipients like the advertisement and will share it with 3 friends on the following day. 
Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, 
beginning with launch day as day 1.<br>
For example, assume you want to know how many have liked the ad by the end of the 5th day.<br>

Day Shared Liked Cumulative<br>
1      5     2       2<br>
2      6     3       5<br>
3      9     4       9<br>
4     12     6      15<br>
5     18     9      24<br>
The cumulative number of likes is 24.

<hr>
<h2>Input Format</h2>
A single integer, n, denoting a number of days.

<h2>Output Format</h2>
Print the number of people who liked the advertisement during the first n days.

<h3>Sample Input</h3>
3

<h3>Sample Output</h3>
9
