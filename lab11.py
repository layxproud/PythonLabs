class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __iter__(self):
        if self.left:
            yield from self.left.__iter__()
        yield self.val
        if self.right:
            yield from self.right.__iter__()

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = Tree(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = Tree(val)


if __name__ == "__main__":
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    BST = Tree(0)
    for num in nums:
        BST.insert(num)
    print("In order: ", list(x for x in BST))
