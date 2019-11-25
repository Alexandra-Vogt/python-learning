class AvlBintreeNode:
    def __init__(self, val):
        self.gtr = None
        self.lsr = None
        self.val = val


class Bintree:
    def __init__(self):
        self.head = None

    def rotate(self):
        noop

    def rebalance(self, prev_node, side):
        def get_weights(node):
            node.lsr = 1

        if side == "lsr":
            "left rotation"
        else:
            "right rotation"

    def add_node(self, val):
        if not self.head:
            self.head = BintreeNode(val)
        else:
            past_node0 = None
            past_node1 = None
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
