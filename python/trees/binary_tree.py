from trees.node import Node
# from node import Node

class BinaryTree():


    def __init__(self, root = None):
        """
        BinaryTree class creates BinaryTree instances.

        Arguments:
        root: Node
        """
        self.root = root
        self.values = []
        self.maximum = 0

    def pre_order(self):
        """
        pre_order method traverses the binary tree in (root >> left >> right) order.

        Arguments: None

        Return: List of Node Values
        """
        self.values = []

        def walk(root):
            """
            walk is a helper method for pre_order.

            Arguments:
            root: Tree Root Node
            """
            try:
                if root:
                    self.values += [root.value]

                if root and root.left:
                    walk(root.left)

                if root and root.right:
                    walk(root.right)
            except:
                raise Exception("Tree seems to be empty. Check your data and try again.")

        walk(self.root)
        print(self.values)
        return self.values


    def in_order(self):
        """
        in_order method traverses the binary tree in  (left >> root >> right) order.

        Arguments: None

        Return: List of Node Values
        """
        self.values = []

        def walk(root):
            """
            walk is a helper method for in_order.

            Arguments:
            root: Tree Root Node
            """
            try:
                if root and root.left:
                    walk(root.left)

                if root:
                    self.values += [root.value]

                if root and root.right:
                    walk(root.right)

            except:
                raise Exception("Tree seems to be empty. Check your data and try again.")

        walk(self.root)
        print(self.values)
        return self.values



    def post_order(self):
        """
        post_order method traverses the binary tree in  (left >> right >> root) order.

        Arguments: None

        Return: List of Node Values
        """
        self.values = []

        def walk(root):
            """
            walk is a helper method for post_order.

            Arguments:
            root: Tree Root Node
            """

            try:
                if root and root.left:
                    walk(root.left)

                if root and root.right:
                    walk(root.right)

                if root:
                    self.values += [root.value]

            except:
                raise Exception("Tree seems to be empty. Check your data and try again.")

        walk(self.root)
        print(self.values)
        return self.values



    def find_maximum_value(self):
        """
        find_maximum_value method traverses the binary tree in search for the maximum number its' nodes contain.

        Arguments: None

        Return: Number
        """

        def walk(root):
            """"
            walk is a helper method for find_maximum_value.

            Arguments:
            root: Tree Root Node
            """

            try:
                if root:
                    if (type(root.value) == int or type(root.value) == float) and root.value > self.maximum   :
                        self.maximum = root.value

                if root and root.left:
                    walk(root.left)

                if root and root.right:
                    walk(root.right)


            except:
                raise Exception("Tree seems to be empty. Check your data and try again.")


        walk(self.root)
        print(self.maximum)
        return self.maximum



class BinarySearchTree(BinaryTree):

    def __init__(self, root=None):
        """
        BinaryTree class creates BinaryTree instances.

        Arguments:
        root: Node
        """
        super().__init__(root=root)
        self.target = None

    def search(self, value):
        """
        Searches for a Node lcoation in a Binary Search Tree.

        Arguments:
        value: any

        Return : Target Node
        """

        def walk(root, value):
            """
            walk is a helper method for search.

            Arguments:
            root: Tree Root Node
            value: any
            """

            try:
                if not root or root.value == value:
                    self.target = root
                    print(self.target.value)
                    return self.target

                if value > root.value:
                    walk(root.right, value)

                if value < root.value:
                    walk(root.left, value)

            except:
                raise Exception("Entered value does not to exist within the tree.")


        walk(self.root, value)



    def add(self, value):
        """
        Adds a new node with that value in the correct location in the binary search tree.

        Arguments:
        value: any

        Return :Added Node Value
        """


        def walk(root, value):
            """
            walk is a helper method for add.

            Arguments:
            root: Tree Root Node
            value: any
            """
            if not root:
                self.target = Node(value)
                root = self.target
                return root

            else:
                if root.value == value:
                    self.target = root
                    return root

                if value > root.value:
                    root.right = walk(root.right, value)

                if value < root.value:
                    root.left = walk(root.left, value)

            return root


        if not self.root:
            self.target = Node(value)
            self.root = self.target
            return self.root
        else:
            walk(self.root, value)
            print(self.target.value)
            return self.target



    def contain(self, value):
        """
        Indicates whether or not a value is in the tree at least once.

        Arguments:
        value: any

        Return :Boolean
        """
        self.target = False

        def walk(root, value):
            """
            walk is a helper method for contain.

            Arguments:
            value: any
            """

            if root and root.value == value:
                self.target = True
                print(self.target)
                return self.target

            if root and value > root.value:
                walk(root.right, value)

            if root and value < root.value:
                walk(root.left, value)

        walk(self.root, value)

        print(self.target)
        return self.target



