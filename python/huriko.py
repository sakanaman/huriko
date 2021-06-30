import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm


m1 = 1.2
m2 = 0.1
l1 = 1.4
l2 = 1.2
g = 9.8
start_theta1 = 3.1
start_theta2 = -2.0
start_omega1 = 0.0
start_omega2 = 0.0
T = 30
n = 3000
h = T/n


def f1(a,b,c,d):
    return c

def f2(a,b,c,d):
    return d

def f3(a,b,c,d):
    det_under = (m1 + m2)*l1*l2*l2 - m2*l1*l2*l2*np.cos(a - b)*np.cos(a - b)

    A = -m2*l2*d*d*np.sin(a - b) - (m1 + m2)*g*np.sin(a)
    if np.isinf(A):
        print(b)
        exit()
    B = m2*l2*np.cos(a - b)
    C =  l1*l2*c*c*np.sin(a - b) - g*l2*np.sin(b)
    D = l2*l2
    det_above =  A*D - B*C

    return det_above/det_under

def f4(a,b,c,d):
    det_under = (m1 + m2)*l1*l2*l2 - m2*l1*l2*l2*np.cos(a - b)*np.cos(a - b)

    A = (m1 + m2) * l1
    B = -m2*l2*d*d*np.sin(a - b) - (m1 + m2)*g*np.sin(a)
    C = l1*l2*np.cos(a - b)
    D =  l1*l2*c*c*np.sin(a - b) - g*l2*np.sin(b)
    det_above = A*D - B*C

    return det_above/det_under


def f(t, a, b, c, d):
    return np.array([f1(a,b,c,d), f2(a,b,c,d), f3(a,b,c,d), f4(a,b,c,d)])

def solve_with_runge_kutta():

    alpha = delta = 1.0/8.0
    beta = ganma = 3.0/8.0
    p = q = 1.0/3.0
    t = -1.0/3.0
    r = 2.0/3.0
    s = u = v = z = 1.0
    w = -1.0

    U = np.zeros((n+1, 4))
    U[0] = [start_theta1, start_theta2, start_omega1, start_omega2]
    print(U)

    for i in range(n):
        ti = i * h
        ui = U[i]

        k1 = f(ti, ui[0], ui[1], ui[2], ui[3])

        param2 = U[i] + q*h*k1
        k2 = f(ti + p*h, param2[0], param2[1], param2[2], param2[3])

        param3 = U[i] + s*h*k2 + t*h*k1
        k3 = f(ti + r*h, param3[0], param3[1], param3[2], param3[3])

        param4 = U[i] + v*h*k3 + w*h*k2 + z*h*k1
        k4 = f(ti + u*h, param4[0], param4[1], param4[2], param4[3])

        U[i+1] = U[i] + h * (alpha * k1 + beta * k2 + ganma * k3 + delta * k4)

    return U


def update(frames, ax, data, dt):
    ax.clear()

    now_data = data[5 * frames]
    theta1 = now_data[0]
    theta2 = now_data[1]

    pos_a = np.array([l1*np.sin(theta1), -l1*np.cos(theta1)])
    pos_b = np.array([l2*np.sin(theta2), -l2*np.cos(theta2)]) + pos_a

    ax.set_ylim(-3,3)
    ax.set_xlim(-3,3)

    ax.plot([0,pos_a[0]],[0,pos_a[1]],color="green")
    ax.plot([pos_a[0],pos_b[0]],[pos_a[1],pos_b[1]],color="red")


if __name__ == "__main__":
    U = solve_with_runge_kutta()
    print(U)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    anime = anm.FuncAnimation(fig, update, fargs=(ax, U, h), frames=(n + 1)//5, interval=1)
    #anime.save("huriko.gif")

    plt.show()
