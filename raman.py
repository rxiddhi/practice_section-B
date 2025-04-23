##SORT WITHOUT SORTING
"""Given a list of integers, complete the function sorted_list(list_of_integers) that returns a list with the same integers arranged in non-decreasing order. Non-decreasing order means that each number in the list is followed by a number that is either the same or larger (in other words, from smallest to largest, with repeats allowed). For example, [3, 1, 4, 2, 2] in non-decreasing order would be [1, 2, 2, 3, 4].

Note: You are not allowed to use Python's built-in sort() or sorted() functions; instead, implement your own sorting logic to arrange the elements in non-decreasing order.
Input
The first and only line consists of space separated Integers representing the required list.

Note: No need to use input() for taking input. It's already done by checker.

Constraints:
1<= size of list<=1000
1<=elements in list<=106
Output
Print the given space separated integers in non-decreasing order.

Note: You just need to return, No need to use print() for printing output. It's already done by checker.
Example
Input:
5 6 10 1 2 4 2

Output:
1 2 2 4 5 6 10"""

def sorted_list(list_of_integers):
    sor=[]
    while list_of_integers!=[]:
        temp=min(list_of_integers)
        sor.append(temp)
        list_of_integers.remove(temp)
    return sor