# using scikit-learn NumPy array splitting SciPy and stuff
import numpy as np
from scipy import stats

# let's consider a set of data
set_of_data =  [86, 87, 88, 86, 87, 85, 86, 87, 88, 86, 87, 85]
sod = [77, 32, 111, 99, 56, 86, 90, 178, 45, 67, 89, 23]
# mean function mean() from numpy output the average value of the set of data
avg = np.mean(set_of_data)
print(avg)
# mean function median() from numpy output the middle value of the set of data
mine = np.median(set_of_data)
print(mine)
# mean function mode() from stats from scipy output the mode value of the set of data
mode = stats.mode(set_of_data)
print(mode)
# mean function std() from numpy output the standard deviation value of the set of data
std = np.std(sod)
print(std)
# mean function var() from numpy output the variance value of the set of data
vary = np.var(sod)
print(vary)
# mean function percentile() from numpy output the percent value lower than a given value of the set of data
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = np.percentile(ages, 75)
print(x)

## DATA DISTRIBUTION
# Create an array with 100000 random numbers, and display them using a histogram with 100 bars:
import matplotlib
matplotlib.use('TkAgg')  # Must be called BEFORE importing pyplot
import matplotlib.pyplot as plt
dis = np.random.uniform(0.0, 5.0, 100000)
plt.hist(dis, 100)
plt.show()

## DATA NORMAL DISTRIBUTION
#A typical normal data distribution:
ndis = np.random.normal(5.0, 1.0, 100000)
plt.hist(ndis, 100)
plt.show()

## SCATTER PLOT
# Use the scatter() method to draw a scatter plot diagram:
a = [5,7,8,7,2,17,2,9,4,11,12,9,6]
b = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(a, b)
plt.show()

## RANDOM DATA DISTRIBUTION
# A scatter plot with 1000 dots:
A = np.random.normal(5.0, 1.0, 1000)
B = np.random.normal(10.0, 2.0, 1000)
plt.scatter(A, B)
plt.show()

## LINEAR REGRESSION
# Start by drawing a scatter plot:
age = [5,7,8,7,2,17,2,9,4,11,12,9,6]
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# draw the line of Linear Regression with scipy stats and linregress:
slope, intercept, r, p, std_err = stats.linregress(age, speed)
def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, age))

plt.scatter(age, speed)
plt.plot(age, mymodel)
plt.show()