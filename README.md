# pyfds

Simple implementaion of data structures __(DS)__ for python

## Content

- linked list
- doubly linked list
- sorted linked list
- stack
- queue
- priority queue
- binary search tree
* __utils__ // (package)

### Content of utils

- node // single pointer node
- dnode // double pointer node
- tnode // tree pointer node
- pair

### how to import utils

`from pyfds.utils import *`\
`pair = Pair()`\
or\
`import pyfds.utils`\
`pair = utils.Pair()`

## Classes

- List // linked list
- DList // doubly linked list
- SList // sorted linked list
- Stack // stack
- Queue // queue
- PQueue // priority queue
- BST // binary search tree

## API

### List

#### Properties

- first(self) // TODO: return the data in the first node
- last(self) // TODO: return the data in the last node

#### Methodes

- insert(self, data, pos=0) // TODO: add node in the entered position (pos=0 => add in the begining)
- append(self, data) // TODO: add node in the end
- delete(self, data) // TODO: delete all nodes hav the entered data
- remove(self, pos=0) // TODO: return and remove node in the entered position (pos=0 => remove first node, pos=-1 => remove last node)

### DList

#### Properties

- first // TODO: return the data in the first node
- last // TODO: return the data in the last node

#### Methodes

- add_begin(self, data) // TODO: add a node to the begin
- add_fin(self, data) // TODO: add a node to the fin
- delete(self, data) // TODO: delete all nodes hav the entered data
- remove(self, pos=0) // TODO: return and remove node in the entered position (pos=0 => remove first node, pos=-1 => remove last node)

### SList

#### Properties

- first // TODO: return the data in the first node
- last // TODO: return the data in the last node

#### Methodes

- append(self, data) // TODO: add a node to the list in a sorted way
- delete(self, data) // TODO: delete all nodes hav the entered data
- remove(self, pos=0) // TODO: return and remove node in the entered position (pos=0 => remove first node, pos=-1 => remove last node)

#### Note

- the (reverse, sort, exchange) are not supported in this __DS__ because they brake the rule of the __Sorted Linked List__

### Stack

#### Properties

- top // TODO: return the data in the first node

#### Methodes

- push(self, data) // TODO: add a node to the top
- pop(self) // TODO: return and remove the node in the top

### Queue

#### Properties

- front // TODO: return the data in the first node
- back // TODO: return the data in the last node

#### Methods

- enqueue(self, data) // TODO: add a node to the end
- dequeue(self) // TODO: return and remove the first element

### PQueue

#### Properties

- front // TODO: return the data in the first node
- back // TODO: return the data in the last node

#### Methods

- enqueue(self, data) // TODO: add a node to the queue in a sorted way
- dequeue(self) // TODO: return and remove the first element

### Methods for all DSs

- __str__(self) // USE: print([DS_name]) // TODO: display the __DS__
- __len__(self) // USE: len([DS_name]) // TODO: return the lenth of the __DS__
- empty(self) // TODO: return True if the __DS__ is empty
- clear(self) // TODO: clear the __DS__
- find(self, data) // TODO: return the number of how many the entered data found in the __DS__
- reverse(self) // TODO: return the reverse of the __DS__
- sort(self) // TODO: sort the __DS__ if its not sorted
- exchange(self, n) // TODO: circular permutation for n time

### classmethods for all DSs

// USE: [DS] = [DS_type].method([DS1], [DS2])</br>
// Examples:</br>
__>>>__ stck3 = Stack.merge(stck1, stck2)</br>
__>>>__ Stack.swap([DS1], [DS2])</br>
__the tow DS parameters must be from the same DS__

- merge(cls, DS1, DS2) // TODO: return the merge of two DS in new DS
- swap(cls, DS1, DS2) // TODO: swap between DS1 and DS2 (DS1 will be DS2 and DS2 will be DS1)
=======
# pyfds

Simple implementaion of data structures __(DS)__ for python

## Content

- linked list
- doubly linked list
- sorted linked list
- stack
- queue
- priority queue
* __utils__ // (package)

### Content of utils

- node // single pointer node
- dnode // double pointer node
- pair

### how to import utils

`from pyfds.utils import *`\
`pair = Pair()`\
or\
`import pyfds.utils`\
`pair = utils.Pair()`

## Classes

