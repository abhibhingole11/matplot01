from matplotlib import pyplot as plt
x = [ 10,20,30,40,50]
y = [ 100,200,250,350,450]
plt.bar(x,y,color='r')

plt.grid(True)
plt.savefig('plot.png')

plt.show()