from collections import deque

n = int(input())

flag = 0
max_size = 0
numbers = []
dict = {}
nums_in_stack = {0: 0}
stack = deque()

for i in range(n):
    numbers.append(int(input()))

for num in numbers:
    if num in dict.keys():
        dict[num] = dict[num] + 1
    else:
        dict[num] = 1
        nums_in_stack[num] = 0
        
for num in numbers:
    if (dict[num] == 1):
        if (nums_in_stack[num] == 1):
            if (num == stack[-1]):
                stack.pop()
                nums_in_stack[num] = 0
            else:
                flag = 1
                break
        else:
            stack.append(num)
            nums_in_stack[num] = 0
            if ((len(stack) > max_size) and (nums_in_stack[0] == 0)):
                max_size = len(stack)
            elif ((len(stack) > max_size) and (nums_in_stack[0] == 1)):
                max_size = len(stack) - 1
            stack.pop()
    else:
        if (nums_in_stack[num] == 0):
            stack.append(num)
            nums_in_stack[num] = 1
            if ((len(stack) > max_size) and (nums_in_stack[0] == 0)):
                max_size = len(stack)
            elif ((len(stack) > max_size) and (nums_in_stack[0] == 1)):
                max_size = len(stack) - 1
    dict[num] = dict[num] - 1
            
if ((len(stack) == 0 or (len(stack) == 1 and nums_in_stack[0] == 1)) and flag == 0):
    print(max_size)
else:
    if (flag == 1):
        print(-1)