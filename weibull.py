#weibull in optimization techniques

import numpy as np 

lis=[]
#i=0
# while i<100:                          #for random inputs
#     num=(np.random.random(1))[0]*100
#     if(num>1):
#         lis.append(num)
#         i=i+1

# num=int(input("enter a no. "))   # if you want  user defined input
# while num>=0:
#     lis.append(num)
#     num=int(input("enter a no. "))
print("processing the data...")

n=len(lis)
bias_arr=lis
for i in range(0,n):
    bias_arr[i]=bias_arr[i]-0.99999
betas=[0]*10


def eta_value(beta, arr):
    sum=0
    for i in range (0,len(arr)):
        sum=sum+arr[i]**beta
    return (sum**(1/beta))/len(arr) 

def beta_value(beta,arr):
    sum=0
    eta=eta_value(beta,arr)
    for i in range (0,len(arr)):
        sum=sum+(np.log(arr[i])*((arr[i]/eta)**beta -1))
    return abs(sum/len(arr))



def enter_beta(beta):
    global betas
    for i in range (8,-1,-1):
        betas[i+1]=betas[i]
    betas[0]=beta

def beta_iterator(arr):
    global betas
    betas[9]=1
    i=8
    while (i>=0):
        betas[i]=beta_value(betas[i+1],arr)
        i=i-1
    betasarr=np.array(betas)
    while (np.std(betasarr)>0.001*betas[0]):
       enter_beta(beta_value(betas[0],arr))

    return [betas[0],eta_value(beta,arr)]

beta=beta_iterator(bias_arr)[0]
eta=beta_iterator(bias_arr)[1]
print("beta is : {beta}")
print("eta is : {eta}")



