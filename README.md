# convex_optimization
This repository stores the assignments done while doing the summer project of convex **optimization techniques** at **IITK** provided by **pclub**.
It contains the following assignments:
* **[Assignment 1](https://github.com/kartavya2000/convex_optimization/blob/master/weibull.py)**: Weibull distribution maximizing the log likelihood function.
              This assignment deals with maximizing the log likelihood function by partial differintiation of the same function
              with respect to different variables on which the fuction depends.
              The problem statement for the assignment is here:
              ![weibull distribution](https://scontent-bom1-1.xx.fbcdn.net/v/t1.15752-0/p480x480/60730643_2040459639591866_4893926306770583552_n.png?_nc_cat=107&_nc_oc=AQnzUsgs_31tvGPrrFzyGaQbSHVcqPFnzNDlNBxB_YgXDq-m5EN86P9fjhDM1pDgo-I&_nc_ht=scontent-bom1-1.xx&oh=4bd4b1c4db9d6658c239e04e87a652f2&oe=5D8C2E91 "assignment 1 problem statement")
  So to solve the  problem here the log likelihood  function is first differentiated with respect to the three given parameters and then it this is used to obtain eta solely in terms of beta. Then beta is solved using recursive method of approximating by first assuming the value of the parameter beta to be 1. The iterations are stopped once the standard deviation of the last some of the values falls below a particular value. 
              
