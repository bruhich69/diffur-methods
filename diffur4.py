import matplotlib.pyplot as plt
import numpy as np


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


def hmn(func2, func1, arg, neiz, proizv, shag, em):
    a1 = yn(func2, func1, arg, neiz, proizv, shag)[1]
    a2 = yn(func2, func1, arg, neiz, proizv, shag/2)
    a3 = yn(func2, func1, arg + shag/2, a2[1], a2[0], shag/2)[1]
    a4 = yn(func2, func1, arg + shag/2, a2[1], a2[0], shag/2)[0]
    eh = (16/15) * abs(a1 - a3)
    hmax = abs(em/eh)**0.2 * shag
    return [hmax, a4, a3]


def f2(arg, neiz):
    f = -neiz
    return f


def f1(arg, proiz):
    f = proiz
    return f


y0 = 1
y10 = 0
t0 = 0
tl = 12.56
h = tl - t0
y = y0
y1 = y10
t = t0
e = 0.000001
graphx = [t0]
graphy = [y]
graphy1 = [y1]

while t < tl:
    g = hmn(f2, f1, t, y, y1, h, e)
    hm = g[0]

    if hm < h / 2:
        h = 2 * hm
        continue

    else:
        y = g[2]
        y1 = g[1]
        t = t + h
        graphx.append(t)
        graphy.append(y)
        graphy1.append(y1)
        h = tl - t

plt.plot(graphx, graphy)
#plt.plot(graphx, graphy1)

xc = np.arange(t0, tl, 0.001)
yc = np.cos(xc)
ys = -np.sin(xc)
#plt.plot(xc, yc)
#plt.plot(xc, ys)

print(f"{y:.5f}")
plt.show()

# h > (tl - t0) / 100000 and