- List // linked list
- DList // doubly linked list
- SList // sorted linked list
- Stack // stack
- Queue // queue
- PQueue // priority queue

## API

### List

#### Properties

- first(self) // TODO: return the data in the first node
- last(self) // TODO: return the data in the last node

#### Methodes

- insert(self, data, pos=0) // TODO: add node in the entered position (pos=0 => add in the begining)
- append(self, data) // TODO: add node in the end
- delete(self, data) // TODO: delete all nodes hav the entered data
- remove(self, pos=0) // TODO: return and remove node in the entered position (pos=0 => remove first node, pos=-1 => remove last node)

### DList

#### Properties

- first // TODO: return the data in the first node
- last // TODO: return the data in the last node

#### Methodes

- add_begin(self, data) // TODO: add a node to the begin
- add_fin(self, data) // TODO: add a node to the fin
- delete(self, data) // TODO: delete all nodes hav the entered data
- remove(self, pos=0) // TODO: return and remove node in the entered position (pos=0 => remove first node, pos=-1 => remove last node)

### SList

#### Properties

- first // TODO: return the data in the first node
- last // TODO: return the data in the last node

#### Methodes

- append(self, data) // TODO: add a node to the list in a sorted way
- delete(self, data) // TODO: delete all nodes hav the entered data
- remove(self, pos=0) // TODO: return and remove node in the entered position (pos=0 => remove first node, pos=-1 => remove last node)

#### Note

- the (reverse, sort, exchange) are not supported in this __DS__ because they brake the rule of the __Sorted Linked List__

### Stack

#### Properties

- top // TODO: return the data in the first node

#### Methodes

- push(self, data) // TODO: add a node to the top
- pop(self) // TODO: return and remove the node in the top

### Queue

#### Properties

- front // TODO: return the data in the first node
- back // TODO: return the data in the last node

#### Methods

- enqueue(self, data) // TODO: add a node to the end
- dequeue(self) // TODO: return and remove the first element

### PQueue

#### Properties

- front // TODO: return the data in the first node
- back // TODO: return the data in the last node

#### Methods

- enqueue(self, data) // TODO: add a node to the queue in a sorted way
- dequeue(self) // TODO: return and remove the first element

### BST

#### Properties

- number_of_nodes // TODO: return the number total of the nodes in the __DS__
- min // TODO: return the min of the __DS__
- max // TODO: return the max of the __DS__

#### Methods

- empty(self) // TODO: return True if the __DS__ is empty
- clear(self) // TODO: clear the __DS__
- pre_order(self) // TODO: show the __DS__ in pre order
- in_order(self) // TODO: show the __DS__ in in order
- post_order(self) // TODO: show the __DS__ in post order
- append(self, data) // TODO: append a new node to the __DS__
- find(self, data) // TODO: return the number of how many the entered data found in the __DS__
- parent(self, data) // TODO: return parent node of the element // Note: its return the node not the data
- predecessor(self, data) // TODO: return the predecessor of the element // Note: its return the node not the data
- successor(self, data) // TODO: return the successor of the element // Note: its return the node not the data
- delete(self, data) // TODO: delete the node of the element from the __DS__ and replace it with successor

### Methods for all DSs except bst

- __str__(self) // USE: print([DS_name]) // TODO: display the __DS__
- __len__(self) // USE: len([DS_name]) // TODO: return the lenth of the __DS__
- empty(self) // TODO: return True if the __DS__ is empty
- clear(self) // TODO: clear the __DS__
- find(self, data) // TODO: return the number of how many the entered data found in the __DS__
- reverse(self) // TODO: return the reverse of the __DS__
- sort(self) // TODO: sort the __DS__ if its not sorted
- exchange(self, n) // TODO: circular permutation for n time

### classmethods for all DSs except bst

// USE: [DS] = [DS_type].method([DS1], [DS2])</br>
// Examples:</br>
__>>>__ stck3 = Stack.merge(stck1, stck2)</br>
__>>>__ Stack.swap([DS1], [DS2])</br>
__the tow DS parameters must be from the same DS__

- merge(cls, DS1, DS2) // TODO: return the merge of two DS in new DS
- swap(cls, DS1, DS2) // TODO: swap between DS1 and DS2 (DS1 will be DS2 and DS2 will be DS1)
