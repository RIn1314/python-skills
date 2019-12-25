from collections import deque


class CountdownTask:
    def run(self):
        import heapq
        nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
        print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
        print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]
        s = sorted(nums)
        print('small 3 :{}'.format(s[0:3]))
        print('max 3 :{}'.format(s[-3:]))


c = CountdownTask()
c.run()
