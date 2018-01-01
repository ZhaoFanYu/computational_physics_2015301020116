# Exercise_07
## Discussion on chaos (problem 3.18 3.19)
### Abstract
Though there is chaos in the graph of theta and t, but the pendulum quickly settles into a regular orbit in the phase space corresponding to the oscillatory motion of both theta and w. 3.18Calculate Poincare section for tjhe pendulum as it undergoesthe period-doubling route to the chaos. Plot w versus theta, with one point ploted for each drive cycle. Do this for FD=1.4, 1.44, and 1.456. You should find that after removing the points to corresponding to the initial transient the attractor in the period-1regime will contain only single point. Likewise, if the behavior is period n, the attractor will contain n discrete points.
 3.19Calculate Poincare sections for the pendulum but for a frequency which has nothing to do with those intrinsic to the system. For example you might calculate the Poincare sections using an angular frequency that is irrationally related to the driving requency (as well as the natural frequency) for your stroboscopic snapshots. Do the results tell you anything about the system?
 ### Method
 Until now, we have calculated theta and t, so we just need to store the w we have calculated in the procedure. Then select several w and t according to period to sketch the graph.
 As we all know that there is the limitation of the significant digits, the number of the points on the poincare section will be affected. Because thre may be several pointts which are really close (in fact they should have been plotted at the same place for the reason of computational accuracy), we should choose proper limits of x and y axis. When we calculate the motion of the pendulum, we have use a given step. But we need to choose several w and t at the same phase in the period. We'd better change the period of the driving force in order to make the period a integer. So that we can always find the w in the same phase which is also calculated in the last circle.
 ### Output
 #### Poincare sections with different FD
 [CODE1](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/code8.1.py)
 
 We have calculate the motion for several FD, where the behaviors are period 1,2,3. 
 ![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic8-1.png)
 
 
 ![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic8-2.png)
 
 
 ![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic8-3.png)
 #### Poincare sections with different angular frequency
 [CODE2](https://github.com/maxiaobao233/compuational_physics_N2015301020106/blob/master/code8.2.py)
 ![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic8-4.png)
 
 
 ![](https://github.com/yyx1996/computational_physics_N2015301020105/raw/master/pic8-5.png)
 ### Conclusion
 In the first problem we can draw a conclusion that if the behavior is period n, the attractor wiil contain n discrete points.
 In the second problem we find that the results look chaotic even in the periodic regimes(for the angular frequency that is irrationally related to the driving frequency)
