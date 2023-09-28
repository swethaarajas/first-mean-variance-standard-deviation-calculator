import numpy as np

def calculate(list):
  count = 0
  for item in list:
    count += 1

  if count != 9 :
    raise ValueError("List must contain nine numbers.")

  
  array = np.array(list,dtype=int)
  matrix = array.reshape(3,3)

  mean1 = np.mean(matrix, axis =0, dtype=np.float64)
  mean2 = np.mean(matrix, axis =1, dtype=np.float64)
  mean3 = np.mean(matrix, dtype=np.float64)

  var1 = np.var(matrix, axis=0, dtype=np.float64)
  var2 = np.var(matrix, axis=1, dtype=np.float64)
  var3 = np.var(matrix, dtype=np.float64)

  std1 = np.std(matrix, axis =0, dtype = np.float64)
  std2 = np.std(matrix, axis =1, dtype = np.float64)
  std3 = np.std(matrix, dtype = np.float64)

  max1 = np.max(matrix, axis =0)
  max2 = np.max(matrix, axis =1)
  max3 = np.max(matrix)

  min1 = np.min(matrix, axis =0)
  min2 = np.min(matrix, axis =1)
  min3 = np.min(matrix)

  sum1 = np.sum(matrix, axis =0, dtype=np.float64)
  sum2 = np.sum(matrix, axis =1, dtype=np.float64)
  sum3 = np.sum(matrix, dtype=np.float64)

  calculations = {
   "mean" : [mean1.tolist() , mean2.tolist() , mean3.tolist()] ,
    "variance" : [var1.tolist() , var2.tolist() , var3.tolist()] ,
    "standard deviation" : [std1.tolist() , std2.tolist() , std3.tolist()],
    "max" : [max1.tolist() , max2.tolist() , max3.tolist()],
    "min" : [min1.tolist() , min2.tolist() , min3.tolist()],
    "sum" : [sum1.tolist() , sum2.tolist() , sum3.tolist()]  
  }


  return calculations
