def fibonacci(n, computed={}):
    if n < 2:
        return n
    elif n in computed:  
        return computed[n]
    else:
        # save the new fibonacci seq in the map.
        computed[n] = fibonacci(n-1) + fibonacci(n-2)
        return computed[n]
    
n = int(raw_input())
print(fibonacci(n))
