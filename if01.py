def main(a):
    """
    If the number is positive, increase it to 1,otherwise leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    if a>0:
        a=a+1
    if a<0:
        a
    return a 
print(main(1))
print(main(-5))
