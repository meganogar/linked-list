
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: ?
    # Space Complexity: ?
    def get_first(self):
        if self.head:
            return self.head.value
        
        print("HERE")
        return None


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_first(self, value):

        if not self.head:
            self.head = Node(value)
        else:
            old_head = self.head
            self.head = Node(value)
            self.head.next = old_head

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: ?
    # Space Complexity: ?
    def search(self, value):
        if not self.head:
            return False

        current = self.head
        while current:
            if current.value == value:
                return True
            print('FALALA')
            print(f'{current= }')
            current = current.next
            print(f'{current= }')

        return False

    # method that returns the length of the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def length(self):
        length = 0
        current = self.head

        while current:
            length += 1
            current = current.next
        
        return length
        

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: ?
    # Space Complexity: ?
    def get_at_index(self, index):
        length = 0
        current = self.head

        if not self.head:
            return None

        while current:
            if length == index:
                return current.value
            else:
                length += 1
                current = current.next
        
        return length

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: ?
    # Space Complexity: ?
    def get_last(self):
        if not self.head:
            return None

        current = self.head

        while current:
            if not current.next:
                return current.value
            
            current = current.next


    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_last(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node

        else:
            current = self.head
            
            while current.next:
                current = current.next

            current.next = new_node #here
            

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if not self.head:
            return None
        
        max = self.head.value
        current = self.head

        while current:
            if current.value > max:
                max = current.value
            current = current.next
        return max

    # method to delete the first node found with specified value
    # Time Complexity: ?
    # Space Complexity: ?
    # 3 -> 4 -> 5 
    # Need to Delete 3
    # Head should become 4
    # Assign current.next to new_head
    def delete(self, value):

        if not self.head:
            return None
            
        new_head = None

        if self.head.value == value:
            new_head = self.head.next
            self.head = new_head

        current = self.head
        while current:
            if current.next:
                if current.next.value == value:
                    current.next = current.next.next
            current = current.next

    # method to print all the values in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: ?
    # Space Complexity: ?
    def reverse(self):
        if not self.head:
            return 

        current = self.head
        next_node = None
        previous = None

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        self.head = previous

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        if not self.head:
            return
        
        current = self.head
        length = 0

        while current:
            length += 1
            current = current.next

        middle = None

        if length % 2:
            print(length % 2)
            middle = length // 2

        else:
            middle = length / 2

        x = 0
        current2 = self.head

        while current2:
            if x == middle:
                return current2.value 
            x += 1
            current2 = current2.next
            


    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        if not self.head:
            return
        
        current = self.head
        length = 0

        while current:
            length += 1
            current = current.next
        
        index = length - n

        current2 = self.head
        b = 1

        while current2:
            if b == index:
                return current2.value
            b += 1
            current2 = current2.next
            


    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        if not self.head:
            return False
        
        current = self.head
        array = []

        while current:
            if current.next in array:
                return True
            
            array.append(current)
            
            current = current.next
        return False
        



    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
