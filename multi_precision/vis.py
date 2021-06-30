import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm

f = open("output.txt", "r")
data = f.readlines()
f.close()


rate = 100

theta1 = np.zeros(60000 // rate)
theta2 = np.zeros(60000 // rate)


for i in range(60000 // rate):
    t1,t2 = data[i * rate].split(" ")
    theta1[i] = t1
    theta2[i] = t2



def update(frames):
    ax.clear()

    pos_a = np.array([1.4*np.sin(theta1[frames]), -1.4*np.cos(theta1[frames])])
    pos_b = np.array([1.2*np.sin(theta2[frames]), -1.2*np.cos(theta2[frames])]) + pos_a

    ax.set_ylim(-3,3)
    ax.set_xlim(-3,3)

    ax.plot([0,pos_a[0]],[0,pos_a[1]],color="green")
    ax.plot([pos_a[0],pos_b[0]],[pos_a[1],pos_b[1]],color="red")



if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    anime = anm.FuncAnimation(fig, update, frames=60000//rate, interval=10)
    # anime.save("huriko.gif")

    plt.show()