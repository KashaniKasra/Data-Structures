class Stack:
    def __init__(self):
        self.elements = []
    def isEmpty(self):
        return (len(self.elements) == 0)
    def push(self, value):
        self.elements.append(value)
    def pop(self):
        return self.elements.pop()
    def peek(self):
        if not self.isEmpty():
            return self.elements[-1]
        else:
            return 0

N = int(input())

places = {}
dict = {0: -2}
res = []
org_stack = Stack()
temp_stack = Stack()

numbers = [int(i) for i in input().split()]

for i in range(len(numbers)):
    places[numbers[i]] = i
    
for i in range(N + 1):
    res.append(0)
    
for i in range(N, 0, -1):
    if (org_stack.isEmpty()):
        dict[places[i]] = -1
        org_stack.push(places[i])
    else:
        while(places[i] < org_stack.peek()):
            org_stack.pop()
        if (org_stack.isEmpty()):
            dict[places[i]] = -1
            org_stack.push(places[i])
        else:
            dict[places[i]] = org_stack.peek()
            org_stack.push(places[i])    
        
for i in range(N + 1):
    if (i == 0):
        continue
    res[i] = res[i - 1]
    place = places[i]
    while (not temp_stack.isEmpty() and places[i] < temp_stack.peek()):
        res[i] = res[i] - 1
        temp_stack.pop()
    if (dict[place] != -1 and (temp_stack.isEmpty()) or dict[place] != -1 and dict[place] != dict[temp_stack.peek()]):
        res[i] = res[i] + 1
        temp_stack.push(place)
        
for x in res:
    print(x)