import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm

f_1024 = open("output_1024.txt", "r")
data_1024 = f_1024.readlines()
f_1024.close()

f_64 = open("output_64.txt","r")
data_64 = f_64.readlines()
f_64.close()

f_32 = open("output_32.txt","r")
data_32 = f_32.readlines()
f_32.close()


rate = 100

theta1_1024 = np.zeros(600000 // rate)
theta2_1024 = np.zeros(600000 // rate)

theta1_64 = np.zeros(600000 // rate)
theta2_64 = np.zeros(600000 // rate)

theta1_32 = np.zeros(600000 // rate)
theta2_32 = np.zeros(600000 // rate)


for i in range(600000 // rate):
    t1_1024,t2_1024 = data_1024[i * rate].split(" ")
    theta1_1024[i] = t1_1024
    theta2_1024[i] = t2_1024

    t1_64,t2_64 = data_64[i * rate].split(" ")
    theta1_64[i] = t1_64
    theta2_64[i] = t2_64

    t1_32,t2_32 = data_32[i * rate].split(" ")
    theta1_32[i] = t1_32
    theta2_32[i] = t2_32



def update(frames):
    ax.clear()
    ax.set_ylim(-3,3)
    ax.set_xlim(-3,3)

    pos_a = np.array([1.4*np.sin(theta1_1024[frames]), -1.4*np.cos(theta1_1024[frames])])
    pos_b = np.array([1.2*np.sin(theta2_1024[frames]), -1.2*np.cos(theta2_1024[frames])]) + pos_a
    ax.plot([0,pos_a[0]],[0,pos_a[1]],color="green")
    ax.plot([pos_a[0],pos_b[0]],[pos_a[1],pos_b[1]],color="green", label = "1024bit")

    pos_a = np.array([1.4*np.sin(theta1_64[frames]), -1.4*np.cos(theta1_64[frames])])
    pos_b = np.array([1.2*np.sin(theta2_64[frames]), -1.2*np.cos(theta2_64[frames])]) + pos_a
    ax.plot([0,pos_a[0]],[0,pos_a[1]],color="blue")
    ax.plot([pos_a[0],pos_b[0]],[pos_a[1],pos_b[1]],color="blue", label = "64bit")

    pos_a = np.array([1.4*np.sin(theta1_32[frames]), -1.4*np.cos(theta1_32[frames])])
    pos_b = np.array([1.2*np.sin(theta2_32[frames]), -1.2*np.cos(theta2_32[frames])]) + pos_a
    ax.plot([0,pos_a[0]],[0,pos_a[1]],color="red")
    ax.plot([pos_a[0],pos_b[0]],[pos_a[1],pos_b[1]],color="red", label = "32bit")



    ax.legend()
    


if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    anime = anm.FuncAnimation(fig, update, frames=600000//rate, interval=10)
    # anime.save("huriko.gif")
    plt.show()