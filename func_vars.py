#!/usr/bin/env python

 # You'd think L would stay local, but the return changes all that !
 
def var_acc(a, L=[]):
    L.append(a)
    return L

print var_acc(1)
print var_acc(2)
print var_acc(3)