## Chapter 1
### Ex 1.1
With sorted list of 128 names what maximal number of checks is needed to find a certain name with binary search?

*Binary search is working with O(log(n)), so maximal number of checks is log(128) = 7.*

### Ex 1.2
If length of the list is doubled how will change the number of checks?

*Maximal number of checks is log(128\*2) = 8.*

### Ex 1.3
Knowing last name it is needed to find phone number in the phone book. What is estimated time O() of search?

*We can use binary search to find a needed name in the book, so estimated time is O(log(n)).*

### Ex 1.4
What is estimated time O for search of name in the phone book with knowledge of phone number?

*To find needed phone number we should look through all the table, so estimated time is O(n).*

### Ex 1.5
It is required to read all the phone numbers in the phone book. What is estimated time of this search?

*As far as we need to look through the whole book the estimated time will be O(n).*

### Ex 1.6
It is required to read all the phone numbers of people with name starting from A. What is estimated time of this operation?

*The answer is O(n). It is easy to suppose that estimated time will decrease, comparing to last exercise - we have only one letter of 26. However, simple arithmetic operations such as addiction, multiplication and division do not influence big-O estimation. In worst case we can have all the book containing only A-starting names.*
