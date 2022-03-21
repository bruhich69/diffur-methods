# Метод Рунге - Кутта 4 - го порядка при 2 производной, зависящей только от y
def yn(func2, func1, arg, neiz, proiz, shag):
    k1 = shag * func1(arg, proiz)
    l1 = shag * func2(arg, neiz)
    k2 = shag * func1(arg + shag / 2, proiz + l1 / 2)
    l2 = shag * func2(arg + shag / 2, neiz + k1 / 2)
    k3 = shag * func1(arg + shag / 2, proiz + l2 / 2)
    l3 = shag * func2(arg + shag / 2, neiz + k2 / 2)
    k4 = shag * func1(arg + shag, proiz + l3)
    l4 = shag * func2(arg + shag, neiz + k3)
    neiz = neiz + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    proiz = proiz + (1/6) * (l1 + 2 * l2 + 2 * l3 + l4)
    return [proiz, neiz]


# Адаптация шага
def hmn(func2, func1, arg, neiz, proizv, shag, em):
    a1 = yn(func2, func1, arg, neiz, proizv, shag)[1]
    a2 = yn(func2, func1, arg, neiz, proizv, shag/2)
    a3 = yn(func2, func1, arg + shag/2, a2[1], a2[0], shag/2)[1]
    a4 = yn(func2, func1, arg + shag/2, a2[1], a2[0], shag/2)[0]
    eh = (16/15) * abs(a1 - a3)
    hmax = abs(em/eh)**0.2 * shag
    return [hmax, a4, a3]


# Метод Рунге - Кутта 4 - го порядка: одномерная задача
def yn1(func2, func1, arg, neiz, proiz, shag):
    k1 = shag * func1(arg, proiz, neiz)
    l1 = shag * func2(arg, proiz, neiz)
    k2 = shag * func1(arg + shag / 2, proiz + l1 / 2, neiz + k1 / 2)
    l2 = shag * func2(arg + shag / 2, proiz + l1 / 2, neiz + k1 / 2)
    k3 = shag * func1(arg + shag / 2, proiz + l2 / 2, neiz + k2 / 2)
    l3 = shag * func2(arg + shag / 2, proiz + l2 / 2, neiz + k2 / 2)
    k4 = shag * func1(arg + shag, proiz + l3, neiz + k3)
    l4 = shag * func2(arg + shag, proiz + l3, neiz + k3)
    neiz = neiz + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    proiz = proiz + (1 / 6) * (l1 + 2 * l2 + 2 * l3 + l4)
    return [proiz, neiz]


# Метод Рунге - Кутта 4 - го порядка: двумерная задача
def yn2(yfunc2, yfunc1, xfunc2, xfunc1, arg, yneiz, yproiz, xneiz, xproiz, shag):
    # k - neiz, l - proiz
    yk1 = shag * yfunc1(arg, yproiz, yneiz, xproiz, xneiz)
    yl1 = shag * yfunc2(arg, yproiz, yneiz, xproiz, xneiz)
    xk1 = shag * xfunc1(arg, yproiz, yneiz, xproiz, xneiz)
    xl1 = shag * xfunc2(arg, yproiz, yneiz, xproiz, xneiz)
    yk2 = shag * yfunc1(arg + shag / 2, yproiz + yl1 / 2, yneiz + yk1 / 2, xproiz + xl1 / 2, xneiz + xk1 / 2)
    yl2 = shag * yfunc2(arg + shag / 2, yproiz + yl1 / 2, yneiz + yk1 / 2, xproiz + xl1 / 2, xneiz + xk1 / 2)
    xk2 = shag * xfunc1(arg + shag / 2, yproiz + yl1 / 2, yneiz + yk1 / 2, xproiz + xl1 / 2, xneiz + xk1 / 2)
    xl2 = shag * xfunc2(arg + shag / 2, yproiz + yl1 / 2, yneiz + yk1 / 2, xproiz + xl1 / 2, xneiz + xk1 / 2)
    yk3 = shag * yfunc1(arg + shag / 2, yproiz + yl2 / 2, yneiz + yk2 / 2, xproiz + xl2 / 2, xneiz + xk2 / 2)
    yl3 = shag * yfunc2(arg + shag / 2, yproiz + yl2 / 2, yneiz + yk2 / 2, xproiz + xl2 / 2, xneiz + xk2 / 2)
    xk3 = shag * xfunc1(arg + shag / 2, yproiz + yl2 / 2, yneiz + yk2 / 2, xproiz + xl2 / 2, xneiz + xk2 / 2)
    xl3 = shag * xfunc2(arg + shag / 2, yproiz + yl2 / 2, yneiz + yk2 / 2, xproiz + xl2 / 2, xneiz + xk2 / 2)
    yk4 = shag * yfunc1(arg + shag, yproiz + yl3, yneiz + yk3, xproiz + xl3, xneiz + xk3)
    yl4 = shag * yfunc2(arg + shag, yproiz + yl3, yneiz + yk3, xproiz + xl3, xneiz + xk3)
    xk4 = shag * xfunc1(arg + shag, yproiz + yl3, yneiz + yk3, xproiz + xl3, xneiz + xk3)
    xl4 = shag * xfunc2(arg + shag, yproiz + yl3, yneiz + yk3, xproiz + xl3, xneiz + xk3)
    yneiz = yneiz + (1 / 6) * (yk1 + 2 * yk2 + 2 * yk3 + yk4)
    yproiz = yproiz + (1 / 6) * (yl1 + 2 * yl2 + 2 * yl3 + yl4)
    xneiz = xneiz + (1 / 6) * (xk1 + 2 * xk2 + 2 * xk3 + xk4)
    xproiz = xproiz + (1 / 6) * (xl1 + 2 * xl2 + 2 * xl3 + xl4)
    return [yproiz, yneiz, xproiz, xneiz]


