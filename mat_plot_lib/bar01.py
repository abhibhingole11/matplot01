import matplotlib.pyplot as plt
import numpy as np
x = 0.5 + np.arange(7)
y = 0.4 + np.arange(7)
plt.xlabel('java')
plt.ylabel('python')
plt.title('languages')
plt.bar(x,y,color='yellow')
print(plt.style.available)
plt.style.use('dark_background')
# plt.grid(True)

plt.show()
