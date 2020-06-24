Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally.
Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item.
Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2,4,6].
Anna declines to eat item k=bill[2] which costs 6. If Brian calculates the bill correctly, Anna will pay (2+4)/2=3.
If he includes the cost of bill[2], he will calculate (2+4+6)/2=6. In the second case, he should refund 3 to Anna.

Input Format:
The first line contains two space-separated integers n and k, the number of items ordered and the 0-based index of the item that
Anna did not eat.
The second line contains n space-separated integers bill[i] where 0<i<n.
The third line contains an integer, b, the amount of money that Brian charged Anna for her share of the bill.

Output Format:
If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e., b(charged)-b(actual))
that Brian must refund to Anna. This will always be an integer.


