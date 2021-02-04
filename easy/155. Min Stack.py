# Tag: Stack
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

SOL: use two list: one put in the element, another record the current minimum value
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.Min = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        cur_min = self.getMin()
        if cur_min is None or x < cur_min:
            cur_min = x
        self.Min.append(cur_min)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.Min.pop(-1)
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.Min:
            return None
        return self.Min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()