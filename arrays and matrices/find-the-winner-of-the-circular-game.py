class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #idea
        #constant space -> implies one array we pop from till winner and return that
        #can't we use a linkedlist in python and a next method to help with the removals?

        #code
        friends = list(range(1,n+1))
        i = 0

        while len(friends) > 1:
            i = (i + k - 1) % len(friends)
            _ = friends.pop(i)
        
        return friends[0]