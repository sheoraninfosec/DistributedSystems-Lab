sheoraninfosec@Mac Assignment2 % /usr/local/bin/python3 "/Users/sheoraninfosec/Documents/Masters UPES/Distributed Systems/Assignment2/dvr_algorithm.py"


Enter the number of nodes: 5
Enter the number of edges: 5
Enter the node names (separated by spaces): A B C D E
A B 1
A D 1
A E 7
B C 1
C D 1
-- Initial State of Routing Tables --
*** Distance-Vector: Router A ***
Dest   Cost   NextHop  Path
-----------------------------------
A      0      A        A
B      1      B        A->B
C      INF    -        No Path
D      1      D        A->D
E      7      E        A->E

*** Distance-Vector: Router B ***
Dest   Cost   NextHop  Path
-----------------------------------
A      1      A        B->A
B      0      B        B
C      1      C        B->C
D      INF    -        No Path
E      INF    -        No Path

*** Distance-Vector: Router C ***
Dest   Cost   NextHop  Path
-----------------------------------
A      INF    -        No Path
B      1      B        C->B
C      0      C        C
D      1      D        C->D
E      INF    -        No Path

*** Distance-Vector: Router D ***
Dest   Cost   NextHop  Path
-----------------------------------
A      1      A        D->A
B      INF    -        No Path
C      1      C        D->C
D      0      D        D
E      INF    -        No Path

*** Distance-Vector: Router E ***
Dest   Cost   NextHop  Path
-----------------------------------
A      7      A        E->A
B      INF    -        No Path
C      INF    -        No Path
D      INF    -        No Path
E      0      E        E


Starting Distance-Vector Algorithm.........

--- Iteration 1 ---
  Table for Router A updated.
  Table for Router B updated.
  Table for Router C updated.
  Table for Router D updated.
  Table for Router E updated.
-------------------------
--- Iteration 2 ---
-------------------------

Convergence achieved after 1 update iterations.

*** Distance-Vector: Router A ***
Dest   Cost   NextHop  Path
-----------------------------------
A      0      A        A
B      1      B        A->B
C      2      B        A->B->C
D      1      D        A->D
E      7      E        A->E

*** Distance-Vector: Router B ***
Dest   Cost   NextHop  Path
-----------------------------------
A      1      A        B->A
B      0      B        B
C      1      C        B->C
D      2      A        B->A->D
E      8      A        B->A->E

*** Distance-Vector: Router C ***
Dest   Cost   NextHop  Path
-----------------------------------
A      2      B        C->B->A
B      1      B        C->B
C      0      C        C
D      1      D        C->D
E      9      B        C->B->A->E

*** Distance-Vector: Router D ***
Dest   Cost   NextHop  Path
-----------------------------------
A      1      A        D->A
B      2      A        D->A->B
C      1      C        D->C
D      0      D        D
E      8      A        D->A->E

*** Distance-Vector: Router E ***
Dest   Cost   NextHop  Path
-----------------------------------
A      7      A        E->A
B      8      A        E->A->B
C      9      A        E->A->B->C
D      8      A        E->A->D
E      0      E        E

sheoraninfosec@Mac Assignment2 % /usr/local/bin/python3 "/Users/sheoraninfosec/Document
s/Masters UPES/Distributed Systems/Assignment2/dvr_algorithm.py"
Enter the number of nodes: 5
Enter the number of edges: 4
Enter the node names (separated by spaces): A B C D E
A B 1
A D 1
B C 1
C D 1
-- Initial State of Routing Tables --
*** Distance-Vector: Router A ***
Dest   Cost   NextHop  Path
---------------------------------
A      0      A        A
B      1      B        A->B
C      INF    -        No Path
D      1      D        A->D
E      INF    -        No Path

*** Distance-Vector: Router B ***
Dest   Cost   NextHop  Path
---------------------------------
A      1      A        B->A
B      0      B        B
C      1      C        B->C
D      INF    -        No Path
E      INF    -        No Path

*** Distance-Vector: Router C ***
Dest   Cost   NextHop  Path
---------------------------------
A      INF    -        No Path
B      1      B        C->B
C      0      C        C
D      1      D        C->D
E      INF    -        No Path

*** Distance-Vector: Router D ***
Dest   Cost   NextHop  Path
---------------------------------
A      1      A        D->A
B      INF    -        No Path
C      1      C        D->C
D      0      D        D
E      INF    -        No Path

*** Distance-Vector: Router E ***
Dest   Cost   NextHop  Path
---------------------------------
A      INF    -        No Path
B      INF    -        No Path
C      INF    -        No Path
D      INF    -        No Path
E      0      E        E


Starting Distance-Vector Algorithm.........

--- Iteration 1 ---
  Table for Router A updated.
  Table for Router B updated.
  Table for Router C updated.
  Table for Router D updated.
-------------------------
--- Iteration 2 ---
-------------------------

Convergence achieved after 1 update iterations.

*** Distance-Vector: Router A ***
Dest   Cost   NextHop  Path
---------------------------------
A      0      A        A
B      1      B        A->B
C      2      B        A->B->C
D      1      D        A->D
E      INF    -        No Path

*** Distance-Vector: Router B ***
Dest   Cost   NextHop  Path
---------------------------------
A      1      A        B->A
B      0      B        B
C      1      C        B->C
D      2      A        B->A->D
E      INF    -        No Path

*** Distance-Vector: Router C ***
Dest   Cost   NextHop  Path
---------------------------------
A      2      B        C->B->A
B      1      B        C->B
C      0      C        C
D      1      D        C->D
E      INF    -        No Path

*** Distance-Vector: Router D ***
Dest   Cost   NextHop  Path
---------------------------------
A      1      A        D->A
B      2      A        D->A->B
C      1      C        D->C
D      0      D        D
E      INF    -        No Path

*** Distance-Vector: Router E ***
Dest   Cost   NextHop  Path
---------------------------------
A      INF    -        No Path
B      INF    -        No Path
C      INF    -        No Path
D      INF    -        No Path
E      0      E        E

sheoraninfosec@Mac Assignment2 % /usr/local/bin/python3 "/Users/sheoraninfosec/Document
s/Masters UPES/Distributed Systems/Assignment2/dvr_algorithm.py"
Enter the number of nodes: 5
Enter the number of edges: 5
Enter the node names (separated by spaces): A B C D E
A B ONE
Error reading input: invalid literal for int() with base 10: 'ONE'. Please check the input format.
sheoraninfosec@Mac Assignment2 % /usr/local/bin/python3 "/Users/sheoraninfosec/Document
s/Masters UPES/Distributed Systems/Assignment2/dvr_algorithm.py"
Enter the number of nodes: 4
Enter the number of edges: 3
Enter the node names (separated by spaces): A B C D
A B 1
B C 1
C D -5
Error reading input: Error: Negative weights are not allowed.. Please check the input format.
