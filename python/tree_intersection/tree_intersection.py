"""This module contains tree_intersection function"""

from trees.binary_tree import BinaryTree
from hashtable.hashtable import HashTable


def tree_intersection(tree1:BinaryTree, tree2:BinaryTree):
    """
    tree_intersection function finds common values in 2 binary trees.

    Arguments:

        tree1: BinaryTree

        tree2: BinaryTree

    Return: Set containing common values
    """
    hashtable = HashTable()


    # Traverse Tree1
    def walk_add(root1):
        """
        walk_add is a helper method for tree_intersection.

        Arguments:
        root: Tree Root Node
        """
        try:
            if root1:
                hashtable.add(str(root1.value), root1.value)

            if root1 and root1.left:
                walk_add(root1.left)

            if root1 and root1.right:
                walk_add(root1.right)
        except:
            raise Exception("Tree seems to be empty. Check your data and try again.")

    # Traverse Tree2
    def walk_contain(root2):
        """
        walk_contain is a helper function for tree_intersection.

        Arguments:
        root: Tree Root Node

        Return: List of Values
        """
        try:
            if root2:
                if hashtable.contains(str(root2.value)):
                    tree2.values += [root2.value]
            if root2 and root2.left:
                walk_contain(root2.left)

            if root2 and root2.right:
                walk_contain(root2.right)

        except:
            raise Exception("Tree seems to be empty. Check your data and try again.")

        return tree2.values

    walk_add(tree1.root)
    common_set = set(walk_contain(tree2.root))
    if common_set:
        return common_set
    else:
        return {}


from trees.node import Node

node = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(44)
node5 = Node(5)
node6 = Node(6)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5
node5.left = node6

tree1 = BinaryTree()
tree1.root = node


pnode = Node(1)
pnode2 = Node(2)
pnode3 = Node(3)
pnode4 = Node(4)
pnode5 = Node(5)
pnode6 = Node(6)
pnode10 = Node(10)
pnodea = Node("a")
pnodeb = Node("b")


pnodea.left = pnode
pnodea.right = pnodeb
pnodeb.right = pnode10
pnode.left = pnode2
pnode.right = pnode3
pnode3.left = pnode4
pnode3.right = pnode5
pnode5.left = pnode6

tree2 = BinaryTree()
tree2.root = pnodea

tree_intersection(tree1, tree2)
