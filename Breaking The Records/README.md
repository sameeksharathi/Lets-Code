<h1>Breaking the Records</h1>
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there.<br>

For example, assume her scores for the season are represented in the array scores=[12,24,10,24]. 
Scores are in the same order as the games played. She would tabulate her results as follows:<br>
<br>
                                 Count<br>
Game  Score  Minimum  Maximum   Min Max<br>
 0     12     12       12       0   0<br>
 1     24     12       24       0   1<br>
 2     10     10       24       1   1<br>
 3     24     10       24       1   1<br>
 
Given Maria's scores for a season, find and print the number of times she breaks her records for most and least points scored during the season.

<hr>
<h2>Input Format</h2>
The first line contains an integer n, the number of games.<br>
The second line contains n space-separated integers describing the respective values of score0, score1, score2-------,score(n-1).

<h2>Output Format</h2>
Print two space-seperated integers describing the respective numbers of times her best (highest) score increased and her worst (lowest) score decreased.

<h3>Sample Input 0</h3>
9<br>
10 5 20 20 4 5 2 25 1

<h3>Sample Output 0</h3>
2 4
