# Group project notes

threads look like trees:

DISCUSSION TREE:
```
OP original_post (OP)
    \ A1 root_reply (user1 - root_challenger)
        \ A2 (OP - delta awarded)*
            \ A3 (bot)*
            \ A4 (user2)
                \ A5 (OP)
            
    \ B1 (user3) 
        \ B2 (OP)
            \ B3 (user4)
                \ B4 (OP)
                    \ B5 (user4)
                        \ B6 (OP)
                            \ B7 (user4)
                                \ B8 (OP)
                                    \ B9 (user4)
                                        \ B10 (OP)
                                            \ B11 (user4)
        \ B12 (user5)
      
```
*A1 is considered a leaf because A3 and A4 are the awarding of a delta. 


### Paths 
4 paths:
```
p1  A1*
p2  A1, A2, A4, A5
p3  B1, B2, B3, B4, B5, ... B11
p4  B1, B12
```
Path partipants
```
p1  user1, (op*)
p2  user1, op, user2
p3  user3, op, user4
p4  user3, user5
```

Adjacency matrix
```
    op  u1  u2  u3  u4  u5

op   x   o   o   o   o   x

u1   o   x   o   x   x   x

u2   o   o   x   x   x   x

u3   o   x   x   x   o   o

u4   o   x   x   o   x   x

u5   x   x   x   o   x   x
```


