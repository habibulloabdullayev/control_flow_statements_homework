def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0 and a%2==1:
        print('positive odd number')
    if a>0 and a%2==0:
        print('positive even number')
    if a<0 and a%2==1:
        print('negative odd number')
    if a<0 and a%2==0:
        print('negative even number')
    return '    '
print(main(57))
print(main(-24))