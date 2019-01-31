DISRIMINANT = "По дискриминанту"
DISRIMINANT_BY_FOUR = "По дискриминанту, делённому на четыре,"
FULL_SQUARE = "Раскладывается на полный квадрат"
VIET = "Возможно, по теореме Виета"
DECART = "По уcловию Декартового уравнения"
NO_ROOTS = "Нет корней"


def _transform(res):
    if str(res).replace('-', '').replace('.0', '').isdigit():
        return int(res)
    return res 


def roots_of_square_equation(a, b, c):
    from math import sqrt
    a, b, c = float(a), float(b), float(c)
    if a + b + c == 0:
        return DECART, ['1', _transform(c/a)]
    if a + c == b:
        return DECART, ['-1', _transform(-c/a)]
    if b**2 == 4*a*c:
        return FULL_SQUARE, _transform(-b/2*a)
    if b**2 < 4*a*c:
        return NO_ROOTS
    if b % 2 == 0:
        D_4 = (b/2)**2 - a*c
        x1 = (-b/2 + sqrt(D_4))/a
        x2 = (-b/2 - sqrt(D_4))/a
    else:
        D = b**2 - 4*a*c
        x1 = (-b + sqrt(D))/2*a
        x2 = (-b - sqrt(D))/2*a
    x1 = _transform(x1)
    x2 = _transform(x2)
    if 0 <= abs(x1) <= 10 and 0 <= abs(x2) <= 10 and \
       isinstance(x1, int) and isinstance(x2, int):
        return VIET, [x1, x2]
    if b % 2 == 0:
        return DISRIMINANT_BY_FOUR, [x1, x2]
    return DISRIMINANT, [x1, x2]


def roots_of_bisquare_equation(a, b, c):
    from math import sqrt
    res = roots_of_square_equation(a, b, c)
    if res == NO_ROOTS:
        return NO_ROOTS
    if res[0] == FULL_SQUARE:
        if res[1] >= 0:
            return FULL_SQUARE, [_transform(sqrt(res[1])), _transform(-sqrt(res[1]))]
        return NO_ROOTS
    md, [t1, t2] = res
    x_sp = []
    t1, t2 = float(t1), float(t2)
    if t1 >= 0:
        x_sp.extend([sqrt(t1), -sqrt(t1)])
    if t2 >= 0:
        x_sp.extend([sqrt(t2), -sqrt(t2)])
    if x_sp != []:
        return md, sorted(list(map(_transform, x_sp)))
    else:
        return NO_ROOTS
