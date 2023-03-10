"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        
        if self.head is None: return
    
        current = self.head
        # while position is greater than 0, jump to the next node and drop position by one
        while position - 1 > 0 and current is not None:
            current = current.next
            position -= 1
        return current
            
            
        
    
    def insert(self, new_element, position):
        # get the element the inserted element will link from
        prev = self.get_position(position - 1)
        new_element.next = prev.next
        prev.next = new_element
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # in case the list is empty
        if self.head is None:
            return
        
        # if the head contains the value
        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        # traverse the list until value is spotted in next
        while current.next is not None:
            # if we spot it in the next node delete that node
            if current.next.value == value:
                current.next = current.next.next
                return
        print("not found")
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)