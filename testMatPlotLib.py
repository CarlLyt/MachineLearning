# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 11:41:53 2018

@author: Administrator
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,3,50)
y1 = 2*x + 1
y2 = x**2
"""
每一个figure代表一张图片，从figure开始，到第二个figure之前全部为第一个图片的绘画部分
"""
plt.figure(num = 5)                     
plt.plot(x,y1)

x0 = 1
y0 = 2*x0 +1

ax = plt.gca()
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position('left')

ax.spines["bottom"].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.scatter(x0,y0,s = 50,color = 'r')
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)
##method 1
plt.annotate(r'$2x+1 = %s$' %y0,xy=(x0,y0),xycoords='data',xytext=(+10,-10),textcoords = "offset points",)


##method 2
plt.text(-1,3,r"$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_m$")

"""
下面是第二幅图片
"""
plt.figure(num = 3)
"""
想在一张图片里面显示多个曲线，直接绘画即可
"""

"""
#简单版本
plt.plot(x,y2,label = 'up')
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label = 'down')
plt.legend()

"""


"""
前面用l1,  一定要有(，)，不然找不到
之后将l1,  l2,传进去，handles住   
labels对应着handles里的设置标签
loc代表lengend的位置
"""
l1,=plt.plot(x,y2,label = 'up')
l2,=plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label = 'down')
plt.legend(handles=[l1,l2,],labels=["First Line","Second Line"],loc='best')


"""
定义x轴 和 Y轴的区间范围
"""
plt.xlim((-1,2))
plt.ylim((-2,3))


"""
设置x轴  Y轴的说明
"""
plt.xlabel("X Plot")
plt.ylabel("Y Plot")
"""
定义新的范围区间
"""
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1,0,1,2,3],[r'$Really\ bad$',r'$Bad$',r"$It's\  OK$ ",r'$Normal$',r'$Good$',r"$Very\  Good$"])


"""
将边框的上部 和  右部  设置为空
"""
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
"""
设置x轴  和  y轴的 放置位置
"""
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',-1))
ax.spines['left'].set_position(('data',0))
 
plt.show()
































