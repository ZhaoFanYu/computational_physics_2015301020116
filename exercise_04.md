# Exercise_04
## 2.9
## 题目:Calculate the trajectory of our cannon shell including both air drag and the reduced air density at high altitudes so that you canreproduce the results in Figure 2.5. Perform your calculation for different firing angles and determine the value of the angle that gives the maximum range.
### 题目分析：首先运用python做出物体抛出后的运动图像。再通过图像判断出射程最远时对应角度所在区间，再在所得区间内求出最远时的角度即可。
下先做出30，40，50度时运动图像，尝试是否出现射程最远情况。
```python
import matplotlib.pyplot as plt
import math
def area(v_0, theta_0):
    v_x_0 = v_0 * math.cos(theta_0)
    v_y_0 = v_0 * math.sin(theta_0)
    x_0 = 0
    y_0 = 0
    x_i = x_0
    y_i = y_0
    v_x_i = v_x_0
    v_y_i = v_y_0              
    delta_t = 0.1
    drag_0 = 4 * (10 **(-5))     
    list_x = []
    list_y = []
    list_x.append(x_i)
    list_y.append(y_i)         
    while(1):
    drag_i = drag_0 * ((1 - y_i * (6.5 * 10 **(-3)) / 300) ** (2.5))   #a=6.5*10^(-3)K/m, T=300K, α=2.5
        v_i = math.sqrt(v_x_i ** 2 + v_y_i ** 2)
        x_iplus = x_i + v_x_i * delta_t
        y_iplus = y_i + v_y_i * delta_t
        v_x_iplus = v_x_i - drag_i * v_i * v_x_i * delta_t
        v_y_iplus = v_y_i - drag_i * v_i * v_y_i * delta_t - 9.8 * delta_t
        if y_iplus < 0:
            x_final = x_i - y_i * ((x_i - x_iplus) / (y_i - y_iplus))
            y_final = 0
            list_x.append(x_final)
            list_y.append(y_final)
            break
        else:
            x_i = x_iplus
            y_i = y_iplus
            v_x_i = v_x_iplus
            v_y_i = v_y_iplus
            list_x.append(x_i)
            list_y.append(y_i)
    plt.plot(list_x,list_y,label = theta_0 * 180 / math.pi)
    plt.legend()
    plt.title(u"Cannon shell trajectory") 
    plt.xlabel(u"x(m)")
    plt.ylabel(u"y(m)")
    return x_final
area(700,math.pi * 40 / 180)
area(700,math.pi * 30 / 180)
area(700,math.pi * 50 / 180)
```
图像如下：

![](https://github.com/ZhaoFanYu/computational_physics_2015301020116/blob/master/84DEB2F7B5BA4BCB3A36B9B6F1D84901.jpg)

可知最远距离在40到50度之间
再用下述程序求最远距离
```python
import math
def area(v_0, theta_0):
    v_x_0 = v_0 * math.cos(theta_0)
    v_y_0 = v_0 * math.sin(theta_0)
    x_0 = 0
    y_0 = 0
    x_i = x_0
    y_i = y_0
    v_x_i = v_x_0
    v_y_i = v_y_0             
    delta_t = 0.1
    drag_0 = 4 * (10 **(-5))     
    list_x = []
    list_y = []
    list_x.append(x_i)
    list_y.append(y_i)        
    while(1):
        drag_i = drag_0 * ((1 - y_i * (6.5 * 10 **(-3)) / 300) ** (2.5))   #a=6.5*10^(-3)K/m, T=300K, α=2.5
        v_i = math.sqrt(v_x_i ** 2 + v_y_i ** 2)
        x_iplus = x_i + v_x_i * delta_t
        y_iplus = y_i + v_y_i * delta_t
        v_x_iplus = v_x_i - drag_i * v_i * v_x_i * delta_t
        v_y_iplus = v_y_i - drag_i * v_i * v_y_i * delta_t - 9.8 * delta_t
        if y_iplus < 0
            x_final = x_i - y_i * ((x_i - x_iplus) / (y_i - y_iplus))
            y_final = 0
            list_x.append(x_final)
            list_y.append(y_final)
            break
        else:
            x_i = x_iplus
            y_i = y_iplus
            v_x_i = v_x_iplus
            v_y_i = v_y_iplus
            list_x.append(x_i)
            list_y.append(y_i)
     return x_final
area_max = area(700,math.pi * 30 / 180)
for i in range(21):
    n = i + 30
    area_2 = area(700,math.pi * n / 180)
    if area_max >= area_2:
        max_angle = 30
    else:
        area_max = area_2
        max_angle = n
print("when the range is maximun of %d m"%(area_max))
print("the angle is %d"%(max_angle))
```
### 结果：
可求得角度为40度时，最远距离为24522

