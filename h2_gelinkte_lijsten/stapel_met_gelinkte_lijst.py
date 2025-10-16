class StackList:

    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende

    def __init__(self):
        self.top = StackList.Knoop()

    def is_empty(self):
        return self.top.data is None

    def push(self, data):
        hulp = StackList.Knoop() 
        hulp.data = data
        hulp.volgende = self.top
        self.top = hulp

    def peek(self):
        return self.top.data

    def pop(self):
        x = self.top.data
        self.top = self.top.volgende
        return x


s = StackList()
print(s.is_empty())
s.push(5)
s.push(2)
print(s.is_empty())