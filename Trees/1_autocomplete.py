"""
Letter Frequency Tree. This populates a tree based on the users input, keeping track of words entered and the 
frequency of each letter the user inputs.

@author Ben Antonellis
"""

import string

class Node:
    
    def __init__(self, letter: str) -> None:
        self.letter = letter
        self.count = 0
        self.nodes = []

    def add_node(self, node: object) -> None:
        # Check if the string is currently empty:
        if node.letter == "":
            # Now we return since we're all out of letters
            return
        # Determine if letter is already a child node
        next_node = self.__has_letter_node(node.letter[0])
        # If there is no child node for that letter
        if next_node == None:
            # We need to create a new node with the new letter
            new_node = Node(node.letter[0])
            # Because there is no child, we increment the count by 1
            new_node.count += 1
            # Now we add the node to the nodes list
            self.nodes.append(new_node)
            # Now we need to work with the rest of the letters on the new node, skipping the front letter
            new_node.add_node(Node(node.letter[1:]))
        # If there is a child node present
        else:
            # We need to add the count to that letter
            next_node.count += 1
            # Now we add the next letters to the current node
            next_node.add_node(Node(node.letter[1:]))

    def __has_letter_node(self, letter: str) -> object | None:
        for node in self.nodes:
            if node.letter == letter:
                return node
        return None
    
    def has_nodes(self) -> bool:
        return self.nodes != []

    def __str__(self, level=0) -> str:
        # Martijn Pieters: https://stackoverflow.com/a/20242504/8968906
        ret = "\t" * level + repr(self.letter) + str(self.count) + "\n"
        for child in self.nodes:
            ret += child.__str__(level + 1)
        return ret

    def __repr__(self) -> str:
        return self.__str__()


class AutoCompleteTree:

    def __init__(self) -> None:
        self.roots = [ Node(c) for c in string.ascii_lowercase ]

    def get_root_letter_node(self, letter: str) -> Node:
        for node in self.roots:
            if node.letter == letter:
                return node
    
    def print_tree(self) -> None:
        for root in self.roots:
            if root.has_nodes():
                print(root)
    
    def store_input(self, text: str) -> None:
        node = self.get_root_letter_node(text[0])
        node.count += 1
        node.add_node(Node(text[1:]))

def main():
    tree = AutoCompleteTree()
    while True:
        text = input(">>> ")
        tree.store_input(text)
        tree.print_tree()

if __name__ == '__main__':
    main()