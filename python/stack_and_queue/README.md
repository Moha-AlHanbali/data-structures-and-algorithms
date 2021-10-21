# Stack and Queue

- This Module provides means to create Stacks and Queues and modify them to some extent.

<br>

## Challenge

- To implement new data-sahpe and manipulate it.

<br>


## Whiteboard Process

- ~

<br>

## Approach & Efficiency

- O complexity for (Stack.push) method: O(1)
- O complexity for (Stack.pop) method: O(1)
- O complexity for (Stack.peek) method: O(1)
- O complexity for (Stack.is_empty) method: O(1)

- O complexity for (Queue.queue) method: O(1)
- O complexity for (Queue.dequeue) method: O(1)
- O complexity for (Queue.peek) method: O(1)
- O complexity for (Queue.is_empty) method: O(1)

<br>

## API

- Stack.push()

        This method adds a Node to the top of a Stack.

        Arguments:
        value: any

- Stack.pop()

        This method removes the top Node of a Stack.

        Arguments: None

        Return: Popped Node Value

- Stack.peek()

        This method returns the value of top Node of a Stack.

        Arguments: None

        Return : Top Node Value

- Stack.is_empty()

        This method checks if a Stack has any Nodes within.

        Arguments: None

        Return : Boolean


- Queue.enqueue()

        This method adds a Node to the back of a Queue.

        Arguments:
        value: any

- Queue.dequeue()

        This method removes a Node to the front of a Queue.

        Arguments: None

        Return: Value of Dequeued Node

- Queue.peek()

        This method returns the value of front Node of a Queue.

        Arguments: None

        Return : Front Node Value

- Queue.is_empty()

        This method checks if a Queue has any Nodes within.

        Arguments: None

        Return : Boolean

<br>

## Testing Goals

- [x] Can successfully push onto a stack
- [x] Can successfully push multiple values onto a stack
- [x] Can successfully pop off the stack
- [x] Can successfully empty a stack after multiple pops
- [x] Can successfully peek the next item on the stack
- [x] Can successfully instantiate an empty stack
- [x] Calling pop or peek on empty stack raises exception
- [x] Can successfully enqueue into a queue
- [x] Can successfully enqueue multiple values into a queue
- [x] Can successfully dequeue out of a queue the expected value
- [x] Can successfully peek into a queue, seeing the expected value
- [x] Can successfully empty a queue after multiple dequeues
- [x] Can successfully instantiate an empty queue
- [x] Calling dequeue or peek on empty queue raises exception
