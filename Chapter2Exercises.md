## Chapter 2
### Ex 2.1
What data structure - array or a linked list - will fit better for usage in financial consumption-tracking app? Adding data is used much more often than reading.

*For this app linked list with O(1) for data adding fits better than array with O(n).*

### Ex 2.2

*Linked list is more suitable structure for FIFO queue implementation than array. Insertions and delete are main operations in order table, they have O(1) estimated time for linked list.*

### Ex 2.3

*Sorted array is a convenient structure to store and search in users names. Estimated time for search operation is O(log(n)).*

### Ex 2.4

*Using binary search for finding accounts means work with a sorted array, so every insert will cause additional sorting operation. Array on its own has estimated time O(n) for insertion and with the drawback mentioned for a sorted array it turns out that this structure now is not optimized for accounts data storage.*

### Ex 2.5

*The structure is slower than array for search and faster for insertion, for linked list it has same insertion speed and greater speed for search.*
