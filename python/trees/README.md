# Binary Tree and BST Implementation - tree-max - tree-breadth-first - tree-fizz-buzz

- This Module provides means to create Trees Data Structure and modify them to some extent.

<br>

## Challenge

- To implement new data-sahpe and manipulate it.

<br>


## Whiteboard Process

- tree-max

![tree-max.png](assets/tree-max.png)

<br>

- tree-breadth-first

![tree-breadth-first.png](assets/tree-breadth-first.png)

<br>

- tree-fizz-buzz

![tree-fizz-buzz.png](assets/tree-fizz-buzz.png)

<br>

## Approach & Efficiency

- O complexity for (BinaryTree.pre_order) method: O(log(n))
- O complexity for (BinaryTree.in_order) method: O(log(n))
- O complexity for (BinaryTree.post_order) method: O(log(n))

- O complexity for (BinarySearchTree.search) method: O(log(n))
- O complexity for (BinarySearchTree.add) method: O(log(n))
- O complexity for (BinarySearchTree.contain) method: O(log(n))

- O complexity for (BinaryTree.find_maximum_value) method: O(log(n))

- O complexity for (breadth_first) function: O(log(n))

- O complexity for (KaryTree.traverse_kary_tree) method: O(log(n))
- O complexity for (fizz_buzz) function: O(log(n))

<br>

## API

- BinaryTree.pre_order()

        pre_order method traverses the binary tree in (root >> left >> right) order.

        Arguments: None

        Return: List of Node Values

- BinaryTree.in_order()

        in_order method traverses the binary tree in  (left >> root >> right) order.

        Arguments: None

        Return: List of Node Values

- BinaryTree.post_order()

        post_order method traverses the binary tree in  (left >> right >> root) order.

        Arguments: None

        Return: List of Node Values

- BinarySearchTree.search()

        Searches for a Node lcoation in a Binary Search Tree.

        Arguments:
        value: any

        Return : Target Node

- BinarySearchTree.add()

        Adds a new node with that value in the correct location in the binary search tree.

        Arguments:
        value: any

        Return :Added Node Value

- BinarySearchTree.contain()

        Indicates whether or not a value is in the tree at least once.

        Arguments:
        value: any

        Return :Boolean

- BinaryTree.find_maximum_value()

        find_maximum_value method traverses the binary tree in search for the maximum number its' nodes contain.

        Arguments: None

        Return: Number

- breadth_first()

    Traverse the input tree using a Breadth-first approach.

    Arguments:
    tree: BinaryTree

    Return:  Ordered list of all values in the tree.

- KaryTree.traverse_kary_tree()

        traverse_kary_tree method traverses the K-aryTree in Breadth First Order.

        Arguments: None

        Return: List of Node Values

- fizz_buzz()

    Determines whether or not the value of each node is divisible by 3, 5 or both.
    Create a new tree with the same structure as the original, but the values modified as follows:
    If the value is divisible by 3, replace the value with “Fizz”
    If the value is divisible by 5, replace the value with “Buzz”
    If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
    If the value is not divisible by 3 or 5, simply turn the number into a String.

    Arguments:
    tree: KaryTree

    Return: Modified KaryTree

<br>

## Testing Goals

- Binary Tree

- [x] Can successfully instantiate an empty tree
- [x] Can successfully instantiate a tree with a single root node
- [x] Can successfully add a left child and right child to a single root node
- [x] Can successfully return a collection from a preorder traversal
- [x] Can successfully return a collection from an inorder traversal
- [x] Can successfully return a collection from a postorder traversal
- [x] Can successfully raise exceptions

---------------------------------------------------------------------------

- Binary Search Tree

- [x] Can successfully add a value to and empty tree
- [x] Can successfully add a value in its' correct location
- [x] Can successfully detect if a value is in a tree or not
- [x] Can successfully detect added values in tree

---------------------------------------------------------------------------

- Find Maximum Value

- [x] Can successfully find and return the max value
- [x] Can successfully raise exception if tree was empty
- [x] Can successfully check for values when other data types exist

---------------------------------------------------------------------------

- Tree Breadth First

- [x] Can successfully return a collection from a Breadth First traversal
- [x] Can successfully return values in expected order
- [x] Can successfully raise exceptions

---------------------------------------------------------------------------

- K-ary Tree

- [x] Can successfully instantiate an empty tree
- [x] Can successfully instantiate a tree with a single root node
- [x] Can successfully return a collection from a Breadth First traversal
- [x] Can successfully raise exceptions

---------------------------------------------------------------------------

- FizzBuzz

- [x] Can successfully return modified values in correct order
- [x] Can successfully handle none int values
- [x] Can successfully raise exceptions
