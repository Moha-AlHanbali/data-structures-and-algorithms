from trees.queue import Queue
# from queue import Queue

class KaryNode():
    """
    Node class createsa KaryNode.

    Arguments:
    value: any
    left: Node
    right: Node
    """
    def __init__(self, value):
        self.value = value
        self.children = []



class KaryTree():

    def __init__(self, k, root = None):
        """
        KaryTree class creates KaryTree instances.

        Arguments:
        root: KaryNode
        k: Int number of Node children
        """
        self.root = root
        self.k = k

    def traverse_kary_tree(self):
        """
        traverse_kary_tree method traverses the K-aryTree in Breadth First Order.

        Arguments: None

        Return: List of Node Values
        """

        def walk(root):
            """"
            walk is a helper method for traverse_kary_tree.

            Arguments:
            root: Tree Root Node
            """
            tree_values = []
            queue = Queue()
            queue.enqueue(root)

            while queue.front:
                current = queue.dequeue()
                tree_values += [current.value]

                for child in current.children:
                    queue.enqueue(child)

            return tree_values

        try:
            if self.root:
                walk(self.root)
                print(walk(self.root))
                return walk(self.root)
        except:
            raise Exception("Tree seems to be empty. Check your data and try again.")
