def multiply_basic(poly1,poly2):
    m=len(poly1)
    n=len(poly2)
    prod = [0] * (m + n - 1);
    for i in range(m):
        for j in range(n):
            prod[i + j] += poly1[i] * poly2[j];
 
    return prod

def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
            
    return result

def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly



def multiply_optimized(poly1,poly2):
    n = max(len(poly1), len(poly2))
    
    if len(poly1) == 1:
        return [poly1[0] * i for i in poly2]
    elif len(poly2) == 1:
        return [poly2[0] * i for i in poly1]
    elif (len(poly1) == 0) or (len(poly2) == 0):
        return [0] * n
    
    (A0, A1), (B0, B1) = split(poly1, poly2)
    
    Y = multiply_optimized(add(A0, A1), add(B0, B1))
    U = multiply_optimized(A0, B0)
    Z = multiply_optimized(A1, B1)
    Y_U_Z = add(Y, [-1 * i for i in add(U, Z)])
    
    result = add(add(U, increase_exponent(Y_U_Z, n//2)), increase_exponent(Z, 2*(n//2)))
    
    return result
