from matplotlib import pyplot as plt

x = (1,2,3,4,)
y = (5,6,7,8)
plt.plot(x,y,linestyle='--',marker='o')

dev_y = [9,10,11,12]
c = [13,15,37,40]
d = [41,42,23,28]
plt.plot(x,dev_y,'r',marker='.')
plt.plot(x,c,linestyle='-',marker='o',color='orange')
plt.plot(x,d,color='green',marker='o')
plt.xlabel('Ages')#give name to x-axis
plt.ylabel('median salary(USD)')#give name to y-axis
plt.title('median salary (USD) by ages')#give name to graph
plt.grid(True)#make boxes on graph
plt.legend(['java','python','c','c++'])

plt.tight_layout()


plt.show()#print the graph