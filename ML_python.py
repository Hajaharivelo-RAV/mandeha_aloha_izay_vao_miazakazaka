# using scikit-learn NumPy array splitting SciPy and stuff
import numpy as np
from scipy import stats

# let's consider a set of data
set_of_data =  [86, 87, 88, 86, 87, 85, 86, 87, 88, 86, 87, 85]
sod = [77, 32, 111, 99, 56, 86, 90, 178, 45, 67, 89, 23]
# mean function mean() from numpy output the average value of the set of data
variable_1 = np.mean(set_of_data)
print(variable_1)
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
# Execute a method that returns some important key values of Linear Regression:
slope, intercept, r, p, std_err = stats.linregress(age, speed)
# Create a function that uses the slope and intercept values to return a new value. This new value represents where on the y-axis the corresponding x value will be placed:
def myfunc(x):
  return slope * x + intercept

# Run each value of the x array through the function. This will result in a new array with new values for the y-axis:
my_model = list(map(myfunc, age))
# Draw the original scatter plot
plt.scatter(age, speed)
# Draw the regression line
plt.plot(age, my_model)
plt.show()

## R and the linear regression
# How does my data related, well if r or the coefficient of correlation is between -1 to 1 where near both of these values a strong correlation and close to zero no relation at all
print(r)

## Predict future values
# with these data we created a model that we can use to predict a value corresponding to an input that we give to the model
# let's predict the speed of a car 10 years old of age
my_model10 = myfunc(10)
print(my_model10)

## Bad Fit?
#Let us create an example where linear regression would not be the best method to predict future values.
#These values for the x- and y-axis should result in a very bad fit for linear regression:
age_bf = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
speed_bf = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
slope_bf, intercept_bf, r_bf, p_bf, std_err_bf = stats.linregress(age_bf, speed_bf)

def myfunc(x):
  return slope_bf * x + intercept_bf

mymodel = list(map(myfunc, age_bf))
plt.scatter(age_bf, speed_bf)
plt.plot(age_bf, mymodel)
plt.show()
# r near 0
print(r_bf)

## Polynomial regression
# use of np.polyld() for polynomial regression
# Create the arrays that represent the values of the x (hours )and y (speed) axis:
hours = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
speed_sp = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# NumPy has a method that lets us make a polynomial model:
this_model = np.poly1d(np.polyfit(hours, speed_sp, 3))
# Then specify how the line will display, we start at position 1, and end at position 22:
the_line = np.linspace(1, 22, 100)
# draw the original plot, the line of polynomial regression and show the plot
plt.scatter(hours, speed_sp)
plt.plot(the_line, this_model(the_line))
plt.show()

## R-squared
# R2 is the metrics (range between 0 and 1) use to assess the relationship between x and y in the polynomial regression
# 0 there is no relationship at all (unusable for prediction) and 1 100% relationship (will predict)
# import the module for the assessment from scikit-learn
from sklearn.metrics import r2_score
# print the r2_score for the model
R2 = r2_score(speed_sp, this_model(hours))
if R2 < 0.05:
  print("r2_score :" + str(R2) + "too low there is no relationship")
else:
  print("r2_score :" + str(R2) + " strong relationship")

## Predicting future value
speed_sp17 = this_model(17)
print(speed_sp17)

## Bad fit
# lets consider an array that doesn't have any relation
poly_bf_hours = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
poly_bf_speed = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
poly_bf_model = np.poly1d(np.polyfit(poly_bf_hours, poly_bf_speed, 3))
poly_bf_line = np.linspace(2, 95, 100)
plt.scatter(poly_bf_hours, poly_bf_speed)
plt.plot(poly_bf_line, poly_bf_model(poly_bf_line))
plt.show()
bf_R2 = r2_score(poly_bf_speed, poly_bf_model(poly_bf_hours))
if bf_R2 <= 0.01:
  print("r2_score :" + str(bf_R2) + "too low, there is no relationship")
elif bf_R2 > 0.9:
  print("r2_score :" + str(bf_R2) + " strong relationship")