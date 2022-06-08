class Stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def peak(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
def check(string):
    s=Stack()
    balanced=True
    index=0
    while index<len(string) and balanced:
        symbol=string[index]
        if symbol=="(":
            s.push(symbol)
        else:
            if s.isempty:
                balanced=False
            else:
                s.pop()
    if balanced and s.isempty:
        return True
    else:
        return False

print(check("(())"))


