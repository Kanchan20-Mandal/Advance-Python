
print("Welcome")

for i in range(1,25):
    print(f"print this line {i}")

def add(x,y):
     '''
    Inputs: Takes 2 inputs x and y
    Outputs: Returns one output that contains sum of x and y
    '''
     add=x+y
     return add

op_xy = add(23,67)
print(f"Output of add function is {op_xy}")

def simple_interest(p,n,r):
    """
    inputs: take inputs for principal amount, number of years, rate of interest per annum
    output: display simple interest for the above provided amounts
    """
    if isinstance(p,int|float) and isinstance(n,int|float) and isinstance(r,int|float):
        si = (p*n*r)/100
        return si
    else:
        print("Please provide integer/float data for respective inputs")

simp_intr=simple_interest(2500,6,5.4)
print(f"Output of Simple Interest Function: {simp_intr}")


simp_intr2 = simple_interest("string",6,4.3)
print(simp_intr2)








