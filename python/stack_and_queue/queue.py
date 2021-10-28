from stack_and_queue.node  import Node
# from node  import Node



class Queue():
     """
     Queue class creates Queue instances.

     Arguments:
     front: Node
     back: Node
     """
     def __init__(self, front = None, back = None):
        self.front = front
        self.back = back

     def enqueue(self, value):
        """
        This method adds a Node to the back of a Queue.

        Arguments:
        value: any
        """
        if self.is_empty():
            self.front = Node(value)
            self.back = self.front
        else:
            self.back.next = Node(value)
            self.back = self.back.next


     def dequeue(self):
        """
        This method removes a Node to the front of a Queue.

        Arguments: None

        Return: Value of Dequeued Node
        """
        if self.is_empty():
            raise Exception("Queue is empty.")
        else:
            dispose = self.front
            self.front = self.front.next
            dispose.next = None
            if dispose == self.back:
                self.back == None
            return dispose.value


     def peek(self):
        """
        This method returns the value of front Node of a Queue.

        Arguments: None

        Return : Front Node Value
        """
        if self.is_empty():
            raise Exception("Queue is empty.")
        else:
            return self.front.value


     def is_empty(self):
        """
        This method checks if a Queue has any Nodes within.

        Arguments: None

        Return : Boolean
        """
        if not self.front:
            return True
        else:
            return False



def duck_duck_goose(list, k):

    counter=  1
    game_queue = Queue()


    for name in list:
        if counter== k:
            counter = 1
            continue
        else:
            counter += 1
            game_queue.enqueue(name)
    current = game_queue.front
    previous = current
    next_node = current

    while current and game_queue.front != game_queue.back:


        if counter == k:
            if current == game_queue.front:
                    game_queue.dequeue()
                    counter = 1
                    current = game_queue.front
                    previous = game_queue.front
                    continue

            if previous.next == game_queue.back:
                    previous.next = None
                    game_queue.back = previous
                    current = game_queue.front
                    previous = game_queue.front
                    counter = 1
                    continue

            else:
                previous.next = current.next
                next_node = current.next
                current.next = None
                current.next = next_node
                current = next_node
                counter = 1
                continue
        else:
            if current.next:
                previous  = current
                current = current.next
            else:
                current = game_queue.front
            counter += 1

    return game_queue.front.value

# if __name__ == "__main__":
#     names = ["A", "B", "C", "D", "E"]
#     names2 = ["A", "B", "C", "D", "E", "F", "G"]
#     names3 = ["A", "B", "C", "D", "E"]
#     names4 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
#     names5 = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

#     # duck_duck_goose(names, 3)
#     # duck_duck_goose(names2, 5)
#     # duck_duck_goose(names3, 2)
#     # duck_duck_goose(names4, 3)
#     duck_duck_goose(names5, 7)