#  Метод Рунге - Кутта 4 - го порядка: трехмерная задача
def yn3(yfunc2, yfunc1, xfunc2, xfunc1, zfunc2, zfunc1, arg, yneiz, yproiz, xneiz, xproiz, zneiz, zproiz, shag):
    # k - neiz, l - proiz
    yk1 = shag * yfunc1(yproiz)
    yl1 = shag * yfunc2(arg, yproiz, yneiz, xproiz, xneiz, zproiz, zneiz)
    xk1 = shag * xfunc1(xproiz)
    xl1 = shag * xfunc2(arg, yproiz, yneiz, xproiz, xneiz, zproiz, zneiz)
    zk1 = shag * zfunc1(zproiz)
    zl1 = shag * zfunc2(arg, yproiz, yneiz, xproiz, xneiz, zproiz, zneiz)
    yk2 = shag * yfunc1(yproiz + yl1 / 2)
    yl2 = shag * yfunc2(arg + shag / 2, yproiz + yl1 / 2, yneiz + yk1 / 2, xproiz + xl1 / 2, xneiz + xk1 / 2, zproiz + zl1 / 2, zneiz + zk1 / 2)
    xk2 = shag * xfunc1(xproiz + xl1 / 2)
    xl2 = shag * xfunc2(arg + shag / 2, yproiz + yl1 / 2, yneiz + yk1 / 2, xproiz + xl1 / 2, xneiz + xk1 / 2, zproiz + zl1 / 2, zneiz + zk1 / 2)
    zk2 = shag * zfunc1(zproiz + zl1 / 2)
    zl2 = shag * zfunc2(arg + shag / 2, yproiz + yl1 / 2, yneiz + yk1 / 2, xproiz + xl1 / 2, xneiz + xk1 / 2, zproiz + zl1 / 2, zneiz + zk1 / 2)
    yk3 = shag * yfunc1(yproiz + yl2 / 2)
    yl3 = shag * yfunc2(arg + shag / 2, yproiz + yl2 / 2, yneiz + yk2 / 2, xproiz + xl2 / 2, xneiz + xk2 / 2, zproiz + zl2 / 2, zneiz + zk2 / 2)
    xk3 = shag * xfunc1(xproiz + xl2 / 2)
    xl3 = shag * xfunc2(arg + shag / 2, yproiz + yl2 / 2, yneiz + yk2 / 2, xproiz + xl2 / 2, xneiz + xk2 / 2, zproiz + zl2 / 2, zneiz + zk2 / 2)
    zk3 = shag * zfunc1(zproiz + zl2 / 2)
    zl3 = shag * zfunc2(arg + shag / 2, yproiz + yl2 / 2, yneiz + yk2 / 2, xproiz + xl2 / 2, xneiz + xk2 / 2, zproiz + zl2 / 2, zneiz + zk2 / 2)
    yk4 = shag * yfunc1(yproiz + yl3)
    yl4 = shag * yfunc2(arg + shag, yproiz + yl3, yneiz + yk3, xproiz + xl3, xneiz + xk3, zproiz + zl3, zneiz + zk3)
    xk4 = shag * xfunc1(xproiz + xl3)
    xl4 = shag * xfunc2(arg + shag, yproiz + yl3, yneiz + yk3, xproiz + xl3, xneiz + xk3, zproiz + zl3, zneiz + zk3)
    zk4 = shag * zfunc1(zproiz + zl3)
    zl4 = shag * zfunc2(arg + shag, yproiz + yl3, yneiz + yk3, xproiz + xl3, xneiz + xk3, zproiz + zl3, zneiz + zk3)
    yneiz = yneiz + (1 / 6) * (yk1 + 2 * yk2 + 2 * yk3 + yk4)
    yproiz = yproiz + (1 / 6) * (yl1 + 2 * yl2 + 2 * yl3 + yl4)
    xneiz = xneiz + (1 / 6) * (xk1 + 2 * xk2 + 2 * xk3 + xk4)
    xproiz = xproiz + (1 / 6) * (xl1 + 2 * xl2 + 2 * xl3 + xl4)
    zneiz = zneiz + (1 / 6) * (zk1 + 2 * zk2 + 2 * zk3 + zk4)
    zproiz = zproiz + (1 / 6) * (zl1 + 2 * zl2 + 2 * zl3 + zl4)
    return[yproiz, yneiz, xproiz, xneiz, zproiz, zneiz]
