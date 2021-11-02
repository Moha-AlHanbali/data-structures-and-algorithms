from trees.kary_tree import KaryNode, KaryTree
from trees.queue import Queue

# from kary_tree import KaryNode, KaryTree
# from queue import Queue


def fizz_buzz(tree: KaryTree):
    """
    Determines whether or not the value of each node is divisible by 3, 5 or both.
    Create a new tree with the same structure as the original, but the values modified as follows:
    If the value is divisible by 3, replace the value with “Fizz”
    If the value is divisible by 5, replace the value with “Buzz”
    If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
    If the value is not divisible by 3 or 5, simply turn the number into a String.

    Arguments:
    tree: KaryTree

    Return: Modified KaryTree
    """

    def walk(root):
        """"
        walk is a helper method for fizz_buzz.

        Arguments:
        root: Tree Root Node
        """
        tree_values = []
        queue = Queue()

        if type(root.value) == int and (root.value % 3 == 0) and (root.value % 5 == 0):
            root.value = "FizzBuzz"

        elif type(root.value) == int and(root.value % 3 == 0) and not (root.value % 5 == 0):
            root.value = "Fizz"

        elif type(root.value) == int and not (root.value % 3 == 0) and  (root.value % 5 == 0):
            root.value = "Buzz"

        else:
            root.value = str(root.value)


        queue.enqueue(root)

        while queue.front:
            current = queue.dequeue()
            tree_values += [current.value]

            for child in current.children:

                if type(child.value) == int and (child.value % 3 == 0) and (child.value % 5 == 0):
                    child.value = "FizzBuzz"

                elif type(child.value) == int and (child.value % 3 == 0) and not (child.value % 5 == 0):
                    child.value = "Fizz"

                elif type(child.value) == int and not (child.value % 3 == 0) and  (child.value % 5 == 0):
                    child.value = "Buzz"

                else:
                    child.value = str(child.value)

                queue.enqueue(child)

        return tree_values

    try:
        if tree.root:
            return walk(tree.root)
    except:
        raise Exception("Tree seems to be empty. Check your data and try again.")

