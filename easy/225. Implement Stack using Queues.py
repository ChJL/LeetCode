#Tag:  Stack
'''
Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

SOL: just a implementation...
could take a look at the "pop" part.
'''
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = collections.deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        return self.stack

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        tmp = self.stack[-1]
        for i in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())
        self.stack.popleft()
        return tmp

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return 1 if not self.stack else 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()