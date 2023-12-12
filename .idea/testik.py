def plus(a,b):
    schet = 0
    match schet:
        case 0:
            a = a + b
            return a
        case 1:
            b = a + b
        case 2:
            a = a*b
        case 3:
            b = a * b

print(plus(10, 25))