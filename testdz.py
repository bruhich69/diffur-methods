from diffur_methods import yn3
import matplotlib.pyplot as plt


def fy1(sp):
    return sp


def fx1(sp):
    return sp


def fz1(sp):
    return sp


def fx2(arg, ysp, yco, xsp, xco, zsp, zco):
    return -xco


def fy2(arg, ysp, yco, xsp, xco, zsp, zco):
    return -yco


def fz2(arg, ysp, yco, xsp, xco, zsp, zco):
    return -zco


t = 0
tl = 1.57
dt = 0.001
y, x, z = 1, 1, 0
y1, x1, z1 = 0, 0, 1
graphx = [x]
graphy = [y]
graphz = [z]


while t < tl:
    g = yn3(fy2, fy1, fx2, fx1, fz2, fz1, t, y, y1, x, x1, z, z1, dt)
    y1 = g[0]
    y = g[1]
    x1 = g[2]
    x = g[3]
    z1 = g[4]
    z = g[5]
    graphx.append(x)
    graphy.append(y)
    graphz.append(z)
    t = t + dt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(graphx, graphy, graphz)
plt.show()
print(x, y, z, x1, y1, z1)
