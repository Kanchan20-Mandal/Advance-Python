# Calculate Simpe Interest
def simple_interest(p:float|int,n:int,r:float|int)->tuple:
    """
    Inputs:
    p: Principal in INR
    n: Number of years
    r: Rate of interest in percent per annum
    Output: interest, amount
    """
    i=(p*n*r)/100
    a=p+i
    return i, a

# Take input p,n,r from user
p=float(input("Enter principal in INR: "))
n=int(input("Please enter number of years: "))
r=float(input("Please enter rate of interest in %pa:"))

# Call the simple interest
i, a= simple_interest(p,n,r)
p
#Print the Interest and amount
print(f"Simple Interest : {i:.2f} INR")
print(f"Amount : {a:.2f} INR")
