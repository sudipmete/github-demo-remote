# Add implementation
def add(x,y):
	return x+y
       
# Subtract implementation
def subtract(x,y):
	return x-y                 # on main branch
       
# Multiply implementation
def multiply(x,y):
	return x*y              # on Bug456 branch
    
# Divide implementation
def divide(x,y):
	if y==0:                # on Bug789 branch
        return DIVIDED_BY_0_ERROR
    else:
        return x/y

def square:
    pass                    # on Bug111 branch
