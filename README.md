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

### API for all structures

- __repr__(self) // USE: print([DS_name]) // TODO: display the __DS__
- __len__(self) // USE: len([DS_name]) // TODO: return the lenth of the __DS__
- empty(self) // TODO: return True if the __DS__ is empty
- clear(self) // TODO: clear the __DS__
- reverse(self) // TODO: return the reverse of the __DS__