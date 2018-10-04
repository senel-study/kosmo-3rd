def comma(money):
    if money.find("-") is 0:
        isMinus = True
        money = money[1:]
    elif money.find("-") > 0:
        return "Wrong Number"
    else:
        isMinus = False
    
    if money.find(".") > 0 :
        isDecimal = True
        dot = money.find(".")
        decimal = money[dot:] 
        money = money[:dot]
    elif money.find(".") is 0:
        return "Wrong Number"
    else : 
        isDecimal = False
    
    rs = list(money)
    rs.reverse()
    for i, _ in enumerate(rs):
        if i%3==2 and i is not len(rs)-1:
            rs[i] = "," + rs[i]
    rs.reverse()
    result = "".join(rs)

    if isMinus:
        result = "-" + result

    if isDecimal:
        result = result + decimal

    return result


test_list = ["1000", "20000000", "-3245.24"]
result = [comma(s) for s in test_list]
# result = comma("-3245.24")
print(result)