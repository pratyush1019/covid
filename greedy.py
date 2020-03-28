# Sensing matrix design greedy

import numpy as np
import sys
from numpy import linalg as LA
np.set_printoptions(threshold=np.inf)

def create_infection_array_with_prob(n, p):
  arr = np.random.binomial(1, p, n)
  #while sum(arr) == 0:
  #  arr = np.random.binomial(1, p, n)
  return arr

def create_infection_array_with_num_cases(n, d):
  arr = np.zeros(n)
  idx = np.random.choice(range(n), d, replace=False)
  arr[idx] = 1
  assert sum(arr) == d
  return arr



# Test matrix
def initialize_M(s,n,t):
  M = np.random.binomial(1, s, size=(t, n))
  I=np.identity(n)
  # print(I)
  # print(M)
  # print(M.shape)
  # print(np.dot(np.transpose(M),M))
  print("Initial forbenius")
  print(LA.norm(np.dot(np.transpose(M),M)-I))
  no_changes=0
  cnt=0
  while(cnt<n*t):
    i=int(cnt/n)
    j=int(cnt%n)
    # print(cnt)
    val1=LA.norm(np.dot(np.transpose(M),M)-I)
    # print(val1)
    if(M[i][j]==0):
      M[i][j]=1
      val2=LA.norm(np.dot(np.transpose(M),M)-I)
      if(val2<val1):
        # no_changes=0
        cnt+=1
      else:
        M[i][j]=0
        # no_changes+=1
        cnt+=1
      # print(val2)
    else:
      M[i][j]=0
      val2=LA.norm(np.dot(np.transpose(M),M)-I)
      if(val2<val1):
        # no_changes=0
        cnt+=1
      else:
        M[i][j]=1
        no_changes+=1
        cnt+=1
      # print(val2)
  print("required matrix")    
  print(M)
  print("forbenius")
  print(LA.norm(np.dot(np.transpose(M),M)-I))

    #for person in range(n):
    #  while sum(self.M[person]) == 0:
    #    self.M[person] = np.random.binomial(1, self.s, size=(self.t))
    #    print('changing tests for person', person)
    # Count of number of people in only 1 test
    #print(sum([item == 1 for item in [sum(row) for row in self.M]]))

  # Get test results from infection array and test matrix
  # In reality this will happen from group testing



if __name__ == '__main__':
  # matrix width is t*n
  # Test width. Max number of parallel tests available.
  t = 20

  # Infection probability
  p = 0.001

  # Test failure probability
  q = 0.

  # Group size
  n = 1000

  # Number of infections
  d = 300

  # Test assignment probability. Probability that a person gets assigned to a
  # test
  s = 1. / 10
  initialize_M(s,n,t)

 