class BintreeNode:
    def __init__(self, val):
        self.gtr = None
        self.lsr = None
        self.val = val


class Bintree:
    def __init__(self):
        self.head = None

    def add_node(self, val):
        if not self.head:
            self.head = BintreeNode(val)
        else:
            current_node = self.head
            inserted = False
            while not inserted:
                if current_node.val > val:
                    if current_node.lsr:
                        current_node = current_node.lsr
                    else:
                        current_node.lsr = BintreeNode(val)
                        inserted = True
                elif current_node.val < val:
                    if current_node.gtr:
                        current_node = current_node.gtr
                    else:
                        current_node.gtr = BintreeNode(val)
                        inserted = True
                else:
                    raise Exception("duplicate key")

    def node_exists(self, val):
        exists = False
        if self.head:
            current_node = self.head
            found = False
            while not found:
                if current_node.val > val:
                    if current_node.lsr:
                        current_node = current_node.lsr
                    else:
                        exists = False
                        found = True
                elif current_node.val < val:
                    if current_node.gtr:
                        current_node = current_node.gtr
                    else:
                        exists = False
                        found = True
                else:
                    exists = True
                    found = True
        return exists

    # left root right
    def inorder(self):
        def traverse(node):
            node_list = []
            if node.lsr:
                node_list += traverse(node.lsr)
            node_list.append(node.val)
            if node.gtr:
                node_list += traverse(node.gtr)
            return node_list

        return traverse(self.head)

    # root left right
    def postorder(self):
        def traverse(node):
            node_list = []
            node_list.append(node.val)
            if node.lsr:
                node_list += traverse(node.lsr)
            if node.gtr:
                node_list += traverse(node.gtr)
            return node_list

        return traverse(self.head)

    # left right root
    def preorder(self):
        def traverse(node):
            node_list = []
            if node.lsr:
                node_list += traverse(node.lsr)
            if node.gtr:
                node_list += traverse(node.gtr)
            node_list.append(node.val)
            return node_list

        return traverse(self.head)
