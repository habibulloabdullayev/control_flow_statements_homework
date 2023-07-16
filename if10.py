def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<0:
        print('freezing')
    if temp>0 and temp<11:
        print('very cold')
    if temp>10 and temp<21:
        print('cold')
    if temp>20 and temp<31:
        print('normal')
    if temp>30 and temp<41:
        print('hot')
    if temp>40:
        print('very hot')
    return '  '
print(main(21))
print(main(-4))