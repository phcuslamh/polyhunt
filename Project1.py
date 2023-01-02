#######################################################
# Name: Phuc H. Lam
# NetID: plam6
# Email: plam6@u.rochester.edu
#######################################################

import numpy as np
import random as rand
from matplotlib import pyplot as plt
import statistics as stat

#Divide into training/test set
def partition_data(data):
    Train = []
    Test = []
    for i in range(len(data)):
        if (rand.randint(0, 1) % 2 == 0):
            Train.append(data[i])
        else:
            Test.append(data[i])
    return Train, Test

#Construct PHI
def construct_PHI(data, M):
    temp = []
    for n in range(len(data)):
        tempROW = [1.0]
        S = 1.0
        for j in range(M):
            S = S * data[n][0]
            tempROW.append(S)
        temp.append(tempROW)
    return temp

#find parameters w_0, ..., w_n given M and lambda
def find_MLE(data, M, lamb):
    P = np.array(construct_PHI(data, M))
    P_t = P.transpose()
    t = []
    for i in range(len(data)):
        t.append(data[i][1])
    t = np.array(t)
    t = t.transpose()
    A = np.linalg.pinv(np.matmul(P_t, P) + lamb * np.identity(M+1))
    A = np.matmul(A, P_t)
    w = np.matmul(A, t)
    return w

#Take in x, w and compute w_0 + w_1 * x + ... + w_M * x^M
def compute_poly(x, w):
    S = 0.0
    T = 1.0
    for i in range(len(w)):
        S += w[i] * T
        T = T * x
    return S

#Compute the mean square error
def compute_MSE(data, w, lamb):
    b = []
    for i in range(len(data)):
        x = data[i][0]
        y = data[i][1]
        b.append(compute_poly(x, w) - y)
    b = np.array(b)
    b_t = b.transpose()
    S = np.matmul(b, b_t) / 2
    wt = np.array(w)
    wt = wt.transpose()
    S += lamb * np.matmul(w, wt) / 2
    return S

########### MAIN PROGRAM ###########
with open('datasets/A') as f:
    Lines = f.readlines()
dataset = []
for line in Lines:
    lst = [float(n) for n in line.split(',') if n.strip()]
    dataset.append(lst)         

########### Find lambda ###########
"""
dataTrain, dataTest = partition_data(dataset)
M_ind = []
TOTALM = []
for M in range(1, 20):
    M_ind.append(M)
    temp = []
    for i in range(6):
        lamb = np.exp(-i)
        wt = find_MLE(dataTrain, M, lamb)
        temp.append(compute_MSE(dataTest, wt, lamb))
    TOTALM.append(temp)
COL = ["lavender", "navy", "green", "coral", "yellow", "turquoise", "peru", "blueviolet", "crimson", "olivedrab"]
fig1 = plt.figure()
for i in range(1, 10):
    plt.plot(np.array([0, 1, 2, 3, 4, 5]), TOTALM[i], color=COL[i])
plt.show()
fig2 = plt.figure()
for i in range(10, 19):
    plt.plot(np.array([0, 1, 2, 3, 4, 5]), TOTALM[i], color=COL[i-10])
plt.show()
"""
#######################################################

########### Find M ###########
"""     
lamb = np.exp(-2)
ListOfDeg = []
rho = 100 
for i in range(rho):
    dataTrain, dataTest = partition_data(dataset)
    MSE_test = []
    MSE_train = []
    M_ind = []
    for M in range(2, 20):
        M_ind.append(M)
        wt = find_MLE(dataTrain, M, lamb)
        MSE_test.append(compute_MSE(dataTest, wt, lamb))
        MSE_train.append(compute_MSE(dataTrain, wt, lamb))
    ProbArgM = np.min(MSE_test)
    ProbM = MSE_test.index(ProbArgM) + 2
    ListOfDeg.append(ProbM)
ListOfDeg = np.array(ListOfDeg)
print(ListOfDeg) 
print(stat.mode(ListOfDeg))
"""
#######################################################

########### Find w and MSE ###########
"""
M = 19
lamb = np.exp(-2)
w = find_MLE(np.array(dataset), M, lamb)
MSE = compute_MSE(dataset, w, lamb)
print(w)
print(MSE)

D = np.array(dataset)
D = D.transpose()
XCoord = D[0]
YCoord = D[1]
x = np.linspace(-1.1, 1.1, num=200)
fx = []
for i in range(len(x)):
    fx.append(compute_poly(x[i], w))
fig = plt.figure()
plt.scatter(XCoord, YCoord, color="blue")
plt.plot(x, fx, color="red")
plt.show()
"""
#######################################################