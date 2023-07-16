def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a%2==1 and (a//10>0 and a//10<10):
        print('two-digit odd number')
    if a%2==0 and (a//10>0 and a//10<10):
        print('two-digit even number')
    if a%2==1 and (a//100>0 and a//100<10):
        print('three-digit odd number')
    if a%2==0 and (a//100>0 and a//100<10):
        print('three-digit even number')
    if a%2==1 and (a//100<0 and a//100>-10):
        print('three-digit odd number')
    if a%2==0 and (a//100<0 and a//100>-10):
        print('three-digit even number')
    return '   '
print(main(57))
print(main(-242))