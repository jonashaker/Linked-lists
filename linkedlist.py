class ListElement:
    def __init__(self, data, next = None):
        self._data = data
        self._next = next


class LinkedList:
    def __init__(self):
        """First element in list."""
        self._first = None
        """Last element in list."""
        self._last = None
        """Number of elements in list."""
        self._size = 0


    def addFirst(self, element):
        """Insert the given element at the beginning of this list."""
        self._first = ListElement(element, self._first)
        if self._first._next == None:
            self._last = self._first
            self._last._next = None
        self._size += 1

    def addLast(self, element):
        """Insert the given element at the end of this list."""
        if self._size == 0:
            self._first = ListElement(element, None)
            self._last = self._first
        elif self._size == 1:
                self._last = ListElement(element, self._last)
                self._first._next = self._last
        else:
            self._last._next = ListElement(element, None)
            self._last = self._last._next
        self._size += 1


    def getFirst(self):
        """Return the first element of this list."""
        return self._first._data



    def getLast(self):
        """Return the last element of this list."""
        return self._last._data

    def get(self, index):
        """Return the element at the specified position in this list."""
        try:
            element = self._first
            for i in range(0,index):
                element = element._next
            return element._data
        except:
            return None

    def removeFirst(self):
        """Remove and returns the first element from this list.
        Return null if the list is empty."""
        try:
            first = self._first
            self._first = first._next
            self._size -= 1
            return first._data
        except:
            return None

    def clear(self):
        """Remove all elements from this list."""
        self._first = None
        self._last = None
        self._size = 0

    def size(self):
        """Return the number of elements in this list."""
        return self._size

    def string(self):
        """Return a string representation of this list.
            The elements are enclosed in square brackets ("[]").
            Adjacent elements are separated by ", "."""
        string = ""
        element = self._first
        if self._size == None:
            return None
        while True:
            if element._next == None:
                break
            else:
                string += str(element._data) + ","
                element = element._next
        string += str(element._data)
        string = "[" + string + "]"

        return string

    def healthy(self):
        length = 0
        element = self._first
        while True:
            if element == None:
                break
            else:
                length += 1
                element = element._next
        assert length == self._size

        if length == 0:
            assert self._first == None
            assert self._last == None
        else:
            assert isinstance(self._first, ListElement)
            assert isinstance(self._last, ListElement)
            assert self._last._next == None





def main():
    """Main function with test code."""
    s = LinkedList()
    assert s._size == 0
    s.addFirst("good")
    assert s.getFirst() == "good"
    s.healthy()
    s.clear()

    s.healthy()
    s.addLast(1)
    assert s.getFirst() == 1
    assert s.getLast() == 1
    s.healthy()
    s.clear()

    s.addFirst(1)
    s.addLast(2)
    assert s.getFirst() == 1
    assert s.getLast() == 2
    s.addLast(3)
    assert s.get(1) == 2
    assert s._size == 3
    s.healthy()
    assert s.removeFirst() == 1
    assert s._size == 2
    assert s.getFirst() == 2
    assert s.getLast() == 3
    s.healthy()
    print(s.string())
    s.clear()
    assert s._size == 0

    s.addLast("1")
    s.addLast("2")
    s.addLast("3")
    assert s.size() == 3
    s.clear()

    s.addLast(1)
    s.addFirst("hey")
    s.addLast("3")
    s.addFirst(4)
    assert s.get(2) == 1
    assert s._size == 4
    assert s.getFirst() == 4
    assert s.getLast() == "3"





    s.addFirst("Jonas")
    s.addFirst("bye")
    s.addFirst("good")
    print(s.string())




main()