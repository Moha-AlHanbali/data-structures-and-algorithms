from trees.binary_tree import BinaryTree
from trees.queue import Queue
from trees.node import Node

# from binary_tree import BinaryTree
# from queue import Queue
# from node import Node

def breadth_first(tree: BinaryTree):
    """
    Traverse the input tree using a Breadth-first approach.

    Arguments:
    tree: BinaryTree

    Return:  Ordered list of all values in the tree.
    """


    def walk(root):
        """"
        walk is a helper method for breadth_first.

        Arguments:
        root: Tree Root Node
        """
        tree_values = []
        queue = Queue()
        queue.enqueue(root)

        while queue.front:
            current = queue.dequeue()
            tree_values += [current.value]

            if current.left:
                queue.enqueue(current.left)

            if current.right:
                queue.enqueue(current.right)

        return tree_values

    try:
        if tree.root:
            walk(tree.root)
            print(walk(tree.root))
            return walk(tree.root)
    except:
        raise Exception("Tree seems to be empty. Check your data and try again.")


