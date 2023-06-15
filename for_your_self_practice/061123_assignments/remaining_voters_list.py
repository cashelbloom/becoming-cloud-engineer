'''
In this exercise, you are going to write program that will provide a dictionary of the voters who have not yet voted on
a given time on the voting day.
You will have a master voting list as a Python dictionary that will contain all the voter names
and their corresponding voter ids.
This list will NOT change at all.
You will have another dictionary that is the duplicate of the master voting list. At the beginning of the voting ,
this duplicate voter list will have the exact voter list as in the master voting list.
Call this duplicate dictionary as remaining_voters_list
You will have another voter list (a dictionary) that would hold the voters who have voted so far.
Call this dictionary as voted_voters_list.
As a voter completes voting, your program should remove the voter from the remaining_voters_list
and add the same voter to the voted_voters_list.
Have 10 voters in your master voting list and have a while loop for 5 voters to vote.
After the while loop, print the voters in the remaining_voters_list and the voted_voters_list and see if they print
as expected.
'''

master_voting_list = {
    "A": 11,
    "B": 22,
    "C": 33,
    "D": 44,
    "E": 55,
    "F": 66,
    "G": 77,
    "H": 88,
    "I": 99,
    "J": 100
}
