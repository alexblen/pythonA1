import numpy as np
import matplotlib.pyplot as plt
import sympy as sympy
#question 1
#part a
def updateR(R):
    '''
    this function takes a vector of car positions and returns the positions of those cars at t+1
    '''
    R_new=np.zeros_like(R)
    N=len(R)
    for n in range(N):
        if R[n]==0:
            R_new[n]=R[n-1]
        elif R[n]==1:
            if R[(n+1)%N]==0:
                R_new[n]=0
            else:
                R_new[n]=1
    return R_new
            

#part 2
NumCells=100
R_prime=np.zeros((NumCells,1))

for i in range(1,NumCells):
    prime=sympy.isprime(i)
    if(prime==True or (i>40 and i<=55)):
        R_prime[i-1]=1
R_prime=R_prime.astype(int)

def updateRtimes(R,T):
    '''
    Function which takes our original vector and returns car positions at time T
    '''
    for t in range(T):
        R_new_t=updateR(R)
        R=R_new_t
    return R

#part 3
def PlotTimeIntervals(R,t1,t2):
    '''
    calculates all the positions for the cars between t1 and t2
    then plots a checkerboard of where each car is at each time
    '''
    c=t2-t1
    Start_pos=updateRtimes(R,t1)
    temp=Start_pos
    for t in range(c):
        updated=updateRtimes(Start_pos,t+1)
        temp=np.concatenate((temp,updated),axis=1)
    return plt.imshow(temp.T)

    
PlotTimeIntervals(R_prime,0,20)
PlotTimeIntervals(R_prime,300,320)
PlotTimeIntervals(R_prime,380,400)




#question 2

#part 1


#if i want a list can do
#Trajt=[i+1 for i,val in enumerate(x) if val==1]
 
    
def new_position(R,Traj):
    '''
    Takes the trajectory at t and returns the trajectory at t+1
    '''
    M=len(Traj[:,-1])
    N=len(R)
    Traj_new=np.zeros((M,1))
    for m in range(M):
        num=Traj[m,-1]
        if R[(num)%N]==1:
            Traj_new[m]=Traj[m,-1]
        else:
            Traj_new[m]=Traj[m,-1]+1
    return Traj_new.astype(int)

def new_updateR(Traj_t1,N):
    '''
    takes the trajectory at t+1 and the number of cells in the original vector and returns the car positions
    '''
    R=np.zeros((N,1))
    for t in range(len(Traj_t1)):
        j=Traj_t1[t]%N
        R[j-1]=1
    return R.astype(int)

def ave_vel(Traj,t):
    '''
    tells us the speed at which a car is moving
    '''
    speed=Traj[:,t]-Traj[:,t-1]
    return sum(speed)/len(Traj[:,t])
    

        
#part 1
x=np.array((1,0,0,1,1,1,0,0,1)).reshape(9,1)
x1=updateR(x)
x2=updateR(x1)
Traj_x = np.array((1,4,5,6,9)).reshape(5,1)
Traj_1=new_position(x,Traj_x)
Traj_2=new_position(x1,Traj_1)
Traj_3=new_position(x2,Traj_2)
np.concatenate((Traj_x,Traj_1,Traj_2,Traj_3),axis=1)

#Part 2
N_2=50
M_2=15
T_2=50
test_2=np.concatenate((np.ones((M_2,1)),np.zeros((N_2-M_2,1))))
Test_speed=np.zeros((T_2,1))
Test_Traj=np.array((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)).reshape(15,1)
for t in range(T_2):
    Test_R=updateRtimes(test_2,t)
    Test_Traj_1=new_position(Test_R,Test_Traj)
    Test_Traj_matrix=np.concatenate((Test_Traj,Test_Traj_1),axis=1)
    Test_speed[t]=ave_vel(Test_Traj_matrix,1)
    Test_Traj=Test_Traj_1
Test_speed
#creating vectors to test (using the example in class)
M=5
x=np.array((1,0,0,1,1,1,0,0,1)).reshape(9,1)
x1=updateR(x)
x2=updateR(x1)
y_10updates=updateRtimes(x,9)
Traj_x = np.array((1,4,5,6,9)).reshape(5,1)
Traj_y=new_position(x,Traj_x)
Traj_matrix=np.concatenate((Traj_x,Traj_y),axis=1)
vel_car=ave_vel(Traj_matrix,1)

x
y
y_10updates
Traj_x
Traj_y
Traj_matrix
vel_car





 
#def primes():
#    '''
#    Function uses the sieve of Eratosthenes method to return a list
#    of primes <=100.
#    '''
#    prime_list = list(range(2,101))
#    for number in prime_list:
#        i = prime_list.index(number)
#        for j in prime_list[i+1:]:
#            if j%number==0:
#                prime_list.remove(j)
#    return prime_list
#prime100=primes()

