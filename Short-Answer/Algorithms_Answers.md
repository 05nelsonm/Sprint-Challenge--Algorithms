#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)  
Will only go for n number of times, so run time complexity doesn't change.


b) O(n^2)  
Inner loop running dependant on the outer loop.


c) O(n)  
Runs once

## Exercise II
I would use a binary search:
- Cut the number of floors in half from floor 0 to top and drop egg.
- Continue cutting number of floors in half from floor 0 to the last
cut you did, and drop an egg.
  - Do until a floor is found where it doesn't break.
- When it doesn't break, check the floors above between current floor
and where the last cut occurred.
- When you hit a floor where the egg breaks again, the floor - 1 is the
magic num.

- Runtime complexity of this is O(log n)


