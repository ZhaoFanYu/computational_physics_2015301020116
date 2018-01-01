# Exercise_10
## 习题5.3
### 概述
利用电容问题的对称性来编写一个程序，通过计算x - y平面的一个象限的电势来得到结果
### 方法步骤
我们求解Laplace方程


![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic11-1.png)


可以得到解V(i,j,k),我们将这个解写成下面的形式：


![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic11-2.png)


现在需要一个数值方法来确定这个函数，假设V是已知的边界。我们不能仅仅从一个边界开始，然后在整个系统中工作，因为根据拉特方程，我们需要在所有的邻居中知道V，以便计算它在任何特定点的值。我们采取的方法是，从最初的几项开始，以解决问题;称之为V0(i,j,k)。一般来说，除非我们是非常聪明的，否则我们所做的设计不会满足任何地方的拉普拉斯方程。为了得到一个改进的guss，我们使用最后一个方程来计算V的新值，V1，在右边使用V0。然后我们用V1重复这个过程得到一个更好的，V2。这个迭代过程继续下去，直到我们的结果满足一些收敛性的问题，我们将很快讨论这个问题。重点是我们可以迭代过程来得到一个更好更好的解决方案。这种通用的方法称为ralaxation方法，它是处理几个重要类的部分微分方程的有用方法。
### 结果
![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic11-3.png)
### 代码
[souce code](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/code12.py)
