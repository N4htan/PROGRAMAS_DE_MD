A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
C = {6, 12, 24, 33, 59, 45, 28, 79, 100, 101}

print("\nCONJUNTO A: ", A,"\nCONJUNTO B: ", B,"\nCONJUNTO C: ", C)

print ("\nCONJUNTO A, UNIÃO COM B: ", A.union(B))
print ("\nCONJUNTO A, UNIÃO COM C: ", A.union(C))
print ("\nCONJUNTO B, UNIÃO COM C: ", B.union(C))
print ("\nCONJUNTO A, UNIÃO COM B, UNIÃO COM C: ", A.union(B).union(C))

print ("\nCONJUNTO A, INTERSECÇÃO COM B: ", A.intersection(B))
print ("\nCONJUNTO A, INTERSECÇÃO COM C: ", A.intersection(C))
print ("\nCONJUNTO B, INTERSECÇÃO COM C: ", B.intersection(C))
print ("\nCONJUNTO A, INTERSECÇÃO COM B, INTERSECÇÃO COM C: ", A.intersection(B).intersection(C))

print ("\nCONJUNTO A, DIFERENÇA COM B: ", A.difference(B))
print ("\nCONJUNTO A, DIFERENÇA COM C: ", A.difference(C))
print ("\nCONJUNTO B, DIFERENÇA COM C: ", B.difference(C))
print ("\nCONJUNTO B, DIFERENÇA COM A: ", B.difference(A))
print ("\nCONJUNTO C, DIFERENÇA COM A: ", C.difference(A))
print ("\nCONJUNTO C, DIFERENÇA COM B: ", C.difference(B))
print ("\nCONJUNTO A, DIFERENÇA COM B, DIFERENÇA COM C: ", A.difference(B).difference(C))
print ("\nCONJUNTO B, DIFERENÇA COM A, DIFERENÇA COM C: ", B.difference(A).difference(C))
print ("\nCONJUNTO C, DIFERENÇA COM B, DIFERENÇA COM A: ", C.difference(B).difference(A))