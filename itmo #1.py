"""import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5,10])                                         # Обычный график
y = np.array([1,4,9,16,25,14])
plt.plot(x,y)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,1,5,5,1])                                             # Квадрат
y = np.array([1,5,5,1,1])
plt.plot(x,y,'m--', marker = 'o', markerfacecolor = 'y')
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2*np.pi,2*np.pi,0.1)
y = np.sin(x)                                                          # Закрашенная синусоида
plt.plot(x,y)
plt.fill_between(x,y,where = (y > 0), color = 'm',alpha = 0.5)
plt.fill_between(x,y,where = (y < 0), color = 'c',alpha = 0.5)
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
f,ax = plt.subplots(1,3)

x1 = np.arange(10,90,10)
y1 = x1 * 0.5
ax[0].plot(x1,y1,'m:',marker = 'o', markerfacecolor = 'y',linewidth = 2 , alpha = 0.5)
ax[0].grid()

x2 = np.arange(-2*np.pi,2*np.pi,0.1)
y2 = np.cos(x2)
ax[1].plot(x2,y2,"k--",marker = 'p',mfc = 'r',alpha = 1,linewidth = 1)
ax[1].grid()

x3 = np.arange(-10,11,1)
y3 = x3**2
ax[2].plot(x3,y3,color = 'g',marker = 'd',mfc = 'b',alpha = 0.3,linewidth = 3)
ax[2].grid()
plt.show() """

import numpy as np
import matplotlib.pyplot as plt
f, ax = plt.subplots(1,2)
x1 = np.arange(0,20,1)
y1 = x1 ** 2
ax[0].plot(x1,y1,":r",marker = 'o',mfc = 'y',alpha = 0.5)
ax[0].grid()

x2 = np.arange(-2*np.pi,2*np.pi,0.1)
y2 = np.sin(x2)
ax[1].fill_between(x2,y2,'--c', where = (y2 > 0), color = 'm', alpha = 0.5)
ax[1].fill_between(x2,y2,"--c", where = (y2 < 0), color = 'y',alpha = 0.5)
ax[1].grid()
plt.show()


