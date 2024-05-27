def data_gen():
    while True:
        x = (np.random.random([1024])-0.5) * 10 
        y = np.sin(x)
        yield (x,y)

regressor = Sequential()
regressor.add(Dense(units=20, activation='tanh', input_dim=1))
regressor.add(Dense(units=20, activation='tanh'))
regressor.add(Dense(units=20, activation='tanh'))
regressor.add(Dense(units=1, activation='linear'))
regressor.compile(loss='mse', optimizer='adam')

regressor.fit_generator(data_gen(), epochs=3, steps_per_epoch=128)

x = (np.random.random([1024])-0.5)*10
x = np.sort(x)
y = np.sin(x)

plt.plot(x, y)
plt.plot(x, regressor.predict(x))
plt.show()

######################################################


from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import random
import numpy
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import ExtraTreesRegressor
from keras import optimizers

regressor = Sequential()
regressor.add(Dense(units=500, activation='sigmoid', kernel_initializer='uniform', input_dim=1))
regressor.add(Dense(units=500, activation='sigmoid', kernel_initializer='uniform'))
regressor.add(Dense(units=1, activation='sigmoid'))
regressor.compile(loss='mean_squared_error', optimizer='adam')
#regressor = ExtraTreesRegressor()

N = 5000

X = numpy.empty((N,))
Y = numpy.empty((N,))

for i in range(N):
    X[i] = random.uniform(-10, 10)

X = numpy.sort(X).reshape(-1, 1)

for i in range(N):
    Y[i] = numpy.sin(X[i])

Y = Y.reshape(-1, 1)

X_scaler = MinMaxScaler()
Y_scaler = MinMaxScaler()
X = X_scaler.fit_transform(X)
Y = Y_scaler.fit_transform(Y)

regressor.fit(X, Y, epochs=50, verbose=1, batch_size=2)
#regressor.fit(X, Y.reshape(5000,))

x = numpy.mgrid[-10:10:100*1j]
x = x.reshape(-1, 1)
y = numpy.mgrid[-10:10:100*1j]
y = y.reshape(-1, 1)
x = X_scaler.fit_transform(x)
for i in range(len(x)):
    y[i] = regressor.predict(numpy.array([x[i]]))


plt.figure()
plt.plot(X_scaler.inverse_transform(x), Y_scaler.inverse_transform(y))
plt.plot(X_scaler.inverse_transform(X), Y_scaler.inverse_transform(Y))