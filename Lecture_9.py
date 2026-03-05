# Anonymous Function
def do_twice(n,fn):
    return fn(fn(n))                # Here it had created three environment as there is a function call inside return
print(do_twice(3,lambda x: x**2))

