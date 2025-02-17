# Running this test code will provide the output needed for checking the answers to the five questions

import numpy as np
import math

def Question_One() :
    x=[3.6, 3.8, 3.9]
    val=[1.675, 1.436, 1.318]
    w=3.7

    # Declaring 2D array neville and filling it with zeroes
    neville=np.zeros((len(x), len(x)))

    for i in range(len(x)):
        neville[i][0]=val[i]

    for i in range(1, len(x)):
        for j in range(1, i+1):
            term1=(w-x[i-j])*neville[i][j-1]
            term2=(w-x[i])*neville[i-1][j-i]

            neville[i][j]=(term1-term2)/(x[i]-x[i-j])
        #print(neville[i][j])
    print(neville[1][1])

print()
# Print output to make sure the function runs correctly
solution1=Question_One()


def Question_Two():
    x=[7.2, 7.4, 7.5, 7.6]
    fx=[23.5492, 25.3913, 26.8224, 27.4589]

    first_deg=np.zeros(len(x))
    for i in range(1, len(x)):
        first_deg[i]=(fx[i]-fx[i-1])/(x[i]-x[i-1])
    print(first_deg[1])

    sec_deg=np.zeros(len(x))
    for i in range(2, len(x)):
        sec_deg[i]=(first_deg[i]-first_deg[i-1])/(x[i]-x[i-2])
    print(sec_deg[2])

    third_deg=np.zeros(len(x))
    for i in range(3, len(x)):
        third_deg[i]=(sec_deg[i]-sec_deg[i-1])/(x[3]-x[0])
    print(third_deg[3])

    def Question_Three():
        y=fx[0]+first_deg[1]*(7.3-x[0]) + sec_deg[2]*(7.3-x[0])*(7.3-x[1]) + third_deg[3]*(7.3-x[0])*(7.3-x[1])*(7.3-x[2])
        print(y)

    print()
  # Print output to make sure function runs correctly
    solution3=Question_Three()

print()
# Print output to make sure function runs correctly
solution2=Question_Two()

def Question_Four():
    x=[3.6, 3.8, 3.9]
    fx=[1.675, 1.436, 1.318]
    f_deriv=[-1.195, -1.188, -1.182]

    lim=len(x)
    hermite=np.zeros((2*lim, 2*lim-1))

    for i in range(lim*2):
        hermite[i][0]=x[int(i/2)]
    for i in range(lim*2):
        hermite[i][1]=fx[int(i/2)]

    for i in range(1, lim*2, 2):
        hermite[i][2]=f_deriv[int(i/2)]
        
    for i in range(2, lim*2, 2):
        hermite[i][2]=(hermite[i][1]-hermite[i-1][1])/(hermite[i][0]-hermite[i-1][0])

    for i in range(2, lim*2-1):
        for j in range(i, lim*2-1):
            if (i//2==0):
                hermite[i][j]=(hermite[i][j-1]-hermite[i-1][j-1])/(hermite[i][0]-hermite[i-1][0])
            elif (i==2 and j==4):
                hermite[i][j]=0
            else:
                hermite[i][j]=(hermite[i][j-1]-hermite[i-1][j-1])/(hermite[i][0]-hermite[i-2][0])
    print(hermite)

print()
# Print output to make sure function runs correctly
solution4=Question_Four()


def Question_Five():
    x=[2, 5, 8, 10]
    fx=[3, 5, 7, 9]
    lim=len(x)

    h=np.zeros(lim)
    a=np.zeros((lim, lim))
    a[0][0]=1
    a[lim-1][lim-1]=1

    for i in range(lim-1):
        h[i]=x[i+1]-x[i]

    for i in range(1, lim-1):
        a[i, i-1]=h[i-1]
        a[i, i]=2*(h[i-1]+h[i])
        a[i, i+1]=h[i]
    
    b=np.zeros(lim)

    for i in range(1, lim-1):
        b[i]=3*((fx[i+1]-fx[i])/h[i]-(fx[i]-fx[i-1])/h[i-1])

    x=np.linalg.solve(a, b)

    print(a)
    print(b)
    print(x)

print()
# Print output to make sure function runs correctly
solution5=Question_Five()
