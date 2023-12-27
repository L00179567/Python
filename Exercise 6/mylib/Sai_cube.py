cube_text = "Cube of A after import="

def cube(A):
    return A*A*A

print("Cube of A is=",cube(2))

if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    print(f"This module is called {__name__} and is being called by another script")
    