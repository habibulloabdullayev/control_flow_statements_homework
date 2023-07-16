def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    y=0
    x=0
    if a>0:
        x=x+1
    if b>0:
        x=x+1
    if c>0:
        x=x+1
    if a<0:
        y=y+1
    if b<0:
        y=y+1
    if c<0:
        y=y+1
    if x>y:
        print('there are a lot of positive numbers')
    if y>x:
        print('there are a lot of negative numbers')
    return  "   "
print(main(-2,4,1))
print(main(3,-3,-6))