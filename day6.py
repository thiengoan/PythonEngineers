import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(0, 10,0.1)
# y1 = x
# y2 = x/3
# y3 = x**2
# y4 = x**4

# fix, ax = plt.subplots(2,2)
# ax[0,0].plot(x,y1)
# ax[0,1].plot(x,y2)
# ax[1,0].plot(x,y3)
# ax[1,1].plot(x,y4)
# # ax[1,1].axis('off')
# plt.tight_layout()
# plt.legend()
# plt.show()

x = ['Java','Python','PHP','JavaScript','C#','C++']
y = [22.2,17.6,8.8,8,7.7,6.7]

plt.pie(y,labels=x,autopct='%0.1f%%',startangle=135)
plt.show()