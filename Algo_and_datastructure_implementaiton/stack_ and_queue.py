class MyStack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


stack = MyStack()
stack.push(2)
stack.push(97)
stack.push(4)
stack.push(42)
stack.push(12)
stack.push(60)
stack.push(23)

"""
Sorting Array using two stacks.
"""
## Iterative method.
print(stack.stack_list)
def iterative_stack_sort(stack):
    temp_stack = MyStack()
    while not stack.is_empty():
        cur_val = stack.pop()
        if not temp_stack.is_empty() and cur_val > int(temp_stack.top()):
            temp_stack.push(cur_val)
        else:
            while(not temp_stack.is_empty()):
                stack.push(temp_stack.pop())
            temp_stack.push(cur_val)
    
    while(not temp_stack.is_empty()):
        stack.push(temp_stack.pop())
    return stack

sorted_stack = iterative_stack_sort(stack)
print(sorted_stack.stack_list)


stack = MyStack()
stack.push(2)
stack.push(97)
stack.push(4)
stack.push(42)
stack.push(12)
stack.push(60)
stack.push(23)

print(stack.stack_list)
### Recursive sort
def recursive_sort(stack):
    if (not stack.is_empty()):
        value = stack.pop()
        recursive_sort(stack)
        insert_stack(stack, value)
    
def insert_stack(stack, value):
    if (stack.is_empty() or value < stack.top()):
        stack.push(value)
    else:
        temp = stack.pop()
        insert_stack(stack,value)
        stack.push(temp)

recursive_sort(stack)
print(stack.stack_list)