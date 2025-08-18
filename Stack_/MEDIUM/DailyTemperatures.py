'''You are given an array where each element represents the daily temperature on a specific day.
Write a function that returns an array where each element indicates the number of days after the corresponding day until a warmer temperature appears. If no warmer temperature exists in the future, set the value to 0.
'''

def dailyTemperatures(arr):
    n = len(arr)
    answer = [0] * n   # Result list with all 0s
    stack = []         # stores indices of temperatures

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:      #current day is warmer than the last unresolved day
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index  # days waited
        stack.append(i)

    return answer



print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
print(dailyTemperatures([30, 40, 50, 60]))  # Output: [1, 1, 1, 0]