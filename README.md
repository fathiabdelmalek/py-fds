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

<details><summary>List</summary>

<details><summary>Properties</summary>

- first // TODO: return the data in the first node
- last // TODO: return the data in the last node

</details>
<details><summary>Methodes</summary>

- insert(data, pos) // TODO: add node in the entered position (pos=0 => add in the begining) // the default value is set to 0
- append(data) // TODO: add node in the end
- delete(data) // TODO: delete all nodes hav the entered data
- remove(pos=0) // TODO: return and remove node in the entered position (pos=0 => remove first node, pos=-1 => remove last node)

</details>
</details>
<details><summary>DList</summary>

<details><summary>Properties</summary>

- first // TODO: return the data in the first node
- last // TODO: return the data in the last node

</details>
<details><summary>Methodes</summary>

- add_begin(data) // TODO: add a node to the begin
- add_fin(data) // TODO: add a node to the fin
- delete(data) // TODO: delete all nodes hav the entered data
- remove(pos) // TODO: return and remove node in the entered position (pos=0 => remove first node, pos=-1 => remove last node) // the default value is set to 0

</details>
</details>
<details><summary>SList</summary>

<details><summary>Properties</summary>

- first // TODO: return the data in the first node
- last // TODO: return the data in the last node

</details>
<details><summary>Methodes</summary>

- append(data) // TODO: add a node to the list in a sorted way
- delete(data) // TODO: delete all nodes hav the entered data
- remove(pos) // TODO: return and remove node in the entered position (pos=0 => remove first node, pos=-1 => remove last node) // the default value is set to 0

</details>
</details>
<details><summary>Stack</summary>

<details><summary>Properties</summary>

- top // TODO: return the data in the first node

</details>
<details><summary>Methodes</summary>

- push(data) // TODO: add a node to the top
- pop() // TODO: return and remove the node in the top

</details>
</details>
<details><summary>Queue</summary>

<details><summary>Properties</summary>

- front // TODO: return the data in the first node
- back // TODO: return the data in the last node

</details>
<details><summary>Methods</summary>

- enqueue(data) // TODO: add a node to the end
- dequeue() // TODO: return and remove the first element

</details>
</details>
<details><summary>PQueue</summary>

<details><summary>Properties</summary>

- front // TODO: return the data in the first node
- back // TODO: return the data in the last node

</details>
<details><summary>Methods</summary>

- enqueue(data) // TODO: add a node to the queue in a sorted way
- dequeue() // TODO: return and remove the first element

</details>
</details>
<details><summary>methods for all DSs</summary>

- __str__() // USE: print([DS_name]) // TODO: display the __DS__
- __len__() // USE: len([DS_name]) // TODO: return the lenth of the __DS__
- empty() // TODO: return True if the __DS__ is empty
- clear() // TODO: clear the __DS__
- find(data) // TODO: return the number of how many the entered data found in the __DS__
- reverse() // TODO: return the reverse of the __DS__
- sort() // TODO: sort the __DS__ if its not sorted
- exchange(n) // TODO: circular permutation for n time
- equals(DS) // TODO: return True if `DS` is equal to __this DS__

</details>
<details><summary>classmethods for all DSs</summary>

// USE: [DS] = [DS_type].method([DS1], [DS2])<br>
// Examples:<br>
`stck3 = Stack.merge(stck1, stck2)`<br>
`Stack.swap([DS1], [DS2])`<br>
__the tow DS parameters must be from the same DS__
- merge(DS1, DS2) // TODO: return the merge of two __DSs__ in new __DS__
- swap(DS1, DS2) // TODO: swap between DS1 and DS2 (`DS1` will be `DS2` and `DS2` will be `DS1`)

</details>

#### Note :
(reverse, sort, exchange) are not supported in this __DS__ because they brake the rule of the __Sorted Linked List__

<details><summary>BST</summary>

<details><summary>properties</summary>

- number_of_nodes // TODO: return the number of nodes in the __BST__
- number_of_liefs // TODO: return the number of liefs (nodes without any children) in the __BST__
- height // TODO: return the height of the __BST__
- max // TODO: return the maximum value in the __BST__
- min // TODO: return the minimum value in the __BST__

</details>
<details><summary>methodes</summary>

- pre_order() // TODO: represent the __BST__ in pre_order way
- in_order() // TODO: represent the __BST__ in in_order way
- post_order() // TODO: represent the __BST__ in post_order way
- append(data) // TODO: append a new node to the __BST__ if not exist
- find(data) // TODO: search for an element in the __BST__ and return it if exist 
- parent(data) // TODO: return the parent node of an element if exist
- successor(data) // TODO: return the next value in the __BST__ if exist
- predecessor(data) // TODO: return the previous value in the __BST__ if exist
- delete(data) // TODO: delete an element from the __BST__ if exist
- equals(bst) // TODO: return True if `bst` is equal to __this BST__ (__this BST__ is the  same as `bst`)

</details>
</details>
