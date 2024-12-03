import sys
import re


class Queue:
    def __init__(self):
        self.elemnts = []

    def getSize(self):
        return len(self.elemnts)

    def enqueue(self, value):
        self.elemnts.append(value)

    def dequeue(self):
        return self.elemnts.pop(0)

    def isEmpty(self):
        return (len(self.elemnts) == 0)

    def getInOneLine(self):
        print(*self.elemnts)


class Stack:
    def __init__(self, size=10):
        self.elements = []
        self.max_size = size

    def isEmpty(self):
        return (len(self.elements) == 0)

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        return self.elements.pop()

    def put(self, value):
        self.elements.pop()
        self.elements.append(value)

    def peek(self):
        return self.elements[-1]

    def expand(self):
        self.max_size = self.max_size * 2

    def getInOneLine(self):
        print(*self.elements)

    def getSize(self):
        return len(self.elements)

    def getCapacity(self):
        return self.max_size


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def getList(self):
        temp_node = self.head
        while(temp_node.next != None):
            print(temp_node.data, end=' ')
            temp_node = temp_node.next
        print(temp_node.data)

    def insertFront(self, new_data):
        new_node = Node(new_data)
        if(self.head != None):
            new_node.next = self.head
        self.head = new_node

    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if(self.head == None):
            self.head = new_node
        else:
            temp_node = self.head
            while(temp_node.next != None):
                temp_node = temp_node.next
            temp_node.next = new_node

    def reverse(self):
        prev = None
        curr = self.head
        while(curr != None):
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        self.head = prev


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()