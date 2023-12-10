balans = input()
def balanss(balans):
    stack = []
    brackt_baz = '<[{('
    brackt_baste = '>]})'
    map = {')':'(' , ']':'[' ,'}':'{' , '>':'<' }

    for i in balans:
        if i in brackt_baz:
            stack.append(i)
        elif i in brackt_baste:
            if not stack or stack.pop() != map[i] :
                return False
    return not stack

print (balanss(balans))
