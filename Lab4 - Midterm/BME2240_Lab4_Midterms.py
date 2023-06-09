import numpy as np
import matplotlib.pyplot as plt

def equation(u_2,u_1):
    #Adjust these until they match
    g = -9.81 #m/s^2
    c = .0158 #.0142 #.002 #kg [.001]
    k = 51.9 #41.8 #43 #n/m [45]
    m = .712 #.64 #kg [.7]
    
    #Equation Calculated from step 5
    u_2P = m*g - (c/m)*u_2 - (k/m)*u_1

    return u_2P

def eq_given(u_2,u_1):
    g = -9.81 #m/s^2
    c_given =.001
    k_given = 45
    m_given = .7

    u_2P_given = m_given*g - (c_given/m_given)*u_2 - (k_given/m_given)*u_1

    return u_2P_given

def rk4Method(xi,xf,u_2,u_1):
    # ------ Key ------- 
    # xi : starting range
    # xf : last range
    # u_2 : initial u_2 given [x'(0)=0]
    # u_1 : initial u_2 given [x(0)=0]
    # ------------------ 
    
    #Reads the txt file
    t = np.loadtxt('output1.txt',usecols=0,skiprows=12)
    l = np.loadtxt('output1.txt',usecols=1,skiprows=12)
    t = t-.480000
    l = (l/1000)*-1 +.265302196
    print(t)
    print(l)
    print(len(l))

    print('Solving RK4: ')
    #initialize Variables
    xi = xi #Initial range given [0 seconds]
    xf = xf #Final range give [60 seconds]
    n = 6000 #Number of steps
    h = (xf-xi)/n #Solving for StepSize

    xpoints = np.arange(xi,xf,h) #Points on X-Axis

    #Creating lists for u_1,u_2 and k
    u_1_plot = []
    u_2_rk4 = []
    u_1_plot_given = []
    u_2_rk4_given = []

    k1_l = []
    k2_l = []
    k3_l = []
    k4_l = []
    newXPoints = []

    u_1_g = u_1
    u_2_g = u_2

    #Iterating through points of x
    for i in xpoints:
        #Adding (u_1,u_2) to there respected list
        u_1_plot.append(u_1)
        u_2_rk4.append(u_2)
        u_1_plot_given.append(u_1_g)
        u_2_rk4_given.append(u_2_g)
        newXPoints.append(i+.5*h)

        #Solving for K-Values
        m1 = h*u_2
        k1 = h*equation(u_2,u_1)

        m1_g = h*u_2_g
        k1_g = h*eq_given(u_2_g,u_1_g)

        m2 = h*(u_2 + .5*k1)
        k2 = h*equation(u_2 + .5*k1, u_1 + .5*m1)

        m2_g = h*(u_2_g + .5*k1_g)
        k2_g = h*eq_given(u_2_g + .5*k1_g, u_1_g + .5*m1_g)
        
        m3 = h*(u_2 + .5*k2)
        k3 = h*equation(u_2 + .5*k2, u_1 + .5*m2)

        m3_g = h*(u_2_g + .5*k2_g)
        k3_g = h*eq_given(u_2_g + .5*k2_g, u_1_g + .5*m2_g)

        m4 = h*(u_2 + k3)
        k4 = h*equation(u_2 + k3, u_1 + m3)

        m4_g = h*(u_2_g + k3_g)
        k4_g = h*eq_given(u_2_g + k3_g, u_1_g + m3_g)
    
        #phi = ((1/6) * k1) + ((1/3) * k2) + ((1/3) * k3) + ((1/6) * k4)
        
        #Adding K-Values into list for debugging
        k1_l.append(k1)
        k2_l.append(k2)
        k3_l.append(k3)
        k4_l.append(k4)
        #phi_l.append(phi)

        #Solving for Y-RK4 and X
        u_1 += (m1 + 2*m2 + 2*m3 + m4)/6
        u_2 += (k1+ 2*k2 + 2*k3 + k4)/6
        u_1_g += (m1_g + 2*m2_g + 2*m3_g + m4_g)/6
        u_2_g += (k1_g+ 2*k2_g + 2*k3_g + k4_g)/6
    
    '''
    #For Debugging
    print('x - Value: ')
    print(xpoints)
    print('\n' + 'u_1 - rk4 Value: ')
    print(u_1_plot)
    print('\n' + 'u_2 - rk4 Value: ')
    print(u_2_rk4)
    print('\n' + 'K1: ')
    print(k1_l)
    print('\n' + 'K2: ')
    print(k2_l)
    print('\n' + 'K3: ')
    print(k3_l)
    print('\n' + 'K4: ')
    print(k4_l)
    print('\n' + 'Phi: ')
    print(phi_l)
    '''
    print(u_1_plot)

    #Plotting all X_values and y_RK4 values
    plt.plot(xpoints,u_1_plot,color='b',label='Analytical Solution RK4 Analysis')
    plt.plot(xpoints,u_1_plot_given,color='r',label='RK4 approximation')
    plt.plot(t,l,color='g',label='Experimental Data')
    plt.xlabel('Time (s)')
    plt.ylabel('Height (m)')
    plt.legend()
    plt.title('Solution of differential equation (RK4 - StepSize: ' + str(h) + ')')
    plt.show()

    print('Finished Solving RK4!')

rk4Method(0,60,0,0) # (leftbound,  rightbound,  initial u_2,  initial u_1)
