# Save the Prisoner!

A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around 
a circular table in sequentially numbered chairs. 
A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all
have been distributed.<br>
The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner
who will receive that candy.<br>
For example, there are 4 prisoners and 6 pieces of candy. The prisoners arrange themselves in seats numbered 1 to 4. Let's suppose two is drawn from the hat. 
Prisoners receive candy at positions 2 3 4 1 2 3. The prisoner to be warned sits in chair number 3.<br>

## Function Description:
Complete the saveThePrisoner function in the editor below. It should return an integer representing the chair number of the prisoner to warn. <br>
saveThePrisoner has the following parameter(s): <br>

n: an integer, the number of prisoners<br>
m: an integer, the number of sweets<br>
s: an integer, the chair number to begin passing out sweets from<br>

## Input Format:

The first line contains an integer, t, denoting the number of test cases. <br>
The next t lines each contain 3 space-separated integers: <br>
n: the number of prisoners <br>
m: the number of sweets <br>
s: the chair number to start passing out treats at <br>

## Constraints:
1 <= t <= 100<br>
1 <= n <= 10^9 <br>
1 <= m <= 10^9 <br>
1 <= s <= n

## Output Format
For each test case, print the chair number of the prisoner who receives the awful treat on a new line.

### Sample Input 0
2<br>
5 2 1<br>
5 2 2

### Sample Output 0
2<br>
3
