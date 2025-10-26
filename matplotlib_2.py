import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.plot(x,y)
plt.show()
#adding formatting to the line
plt.plot(x,y,"ro")
plt.show()

#green triangles
plt.plot(x,y,"g^")
plt.show()

#blue dotted line "b-" -> default straight line
plt.plot(x,y,"b--")
plt.show()

#how to limit the numbers on each axis
plt.plot(x,y)
plt.axis([0,10,0,200]) #x1 to xn, y1 to yn
plt.show()

#add labels, titles, line width, and legend
plt.plot(x,y,"r--",label="Y = X",linewidth = 10)
plt.axis([0,10,0,50])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("SAMPLE GRAPH!!!!!!!!!!!!!!!!!!!!!")
plt.legend()
plt.show()

#plotting multiple graphs on a single plot
plt.plot([1,2,3,4,5],[1,4,9,16,25],"r--",label = "Y=X^2",linewidth = 5)
plt.plot([1,2,3,4,5],[1,8,27,64,125],"g--",label = "Y=X^3",linewidth = 10)
plt.axis([0,30,0,200])
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.title("MULTIPLE SAMPLE GRAPH")
plt.legend()
plt.show()


import numpy as np
x = np.arange(0,10,0.2)
print(x)
y1 = x**2
y2 = x**3
plt.plot(x,y1,"g--",x,y2,"r--")
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.title("PARABOLA")
plt.legend()
plt.show()
