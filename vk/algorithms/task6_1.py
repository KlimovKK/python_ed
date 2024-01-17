class Stack:
    def __init__(self):
        self.stack = []
        self.last_even = - 1

    def push(self, data):
        self.stack.append(data)
        if data % 2 == 0:
            self.last_even = data

    def pop(self):
        if len(self.stack) == 0:
            return - 1
        removed = self.stack.pop()

        return removed


n = int(input())
my_array = Stack()
for el in input().split():
    try:
        my_array.push(int(el))
    except EOFError:
        print(-1)
print(my_array.last_even)
