import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

days = [1,2,3,4,5]
eating = [2,3,4,3,2]
sleeping = [7,8,6,11,7]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[],color = "m",label = "Eating",linewidth = 5)#change 5 to 15 see output
plt.plot([],[],color = "c",label = "Sleeping",linewidth = 5)
plt.plot([],[],color = "r", label = "Working", linewidth = 5)
plt.plot([],[],color = "g",label = "Playing",linewidth = 5)
plt.stackplot(days,eating,sleeping,working,playing,colors = ["m","c","r","g"])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("RANDOM STACK PLOT")
plt.legend()
plt.show()

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0,5,0.1)
print(f't1 = {t1}\n')
t2 = np.arange(0,5,0.02)
print(f't2 = {t2}\n')

plt.figure()
plt.subplot(2,2,1)#2 rows, 2 columns, index of subplot = 1
plt.plot(t1,f(t1),"bo")

plt.subplot(2,2,3)
plt.plot(t2,np.cos(2*np.pi*t2),"r")
plt.show()
