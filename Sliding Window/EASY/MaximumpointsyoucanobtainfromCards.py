'''Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.

Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12 Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4 Explanation: Regardless of which two cards you take, your score will always be 4.
'''
#MOST EFFFICIENT METHOD
def maxScore(cardPoints, k):
    '''If you're allowed to pick k cards from either end, that means you're leaving behind n - k cards somewhere in the middle (since the ends are being taken).
    So, instead of checking every combination of k cards from ends, you flip the problem:
    Find the minimum sum of n - k continuous cards — the ones you don’t take.
    Then subtract it from the total sum of all cards.'''
    total=sum(cardPoints)
    n=len(cardPoints)
    if k==n:
        return total
    elif k>n:
        return -1
    else:
        window_size=n-k          #You must leave behind n - k cards, so we need to find the subarray of that length with the smallest sum.
        curr_sum=sum(cardPoints[:window_size])
        minsum=curr_sum
        
        for i in range(window_size,n):
            curr_sum+=cardPoints[i]-cardPoints[i-window_size]
            minsum=min(minsum,curr_sum)
        return total-minsum       #Finally, subtract the smallest block of skipped cards from total to get the maximum score.
        


#example usage
cardpoints = [3,2,4,5,1,2,3]
k =2
print(maxScore(cardpoints, k))  # Output: 9