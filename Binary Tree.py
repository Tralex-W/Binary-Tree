class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("CEO")

    cto = TreeNode("CTO")

    ih = TreeNode("Infrastructure Head")
    ih.add_child(TreeNode("Cloud Manager"))
    ih.add_child(TreeNode("App Manager"))

    ah = TreeNode("Application Head")

    hr = TreeNode("HR Head")
    hr.add_child(TreeNode("Recruitment Manager"))
    hr.add_child(TreeNode("Policy Manager"))

    root.add_child(cto)
    cto.add_child(ih)
    cto.add_child(ah)
    root.add_child(hr)

    root.print_tree()


if __name__ == "__main__":
    build_product_tree()