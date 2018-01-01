# Final Exercise
## 赵凡瑜 2015301020116
### 摘要
在之前学习了很多都是有着确定的物理规律的模型，如棒球轨迹等，而书中第七章介绍了随机系统，感觉更为有趣。而在学习\
热力学与统计物理学的过程当中，在学习涨落的过程当中，接触了一些这样随机性的题目，当时用统计物理学的知识求得解，\
虽然是严格的数学上的推导，却不能很好的去验证解的正确性，而如果运用python去研究这个随机系统，就可以得到相应的\
结果，很好地验证了结果的正确性。
### 关键词
随机系统，涨落，高斯分布
### 正文
####1.等概率随机行走
#####1.1一维状态
假设有一个微观粒子，它在下一时刻向左或向右运动的概率相等，若我们统计他走过500次的位移，得到的便是随机行走的模型\
我们产生一个0到1之间的随机数组，如过大于0.5则向左走，反之向右,随即模拟。\
程序代码如下:\
[程序1](https://github.com/ZhaoFanYu/computational_physics_2015301020116/blob/master/untitled0.py)\
产生的结果如图所示\
![](https://github.com/ZhaoFanYu/computational_physics_2015301020116/blob/master/图片%201.png)\
#####1.2二维状态
对于二维的随机行走，我们可以采用创建两个数组构成二维数组来表示，此时粒子每一步有四个方向可供选择，则情况较为复杂\
程序代码下：\
[程序2](https://github.com/ZhaoFanYu/computational_physics_2015301020116/blob/master/untitled1.py)\
结果如图：\
![](https://github.com/ZhaoFanYu/computational_physics_2015301020116/blob/master/图片%202.png)\
#####1.3三维状态
更进一步的，我们可以研究三维情况下的随机行走模型，代码见下\:
[程序3](https://github.com/ZhaoFanYu/computational_physics_2015301020116/blob/master/untitled2.py)\
结果如图：\
![](https://github.com/ZhaoFanYu/computational_physics_2015301020116/blob/master/图片%203.png)\
####2.非等概率随机行走
以上的情况都是建立在两个方向等概率情况下，那如果概率不同又会是什么情况。\
我们将上边一维情况中向左走概率调为0.4向右走概率为0.6，进行模拟，结果如下：\
![](https://github.com/ZhaoFanYu/computational_physics_2015301020116/blob/master/图片%204.png)\
可见已经和等概率情况有了很大不同，那么考虑极限情况，向左概率调为0.49，向右概率0.51，结果如下：\
![](https://github.com/ZhaoFanYu/computational_physics_2015301020116/blob/master/图片%205.png)\
可以看出当步数较小的时候基本还是在中轴附近，但随着步数的增多，将偏向右边越远。\
从而引出统计物理中习题问题：\
当步数N很大时，求走N步后离原点距离的分布。\
假设一人无规行走在东西走向的一条大道上，即他每走一步是朝东还是朝西的几率均为1/2，取x轴沿东西大道，\
向东为正，向西为负。若此人的步长为l,出发点为原点，\
(1)、求走N步后离原点距离的分布；\
(2)、证明当N远大于1时，其分布为高斯分布。\

首先运用统计物理学知识做出解答，再用代码进行验证。\
![](https://github.com/ZhaoFanYu/computational_physics_2015301020116/blob/master/图片6.png)\
![](https://github.com/ZhaoFanYu/computational_physics_2015301020116/blob/master/图片7.png)\
我们得出结论当N远大于1时，其分布为高斯分布，下面用上述模型进行验证：\

代码如下：\

[程序4](https://github.com/ZhaoFanYu/computational_physics_2015301020116/blob/master/untitled3.py)\

可见确实为明显的高斯分布。
