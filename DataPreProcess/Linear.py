import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D

# X1滑动窗口， X2历史同期
# dataX1 = [31, 102, 89, 98, 129, 142, 98]
# dataX2 = [50, 33, 99, 146, 134, 128, 150]
# dataY = [33, 99, 146, 134, 128, 150, 110]

# dataX1 = [21.5, 41, 46.5, 41.5, 45, 37, 39.5, 33, 53, 51, 50.5, 45, 46.5, 49.5, 47]
# dataX2 = [45, 33, 63, 87.5, 69.5, 73, 74.5, 76.5, 63.5, 76, 71.5, 64.5, 86.5, 60, 88.5]
# dataY = [33, 63, 87.5, 69.5, 64, 74.5, 76.5, 63.5, 76, 62.5, 64.5, 86.5, 60, 88.5, 70]

# dataX1 = [21.5, 46.5, 41.5, 45, 37, 39.5, 33, 53, 51, 50.5, 46.5, 47]
# dataX2 = [45, 33, 87.5, 69.5, 73, 74.5, 76.5, 63.5, 76, 71.5, 86.5, 88.5]
# dataY = [33, 63, 69.5, 64, 74.5, 76.5, 63.5, 76, 62.5, 64.5, 60, 70]

# Linear Regression
# dataX1 = [21.5, 41.5, 45, 37, 39.5, 33, 51, 50.5, 46.5, 47]
# dataX2 = [45, 87.5, 69.5, 73, 74.5, 76.5, 76, 71.5, 86.5, 88.5]
# dataY = [33, 69.5, 64, 74.5, 76.5, 63.5, 62.5, 64.5, 60, 70]


dataX1 = [66.4, 73.4, 55.0, 48.5, 63.8, 41.5, 65.3, 76.5, 74.6, 69.9]
dataX2 = [63.1, 76.2, 64.6, 41.1, 89.0, 44.2, 76.2, 67.6, 83.0, 77.0]
dataX3 = [74.3, 71.7, 68.6, 27.4, 109.5, 63.6, 71.7, 74.6, 86.7, 70.8]
dataY = [73.5, 58.5, 68.5, 31.5, 88.5, 54.5, 58.5, 72.5, 83.0, 79.0]

predictX1 = [41.5, 65.3, 76.5, 74.6, 69.9]
predictX2 = [44.2, 76.2, 67.6, 83.0, 77.0]
predictX3 = [63.6, 71.7, 74.6, 86.7, 70.8]
predictX = np.vstack((predictX1, predictX2, predictX3)).T



# print(predictX)


X1 = np.array([dataX1]).T
X2 = np.array([dataX2]).T
# X3 = np.array([dataX3]).T
X = np.vstack((dataX1, dataX2, dataX3)).T
print(X)
Y = np.array([dataY]).T


reg = linear_model.LinearRegression()
reg.fit(X, Y)
predict = reg.predict(predictX)
print(reg.intercept_)
print(reg.coef_)
print(reg.score(X, Y))

for i in predict:
    print(i)


'''
predict = reg.predict(predictX)

for i in predict:
    print(i)
print(reg.intercept_)
print(reg.coef_)
print(reg.score(X, Y))

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(X1, X2, Y)

X1line, X2line = np.meshgrid(np.arange(20, 80, 10), np.arange(20, 80, 10))
Yline = reg.coef_[0][0]*X1line + reg.coef_[0][1]*X2line + reg.intercept_[0]

# ax.plot_wireframe(X1line, X2line, Yline)
ax.plot_surface(X1line, X2line, Yline)

plt.title('3D Linear Regression')
plt.show()
'''

'''
reg1 = linear_model.LinearRegression()
reg1.fit(X1, Y)
print(reg1.intercept_)
print(reg1.coef_)
print(reg1.score(X1, Y))

reg2 = linear_model.LinearRegression()
reg2.fit(X2, Y)
print(reg2.intercept_)
print(reg2.coef_)
print(reg2.score(X2, Y))

plt.subplot(121)
plt.scatter(X1, Y, color='black')
plt.plot(X1, reg1.predict(X1), color='red', linewidth=1, marker='o')
plt.title('Slide Window : Linear Regression')

plt.subplot(122)
plt.scatter(X2, Y, color='black')
plt.plot(X2, reg2.predict(X2), color='red', linewidth=1, marker='o')
plt.title('Historical Period : Linear Regression')

plt.show()
'''