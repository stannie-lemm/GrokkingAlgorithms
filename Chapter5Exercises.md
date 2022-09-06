## Chapter 5

### Which of following hash-functions are consistent?
### Ex 5.1
f(x) = 1

*Returns the only one index for all the elements. Consistent.*

### Ex 5.2
f(x) = rand()

*Can return different random indexes for the same element. Not consistent.*

### Ex 5.3
f(x) = next_empty_slot()

*Every time returns different address. Not consistent.*

### Ex 5.4
f(x) = len(x)

*The length of the string does not change, returns same indexes for same X values. Consistent.*

###  Given 4 Hash-functions, needed to tell in which cases hash-table will be well-distributed

### Ex 5.5
Phone table, with names as keys and numbers as values. Names are: Esther, Ben, Bob, Den.

*A will cause 3 collisions, B - 2, C will cause only one collision and D - no collisions.*

### Ex 5.6
Connection of battery size and its voltage. Sizes are: A, AA, AAA, AAAA.

*A will cause 3 collisions, B - no collisions, C - 3 collisions, D - no collisions*

### Ex 5.7
Connection of book names with its authors names. Book names: "Maus", "Fun Home", "Watchmen".

*C and D will cause no collisions*
