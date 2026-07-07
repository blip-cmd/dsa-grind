#https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/submissions/1889794511/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        #avoid longer step
        if n == k:
            return sum(cardPoints)
        
        #should be absorbed later
        if k == 1:
            if cardPoints[0] > cardPoints[n-1]:
                result = cardPoints[0]
            else:
                result = cardPoints[n-1]
            return result
        
        # sliding window to find max cards to pick
        # u can pick k number of cards.
        # u can only draw from left of right of currently availble cards
        # picking a card removes it from the currently available cards
        #3 ways to pick
            #all left
            #all right
            #left/right -> bigger
                # next: left/right -> bigger sum
                # next: ...
                    # problem: cards arent sorted. biggest can change from one side to another based on the supposed total.
                    #question: do we track possible windows:
                        # like these can easily happen when the 3rd mangitude affects the weight
                        # : left, right, right
                        #     left, right, left
                        #     right, right, left
                        #and return biggest
                        #if possible windows(options) are finite i agree to the approach
                        # so how many possible card drawing options are there
                        #sudden thought: how about prefix sum/accumulator method for going left, right , or right/left
                        #the right/left based on magnitude bit seems to worry me.
                        #the edge logic would be nice to figure out.
                        # a guiding question has lead me to see the mathematical inverse, that is handling the minimum of the excluded cards.

                        #so now we find minimum subarray in the middle
                        # given n&k. we want min(n-k) 

                        # l = 0
                        # r = k
                        # min_undealt_deck = sum(cardPoints[l:r])
                        # for r in range(k, len(cardPoints)):
                        #     l += 1
                        #     # exp = 
                        #     min_undealt_deck = min(sum(cardPoints[l:r]),min_undealt_deck )
                        #ohhh, i forgot sliding window we must sum in the lop elde O(nxW) ...we must use only the edges to determine the sum and get an O(n). The reinforment learning: revision is good.

            # #code Try2
            # l = 0
            # r = k
            # min_undealt_deck = sum(cardPoints[l:r])
            # for r in range(k, len(cardPoints)):
            #     l += 1
            #     exp = min_undealt_deck + cardPoints[r] -cardPoints[l]
            #     min_undealt_deck = min(exp,min_undealt_deck )


        #code Try3
        l = 0
        r = n-k
        current_window_sum = sum(cardPoints[l:r])
        maxi =  sum(cardPoints)
        min_deck = current_window_sum
        for r in range(r, len(cardPoints)):
            current_window_sum = current_window_sum + cardPoints[r] -cardPoints[l]
            min_deck = min(current_window_sum, min_deck)
            l += 1

        return maxi - min_deck
        #personal breakthroughs, correcting the indices with examples before changing variables
        # correctly updating and using multiple relevant different variables