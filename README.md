# fds

Simple implementaion of data structures __(DS)__ for python

## Content

- linked list
- stack
- queue

## Classes

- List // linked list
- Stack // stack
- Queue // queue

## API

### List

- insert(self, data, pos=0) // TODO: add node in the entered position (pos=0 => add in the begining)
- append(self, data) // TODO: add node in the end
- delete(self, data) // TODO: delete all nodes hav the entered data
- remove(self, pos=0) // TODO: return and remove node in the entered position (pos=0 => remove first node, pos=-1 => remove last node)
- first(self) // TODO: return the data in the first node
- last(self) // TODO: return the data in the last node

### Stack

- push(self, data) // TODO: add a node to the top
- pop(self) // TODO: return and remove the node in the top
- top(self) // TODO: return the data in the first node

### Queue

- enqueue(self, data) // TODO: add a node to the end
- dequeue(self) // TODO: return and remove the first element
- front(self) // TODO: return the data in the first node
- back(self) // TODO: return the data in the last node

### API for all DSs

- __repr__(self) // USE: print([DS_name]) // TODO: display the __DS__
- __len__(self) // USE: len([DS_name]) // TODO: return the lenth of the __DS__
- empty(self) // TODO: return True if the __DS__ is empty
- clear(self) // TODO: clear the __DS__
- find(self, data) // TODO: return the number of how many the entered data found in the __DS__
- reverse(self) // TODO: return the reverse of the __DS__

### classmethods for all DSs

// USE: [DS] = [DS_type].method([DS1], [DS2]) // Examples:</br>
>>> stck3 = Stack.merge(stck1, stck2)</br>
>>> Stack.swap([DS1], [DS2])</br>
__the tow DS parameters must be from the same DS__
- merge(DS1, DS2) // TODO: return the merge of two DS in new DS
- swap(DS1, DS2) // TODO: swap between DS1 and DS2 (DS1 will be DS2 and DS2 will be DS1)