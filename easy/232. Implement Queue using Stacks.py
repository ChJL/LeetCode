# Tag : stack

'''
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

SOL: use 2 stacks in push step
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.q2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.q:
            self.q2.append(self.q.pop())
        self.q.append(x)
        while self.q2:
            self.q.append(self.q2.pop())
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.q.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.q[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.q


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()