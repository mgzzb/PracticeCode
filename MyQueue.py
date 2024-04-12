class MyQueue:

    def __init__(self):
        self.queue = []
        

    def push(self, x: int) -> None:
        # Pushes element x to the back of the queue.
        if x in self.queue:
            self.queue.remove(x)
        self.queue.append(x)
        

    def pop(self) -> int:
        num = self.queue[0]
        self.queue.remove(num)
        return num

    def peek(self) -> int:
        # Returns the element at the front of the queue.
        return self.queue[0]

    def empty(self) -> bool:
        # Returns true if the queue is empty, false otherwise.
        if self.queue == []:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
