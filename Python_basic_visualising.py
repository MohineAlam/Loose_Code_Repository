#!/usr/bin/env python


#------------- simple line graph
#import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

#plt.plot(x, y)
#plt.title("Basic line plot")
#plt.xlabel("x-axis")
#plt.ylabel("y-axis")
#plt.show()


#------------ simple scatter plot
#import matplotlib.pyplot as plt
#import numpy as np

#x = np.random.rand(50)
#y = np.random.rand(50)

#plt.scatter(x, y)
#plt.title("Basic sactter plot")
#plt.xlabel("x-axis")
#plt.ylabel("y-axis")
#plt.show()


#---------- simple bar chart
#import matplotlib.pyplot as plt

x = ["a", "b", "c", "d"]
y = [10, 24, 36, 18]

#plt.bar(x, y)
#plt.title("Basic bar chart")
#plt.xlabel("x-axis")
#plt.ylabel("y-axis")
#plt.show()


#-------- simple histogram
#import matplotlib.pyplot as plt
#import numpy as np

#data = np.random.normal(loc = 0, scale = 100, size = 10000) #loc = centre of distribution, scale = spread (standard deviation), size = shape of output array
#plt.hist(data, bins = 100)
#plt.title("Basic histogram")
#plt.xlabel("x-axis")
#plt.ylabel("y-axis")
#plt.show()


#-------- simple multiple line plots
#import matplotlib.pyplot as plt

#x = range(10)
#y1 = [v**2 for v in x]
#y2 = [v**1.5 for v in x]

#plt.plot(x, y1, label = "x^2")
#plt.plot(x, y2, label = "x^(3/2)")
#plt.title("Basic multiple line plot")
#plt.legend()
#plt.show()


#--------- simple subplots (2x2 grid)
#import matplotlib.pyplot as plt
#import numpy as np

#x = np.linspace(0, 10, 100)
#y1 = np.sin(x)
#y2 = np.cos(x)
#y3 = np.tan(x)
#y4 = np.exp(x/10)

#fig, axes = plt.subplots(2, 2, figsize=(8,6))

#axes[0,0].plot(x, y1, color = "blue")
#axes[0,0].set_title("sin(x)")

#axes[0,1].plot(x, y2, color = "red")
#axes[0,1].set_title("cos(x)")

#axes[1,0].plot(x, y3)
#axes[1,0].set_title("tan(x)")

#axes[1,1].plot(x, y4)
#axes[1,1].set_title("exp(x/10)")

#plt.tight_layout()
#plt.show()

#--------- simple annotations
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [2, 4, 1, 8]

plt.plot(x, y, marker="o")

# annotate highest point
max_x = x[y.index(max(y))]
max_y = max(y)

plt.annotate(
	"Peak",
	xy=(max_x, max_y),
	xytext=(max_x + 0.3, max_y + 0.5),
	arrowprops=dict(arrowstyle="->")
)
plt.title("Basic line plot with annotations")

# save plot
plt.savefig("Basic saving", dpi=300, bbox_inches="tight")
plt.show()
