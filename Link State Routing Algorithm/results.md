## SIMPLE - CONNECTED NETWORK
### INPUT 
```
Enter the number of nodes: 4
Enter the number of edges: 4
Enter the node names (separated by spaces): A B C D 
A B 1
B C 1
C D 1
A C 4
```
### OUTPUT 
```
*** Link-State: Router A ***
Dest   Cost   NextHop  Path
---------------------------------
A      0      -        A
B      1      B        A->B
C      2      B        A->B->C
D      3      B        A->B->C->D

*** Link-State: Router B ***
Dest   Cost   NextHop  Path
---------------------------------
A      1      A        B->A
B      0      -        B
C      1      C        B->C
D      2      C        B->C->D

*** Link-State: Router C ***
Dest   Cost   NextHop  Path
---------------------------------
A      2      B        C->B->A
B      1      B        C->B
C      0      -        C
D      1      D        C->D

*** Link-State: Router D ***
Dest   Cost   NextHop  Path
---------------------------------
A      3      C        D->C->B->A
B      2      C        D->C->B
C      1      C        D->C
D      0      -        D
```

## DISCONNECTED NETWORK
### INPUT 
```
Enter the number of nodes: 4
Enter the number of edges: 3
Enter the node names (separated by spaces): A B C D
A B 1
B C 9
A C 11
```
### OUTPUT 
```
*** Link-State: Router A ***
Dest   Cost   NextHop  Path
---------------------------------
A      0      -        A
B      1      B        A->B
C      10     B        A->B->C
D      INF    -        No Path

*** Link-State: Router B ***
Dest   Cost   NextHop  Path
---------------------------------
A      1      A        B->A
B      0      -        B
C      9      C        B->C
D      INF    -        No Path

*** Link-State: Router C ***
Dest   Cost   NextHop  Path
---------------------------------
A      10     B        C->B->A
B      9      B        C->B
C      0      -        C
D      INF    -        No Path

*** Link-State: Router D ***
Dest   Cost   NextHop  Path
---------------------------------
A      INF    -        No Path
B      INF    -        No Path
C      INF    -        No Path
D      0      -        D
```

## NETWORK WITH A LOOP
### INPUT 
```
Enter the number of nodes: 4
Enter the number of edges: 4
Enter the node names (separated by spaces): A B C D
A B 1
B C 1
C D 1
D A 1
```
### OUTPUT 
```
*** Link-State: Router A ***
Dest   Cost   NextHop  Path
---------------------------------
A      0      -        A
B      1      B        A->B
C      2      D        A->D->C
D      1      D        A->D

*** Link-State: Router B ***
Dest   Cost   NextHop  Path
---------------------------------
A      1      A        B->A
B      0      -        B
C      1      C        B->C
D      2      A        B->A->D

*** Link-State: Router C ***
Dest   Cost   NextHop  Path
---------------------------------
A      2      D        C->D->A
B      1      B        C->B
C      0      -        C
D      1      D        C->D

*** Link-State: Router D ***
Dest   Cost   NextHop  Path
---------------------------------
A      1      A        D->A
B      2      A        D->A->B
C      1      C        D->C
D      0      -        D
```

## GRAPH WITH PARALLEL EDGES
### INPUT 
```
Enter the number of nodes: 3
Enter the number of edges: 4
Enter the node names (separated by spaces): A B C 
A B 1
A B 8
B C 2
A C 4
```
### OUTPUT
```
*** Link-State: Router A ***
Dest   Cost   NextHop  Path
---------------------------------
A      0      -        A
B      6      C        A->C->B
C      4      C        A->C

*** Link-State: Router B ***
Dest   Cost   NextHop  Path
---------------------------------
A      6      C        B->C->A
B      0      -        B
C      2      C        B->C

*** Link-State: Router C ***
Dest   Cost   NextHop  Path
---------------------------------
A      4      A        C->A
B      2      B        C->B
C      0      -        C
```

## INPUT WITH ERROR 1 ( INCORRECT FORMAT )
### INPUT
```
Enter the number of nodes: 5
Enter the number of edges: FIVE
```
### OUTPUT
```
Error reading input: invalid literal for int() with base 10: 'FIVE'. Please check the input format.
```

## INPUT WITH ERROR 2 ( NEGATIVE WEIGHT ) 
### INPUT 
```
Enter the number of nodes: 3
Enter the number of edges: 3
Enter the node names (separated by spaces): A B C
A B 1
B C -4
```
### OUTPUT 
```
Error reading input: Error: Negative weights are not allowed.. Please check the input format.
```
