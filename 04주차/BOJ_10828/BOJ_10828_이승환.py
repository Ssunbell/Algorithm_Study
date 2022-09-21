class Stack:
    def __init__(self):
        self.stack = []

    def command(self, com, x):
        if com == "push":
            self.push(x)
        elif com == "pop":
            self.pop()
        elif com == "size":
            self.size()
        elif com == "empty":
            self.empty()
        elif com == "top":
            self.top()

    def push(self, x):
        self.stack.append(x)

    def __len__(self):
        return len(self.stack)

    def pop(self):
        if self.__len__() > 0:
            a = self.stack[-1]
            del self.stack[-1]
            print(a)
        else:
            print(-1)

    def size(self):
        print(self.__len__())

    def empty(self):
        if self.__len__() > 0:
            print(0)
        else:
            print(1)

    def top(self):
        if self.__len__() > 0:
            a = self.stack[-1]
            print(a)
        else:
            print(-1)


stack = Stack()

n = int(input())
com = [input() for _ in range(n)]

for i in range(n):
    x = 0
    if "push" in com[i]:
        comm, x = com[i].split()
        x = int(x)
        stack.command(comm, x)
    else:
        comm = com[i]
        stack.command(comm, x)
