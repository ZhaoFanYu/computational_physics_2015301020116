# Exercise_09
## 习题 4.16
### 问题概述
进行真实的三体模拟，计算地球、木星和太阳的运动。由于这三个物体现在都在运动，所以将三体系统的质心作为原点，而不是太阳的位置是很有用的。我们还建议给太阳一个初始速度，使系统的总动量为零(这样质量中心就会保持不变)。研究地球在不同初始条件下的运动，试着将木星的质量提高到10,100倍，以及它的质量的1000倍。
### 方法步骤
正如我们之前讨论过的，对于振动问题，Eular不是一个很好的选择，行星运动就是这样一个问题。如果我们用这个方法，我们会发现地球的能量会随着时间增长，它会从太阳旋转。这一困难是通过Eular = Cromer方法避免的，因为它在每个轨道上都能转换能量
#### 结果
#### 正常的条件。(木星的质量是它的质量)时
![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic10-1.png)


画出时间t改变时的轨道



![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic10-2.png)
#### 木星的质量是它实际质量的10倍时
![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic10-3.png)


画出时间t改变时的轨道



![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic10-4.png)
#### 木星的质量是它实际质量的100倍时
![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic10-5.png)


画出时间t改变时的轨道



![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic10-6.png)
#### 木星的质量是它实际质量的1000倍时
![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic10-7.png)
### 结论
在正常情况下，轨道是稳定的。
随着木星质量的增加，轨道逐渐变得不稳定。
当木星的质量足够大时，木星就会脱离太阳
### 代码
[souce code](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/code11.py)
